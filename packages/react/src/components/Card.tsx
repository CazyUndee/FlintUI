import * as React from 'react';

export interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  clickable?: boolean;
}

export interface CardHeaderProps extends React.HTMLAttributes<HTMLDivElement> {}

export interface CardBodyProps extends React.HTMLAttributes<HTMLDivElement> {}

export interface CardFooterProps extends React.HTMLAttributes<HTMLDivElement> {}

export interface CardIconProps extends React.HTMLAttributes<HTMLDivElement> {}

export interface CardTitleProps extends React.HTMLAttributes<HTMLDivElement> {}

export interface CardSubtitleProps extends React.HTMLAttributes<HTMLDivElement> {}

export const Card: React.FC<CardProps> & {
  Header: React.FC<CardHeaderProps>;
  Body: React.FC<CardBodyProps>;
  Footer: React.FC<CardFooterProps>;
  Icon: React.FC<CardIconProps>;
  Title: React.FC<CardTitleProps>;
  Subtitle: React.FC<CardSubtitleProps>;
} = Object.assign(
  ({ children, clickable = false, className = '', ...props }: CardProps) => {
    return (
      <div
        className={`cn-card ${clickable ? 'cn-card-clickable' : ''} ${className}`.trim()}
        {...props}
      >
        {children}
      </div>
    );
  },
  {
    Header: ({ children, className = '', ...props }: CardHeaderProps) => (
      <div className={`cn-card-header ${className}`.trim()} {...props}>{children}</div>
    ),
    Body: ({ children, className = '', ...props }: CardBodyProps) => (
      <div className={`cn-card-body ${className}`.trim()} {...props}>{children}</div>
    ),
    Footer: ({ children, className = '', ...props }: CardFooterProps) => (
      <div className={`cn-card-footer ${className}`.trim()} {...props}>{children}</div>
    ),
    Icon: ({ children, className = '', ...props }: CardIconProps) => (
      <div className={`cn-card-icon ${className}`.trim()} {...props}>
        {children}
      </div>
    ),
    Title: ({ children, className = '', ...props }: CardTitleProps) => (
      <div className={`cn-card-title ${className}`.trim()} {...props}>{children}</div>
    ),
    Subtitle: ({ children, className = '', ...props }: CardSubtitleProps) => (
      <div className={`cn-card-subtitle ${className}`.trim()} {...props}>{children}</div>
    ),
  }
);

Card.displayName = 'Card';
Card.Header.displayName = 'Card.Header';
Card.Body.displayName = 'Card.Body';
Card.Footer.displayName = 'Card.Footer';
Card.Icon.displayName = 'Card.Icon';
Card.Title.displayName = 'Card.Title';
Card.Subtitle.displayName = 'Card.Subtitle';

export default Card;
