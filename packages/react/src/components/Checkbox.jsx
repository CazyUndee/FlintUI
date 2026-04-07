import { forwardRef } from 'react';

const Checkbox = forwardRef(function Checkbox({ 
  checked = false, 
  onChange, 
  disabled = false,
  children,
  className = '',
  ...props 
}, ref) {
  return (
    <label className={`cn-checkbox ${disabled ? 'disabled' : ''} ${className}`}>
      <input
        ref={ref}
        type="checkbox"
        checked={checked}
        onChange={(e) => onChange?.(e.target.checked)}
        disabled={disabled}
        {...props}
      />
      <span className="cn-checkbox-box"></span>
      {children && <span className="cn-checkbox-label">{children}</span>}
    </label>
  );
});

export default Checkbox;
