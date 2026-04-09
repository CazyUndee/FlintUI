import * as React from 'react';

export type ToastType = 'success' | 'error' | 'warning' | 'info';

export interface ToastOptions {
  id?: number;
  title?: string;
  message: string;
  type?: ToastType;
  duration?: number;
  closable?: boolean;
}

export interface ToastProps {
  toasts: ToastOptions[];
  onRemove: (id: number) => void;
}

export interface UseToastReturn {
  toasts: ToastOptions[];
  toast: {
    success: (message: string, title?: string) => number;
    error: (message: string, title?: string) => number;
    warning: (message: string, title?: string) => number;
    info: (message: string, title?: string) => number;
    show: (options: ToastOptions) => number;
    remove: (id: number) => void;
  };
  removeToast: (id: number) => void;
}

const ToastItem: React.FC<{ toast: ToastOptions; onRemove: (id: number) => void }> = ({ toast, onRemove }) => {
  const [isLeaving, setIsLeaving] = React.useState(false);

  React.useEffect(() => {
    if (toast.duration && toast.duration > 0) {
      const timer = setTimeout(() => handleRemove(toast.id!), toast.duration);
      return () => clearTimeout(timer);
    }
  }, [toast.id, toast.duration]);

  const handleRemove = (id: number) => {
    setIsLeaving(true);
    setTimeout(() => onRemove(id), 200);
  };

  const icons: Record<ToastType, React.ReactNode> = {
    success: <polyline points="20 6 9 17 4 12" />,
    error: (
      <>
        <circle cx="12" cy="12" r="10" />
        <line x1="15" y1="9" x2="9" y2="15" />
        <line x1="9" y1="9" x2="15" y2="15" />
      </>
    ),
    warning: (
      <>
        <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z" />
        <line x1="12" y1="9" x2="12" y2="13" />
        <line x1="12" y1="17" x2="12.01" y2="17" />
      </>
    ),
    info: (
      <>
        <circle cx="12" cy="12" r="10" />
        <line x1="12" y1="16" x2="12" y2="12" />
        <line x1="12" y1="8" x2="12.01" y2="8" />
      </>
    ),
  };

  return (
    <div className={`cn-toast cn-toast-${toast.type} ${isLeaving ? 'cn-toast-leaving' : ''}`.trim()} role="alert">
      <div className="cn-alert-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          {icons[toast.type || 'info']}
        </svg>
      </div>
      <div className="cn-alert-content">
        {toast.title && <div className="cn-alert-title">{toast.title}</div>}
        {toast.message && <div className="cn-alert-message">{toast.message}</div>}
      </div>
      {toast.closable && (
        <button className="cn-alert-close" onClick={() => handleRemove(toast.id!)} aria-label="Close">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" width="16" height="16">
            <line x1="18" y1="6" x2="6" y2="18" />
            <line x1="6" y1="6" x2="18" y2="18" />
          </svg>
        </button>
      )}
    </div>
  );
};

export const Toast: React.FC<ToastProps> = ({ toasts = [], onRemove }) => {
  return (
    <div className="cn-toast-container">
      {toasts.map((toast) => (
        <ToastItem key={toast.id} toast={toast} onRemove={onRemove} />
      ))}
    </div>
  );
};

Toast.displayName = 'Toast';

export function useToast(): UseToastReturn {
  const [toasts, setToasts] = React.useState<ToastOptions[]>([]);
  const idRef = React.useRef(0);

  const addToast = (options: ToastOptions): number => {
    const id = ++idRef.current;
    const toast: ToastOptions = { id, duration: 4000, closable: true, type: 'info', ...options };
    setToasts((prev) => [...prev, toast]);
    return id;
  };

  const removeToast = (id: number) => {
    setToasts((prev) => prev.filter((t) => t.id !== id));
  };

  const toast = {
    success: (message: string, title?: string) => addToast({ message, title, type: 'success' }),
    error: (message: string, title?: string) => addToast({ message, title, type: 'error' }),
    warning: (message: string, title?: string) => addToast({ message, title, type: 'warning' }),
    info: (message: string, title?: string) => addToast({ message, title, type: 'info' }),
    show: addToast,
    remove: removeToast,
  };

  return { toasts, toast, removeToast };
}

export default Toast;
