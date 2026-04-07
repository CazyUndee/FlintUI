export default function Progress({ 
  value = 0, 
  max = 100,
  showLabel = false,
  variant = 'default',
  size = 'md',
  className = '' 
}) {
  const percentage = Math.min(Math.max((value / max) * 100, 0), 100);

  return (
    <div className={className}>
      {showLabel && (
        <div className="cn-progress-label">
          <span>{percentage.toFixed(0)}%</span>
        </div>
      )}
      <div className={`cn-progress ${size !== 'md' ? `cn-progress-${size}` : ''} ${variant !== 'default' ? `cn-progress-${variant}` : ''}`}>
        <div className="cn-progress-bar" style={{ width: `${percentage}%` }}></div>
      </div>
    </div>
  );
}
