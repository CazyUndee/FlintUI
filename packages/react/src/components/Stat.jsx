export default function Stat({ 
  value, 
  label,
  delta,
  deltaType = 'up',
  className = '' 
}) {
  return (
    <div className={`cn-stat ${className}`}>
      <div className="cn-stat-value">{value}</div>
      {label && <div className="cn-stat-label">{label}</div>}
      {delta && (
        <div className={`cn-stat-delta cn-stat-delta-${deltaType}`}>
          {deltaType === 'up' ? '↑' : '↓'} {delta}
        </div>
      )}
    </div>
  );
}
