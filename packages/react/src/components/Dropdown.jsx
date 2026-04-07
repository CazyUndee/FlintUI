import { useState, useEffect, useRef } from 'react';

export default function Dropdown({ 
  trigger,
  children,
  className = '' 
}) {
  const [isOpen, setIsOpen] = useState(false);
  const dropdownRef = useRef(null);

  const toggle = () => setIsOpen((prev) => !prev);
  const close = () => setIsOpen(false);

  useEffect(() => {
    const handleClickOutside = (e) => {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target)) {
        close();
      }
    };

    if (isOpen) {
      document.addEventListener('click', handleClickOutside);
    }

    return () => {
      document.removeEventListener('click', handleClickOutside);
    };
  }, [isOpen]);

  return (
    <div ref={dropdownRef} className={`cn-dropdown ${isOpen ? 'cn-dropdown-open' : ''} ${className}`}>
      <div className="cn-dropdown-trigger" onClick={toggle}>
        {trigger}
      </div>
      <div className="cn-dropdown-menu" onClick={close}>
        {children}
      </div>
    </div>
  );
}

export function DropdownItem({ children, onClick, className = '', ...props }) {
  return (
    <div className={`cn-dropdown-item ${className}`} onClick={onClick} {...props}>
      {children}
    </div>
  );
}
