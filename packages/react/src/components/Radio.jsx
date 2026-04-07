import { forwardRef } from 'react';

const Radio = forwardRef(function Radio({ 
  checked = false, 
  onChange, 
  disabled = false,
  children,
  name,
  className = '',
  ...props 
}, ref) {
  return (
    <label className={`cn-radio ${disabled ? 'disabled' : ''} ${className}`}>
      <input
        ref={ref}
        type="radio"
        checked={checked}
        onChange={(e) => onChange?.(e.target.checked)}
        disabled={disabled}
        name={name}
        {...props}
      />
      <span className="cn-radio-box"></span>
      {children && <span className="cn-radio-label">{children}</span>}
    </label>
  );
});

export function RadioGroup({ children, name, value, onChange, className = '' }) {
  return (
    <div className={className} role="radiogroup">
      {children.map((child, idx) => {
        if (child.type?.displayName === 'Radio') {
          return {
            ...child,
            props: {
              ...child.props,
              name,
              checked: child.props.value === value,
              onChange: () => onChange?.(child.props.value),
            }
          };
        }
        return child;
      })}
    </div>
  );
}

export default Radio;
