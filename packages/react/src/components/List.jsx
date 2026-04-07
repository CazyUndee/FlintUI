export function List({ children, className = '' }) {
  return <div className={`cn-list ${className}`}>{children}</div>;
}

export function ListItem({ 
  children, 
  icon,
  title,
  subtitle,
  actions,
  clickable = false,
  onClick,
  className = '' 
}) {
  return (
    <div 
      className={`cn-list-item ${clickable ? 'cn-list-item-clickable' : ''} ${className}`}
      onClick={onClick}
    >
      {icon && <div className="cn-list-item-icon">{icon}</div>}
      <div className="cn-list-item-content">
        {title && <div className="cn-list-item-title">{title}</div>}
        {subtitle && <div className="cn-list-item-subtitle">{subtitle}</div>}
        {children}
      </div>
      {actions && <div className="cn-list-item-actions">{actions}</div>}
    </div>
  );
}
