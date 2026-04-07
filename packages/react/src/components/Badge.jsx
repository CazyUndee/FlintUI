export default function Badge({ 
  children, 
  variant = 'default', 
  size = 'md',
  className = '' 
}) {
  const variantClass = variant !== 'default' ? `cn-badge-${variant}` : '';
  const sizeClass = size !== 'md' ? `cn-badge-${size}` : '';

  return (
    <span className={`cn-badge ${variantClass} ${sizeClass} ${className}`}>
      {children}
    </span>
  );
}
