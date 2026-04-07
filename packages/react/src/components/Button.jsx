export default function Button({ 
  children, 
  variant = 'default', 
  size = 'md', 
  disabled = false,
  className = '',
  ...props 
}) {
  const variantClass = variant !== 'default' ? `cn-btn-${variant}` : '';
  const sizeClass = size !== 'md' ? `cn-btn-${size}` : '';

  return (
    <button 
      className={`cn-btn ${variantClass} ${sizeClass} ${className}`}
      disabled={disabled}
      {...props}
    >
      {children}
    </button>
  );
}
