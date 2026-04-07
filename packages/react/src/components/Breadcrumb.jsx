export function Breadcrumb({ children, className = '' }) {
  const items = Array.isArray(children) ? children : [children];

  return (
    <nav className={`cn-breadcrumb ${className}`}>
      {items.map((child, idx) => (
        <span key={idx}>
          {child}
          {idx < items.length - 1 && (
            <span className="cn-breadcrumb-separator">/</span>
          )}
        </span>
      ))}
    </nav>
  );
}

export function BreadcrumbItem({ children, href, active = false, className = '' }) {
  if (active) {
    return <span className={`cn-breadcrumb-current ${className}`}>{children}</span>;
  }
  return (
    <a href={href} className={`cn-breadcrumb-item ${className}`}>
      {children}
    </a>
  );
}
