import { forwardRef } from 'react';

const Select = forwardRef(function Select({ 
  options = [],
  value,
  onChange,
  placeholder = 'Select...',
  disabled = false,
  className = '',
  ...props 
}, ref) {
  return (
    <div className={`cn-select-wrapper ${className}`}>
      <select
        ref={ref}
        className="cn-select"
        value={value}
        onChange={(e) => onChange?.(e.target.value)}
        disabled={disabled}
        {...props}
      >
        {placeholder && <option value="" disabled>{placeholder}</option>}
        {options.map((opt, idx) => (
          <option key={idx} value={opt.value}>
            {opt.label}
          </option>
        ))}
      </select>
    </div>
  );
});

export default Select;
