export default function Tooltip({ 
  children, 
  content,
  className = '' 
}) {
  return (
    <div className={`cn-tooltip ${className}`}>
      {children}
      <div className="cn-tooltip-content">{content}</div>
    </div>
  );
}
