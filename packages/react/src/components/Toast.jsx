import { useState, useEffect, useRef } from 'react';

function ToastContainer() {
  return <div className="cn-toast-container" />;
}

function ToastItem({ toast, onRemove }) {
  useEffect(() => {
    if (toast.duration > 0) {
      const timer = setTimeout(() => onRemove(toast.id), toast.duration);
      return () => clearTimeout(timer);
    }
  }, [toast.id, toast.duration, onRemove]);

  const icons = {
    success: '<polyline points="20 6 9 17 4 12"></polyline>',
    error: '<circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line>',
    warning: '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line>',
    info: '<circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line>'
  };

  return (
    <div className={`cn-toast cn-toast-${toast.type}`}>
      <div className="cn-alert-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" dangerouslySetInnerHTML={{ __html: icons[toast.type] }} />
      </div>
      <div className="cn-alert-content">
        {toast.title && <div className="cn-alert-title">{toast.title}</div>}
        {toast.message && <div className="cn-alert-message">{toast.message}</div>}
      </div>
      {toast.closable && (
        <button className="cn-alert-close" onClick={() => onRemove(toast.id)}>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" width="16" height="16">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>
      )}
    </div>
  );
}

export default function Toast({ toasts = [], onRemove }) {
  return (
    <div className="cn-toast-container">
      {toasts.map((toast) => (
        <ToastItem key={toast.id} toast={toast} onRemove={onRemove} />
      ))}
    </div>
  );
}

export function useToast() {
  const [toasts, setToasts] = useState([]);
  const idRef = useRef(0);

  const addToast = (options) => {
    const id = ++idRef.current;
    const toast = { id, duration: 4000, closable: true, type: 'info', ...options };
    setToasts((prev) => [...prev, toast]);
    return id;
  };

  const removeToast = (id) => {
    setToasts((prev) => prev.filter((t) => t.id !== id));
  };

  const toast = {
    success: (message, title) => addToast({ message, title, type: 'success' }),
    error: (message, title) => addToast({ message, title, type: 'error' }),
    warning: (message, title) => addToast({ message, title, type: 'warning' }),
    info: (message, title) => addToast({ message, title, type: 'info' }),
    show: addToast,
    remove: removeToast
  };

  return { toasts, toast, removeToast };
}
