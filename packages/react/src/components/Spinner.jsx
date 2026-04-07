export default function Spinner({ size = 'md', className = '' }) {
  const sizeClass = size !== 'md' ? `cn-spinner-${size}` : '';

  return <div className={`cn-spinner ${sizeClass} ${className}`}></div>;
}
