export default function Skeleton({ 
  variant = 'text', 
  width,
  height,
  className = '' 
}) {
  const variantClass = variant !== 'text' ? `cn-skeleton-${variant}` : 'cn-skeleton';

  const style = {
    width: width,
    height: height,
  };

  return <div className={`${variantClass} ${className}`} style={style}></div>;
}
