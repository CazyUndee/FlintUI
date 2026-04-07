import { useState } from 'react';

export default function Alert({ 
  type = 'info', 
  title,
  children,
  closable = true,
  onClose,
  className = '' 
}) {
  const [visible, setVisible] = useState(true);

  const handleClose = () => {
    setVisible(false);
    onClose?.();
  };

  if (!visible) return null;

  return (
    <div className={`cn-alert cn-alert-${type} ${className}`}>
      <div className="cn-alert-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          {type === 'success' && <polyline points="20 6 9 17 4 12"></polyline>}
          {type === 'error' && (
            <>
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="15" y1="9" x2="9" y2="15"></line>
              <line x1="9" y1="9" x2="15" y2="15"></line>
            </>
          )}
          {type === 'warning' && (
            <>
              <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
              <line x1="12" y1="9" x2="12" y2="13"></line>
              <line x1="12" y1="17" x2="12.01" y2="17"></line>
            </>
          )}
          {type === 'info' && (
            <>
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="12" y1="16" x2="12" y2="12"></line>
              <line x1="12" y1="8" x2="12.01" y2="8"></line>
            </>
          )}
        </svg>
      </div>
      <div className="cn-alert-content">
        {title && <div className="cn-alert-title">{title}</div>}
        <div className="cn-alert-message">{children}</div>
      </div>
      {closable && (
        <button className="cn-alert-close" onClick={handleClose}>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" width="16" height="16">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>
      )}
    </div>
  );
}
