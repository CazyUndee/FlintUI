import { useEffect, useRef } from 'react';

export default function Modal({ 
  isOpen = false, 
  onClose, 
  children,
  className = '' 
}) {
  const modalRef = useRef(null);

  useEffect(() => {
    const handleEscape = (e) => {
      if (e.key === 'Escape' && onClose) {
        onClose();
      }
    };

    if (isOpen) {
      document.addEventListener('keydown', handleEscape);
      document.body.style.overflow = 'hidden';
    }

    return () => {
      document.removeEventListener('keydown', handleEscape);
      document.body.style.overflow = '';
    };
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <div 
      className={`cn-modal-backdrop cn-modal-open ${className}`}
      onClick={(e) => e.target === e.currentTarget && onClose?.()}
    >
      <div className="cn-modal" ref={modalRef}>
        {children}
      </div>
    </div>
  );
}

Modal.Header = function ModalHeader({ children, onClose, className = '' }) {
  return (
    <div className={`cn-modal-header ${className}`}>
      <div className="cn-modal-title">{children}</div>
      {onClose && (
        <button className="cn-modal-close" onClick={onClose}>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>
      )}
    </div>
  );
};

Modal.Body = function ModalBody({ children, className = '' }) {
  return <div className={`cn-modal-body ${className}`}>{children}</div>;
};

Modal.Footer = function ModalFooter({ children, className = '' }) {
  return <div className={`cn-modal-footer ${className}`}>{children}</div>;
};
