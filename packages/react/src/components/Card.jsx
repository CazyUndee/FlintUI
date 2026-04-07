export default function Card({ 
  children, 
  hoverable = false,
  className = '' 
}) {
  return (
    <div className={`cn-card ${hoverable ? 'cn-card-hoverable' : ''} ${className}`}>
      {children}
    </div>
  );
}

Card.Header = function CardHeader({ children, className = '' }) {
  return <div className={`cn-card-header ${className}`}>{children}</div>;
};

Card.Body = function CardBody({ children, className = '' }) {
  return <div className={`cn-card-body ${className}`}>{children}</div>;
};

Card.Footer = function CardFooter({ children, className = '' }) {
  return <div className={`cn-card-footer ${className}`}>{children}</div>;
};
