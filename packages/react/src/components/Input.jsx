import { forwardRef } from 'react';

const Input = forwardRef(function Input({ 
  type = 'text',
  size = 'md',
  error = false,
  className = '',
  ...props 
}, ref) {
  const sizeClass = size !== 'md' ? `cn-input-${size}` : '';

  return (
    <input 
      ref={ref}
      type={type}
      className={`cn-input ${sizeClass} ${error ? 'cn-input-error' : ''} ${className}`}
      {...props}
    />
  );
});

export default Input;
