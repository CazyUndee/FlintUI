export default function Avatar({ 
  src, 
  alt = '', 
  initials,
  size = 'md',
  className = '' 
}) {
  const sizeClass = size !== 'md' ? `cn-avatar-${size}` : '';

  return (
    <div className={`cn-avatar ${sizeClass} ${className}`}>
      {src ? (
        <img src={src} alt={alt} />
      ) : initials ? (
        initials
      ) : null}
    </div>
  );
}

export function AvatarGroup({ children, max, className = '' }) {
  const items = Array.isArray(children) ? children : [children];
  const visible = max ? items.slice(0, max) : items;
  const remaining = max ? items.length - max : 0;

  return (
    <div className={`cn-avatar-group ${className}`}>
      {visible}
      {remaining > 0 && (
        <div className="cn-avatar">+{remaining}</div>
      )}
    </div>
  );
}
