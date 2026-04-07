import { useState } from 'react';

export default function Nav({ 
  defaultActive, 
  active: controlledActive, 
  onChange, 
  children,
  className = '' 
}) {
  const [internalActive, setInternalActive] = useState(defaultActive);
  const activeItem = controlledActive !== undefined ? controlledActive : internalActive;

  const handleClick = (item) => {
    if (onChange) {
      onChange(item);
    } else {
      setInternalActive(item);
    }
  };

  return (
    <nav className={`cn-nav ${className}`}>
      {children.map((child, idx) => {
        const isActive = child.props.active !== undefined 
          ? child.props.active 
          : child.props.id === activeItem;

        return {
          ...child,
          props: {
            ...child.props,
            active: isActive,
            onClick: () => handleClick(child.props.id),
          }
        };
      })}
    </nav>
  );
}

export function NavItem({ children, active = false, onClick, className = '' }) {
  return (
    <div 
      className={`cn-nav-item ${active ? 'cn-nav-active' : ''} ${className}`}
      onClick={onClick}
    >
      {children}
    </div>
  );
}
