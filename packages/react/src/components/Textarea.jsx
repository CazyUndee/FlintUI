import { forwardRef } from 'react';

const Textarea = forwardRef(function Textarea({ 
  error = false,
  className = '',
  ...props 
}, ref) {
  return (
    <textarea 
      ref={ref}
      className={`cn-input cn-textarea ${error ? 'cn-input-error' : ''} ${className}`}
      {...props}
    />
  );
});

export default Textarea;
