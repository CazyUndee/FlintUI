import * as React from 'react';

export interface ListProps extends React.HTMLAttributes<HTMLDivElement> {}

export interface ListItemProps extends React.HTMLAttributes<HTMLDivElement> {
  icon?: React.ReactNode;
  title?: string;
  subtitle?: string;
  actions?: React.ReactNode;
  clickable?: boolean;
}

export const List: React.FC<ListProps> = ({ children, className = '', ...props }) => {
  return (
    <div className={`cn-list ${className}`.trim()} role="list" {...props}>
      {children}
    </div>
  );
};

List.displayName = 'List';

export const ListItem: React.FC<ListItemProps> = ({
  children,
  icon,
  title,
  subtitle,
  actions,
  clickable = false,
  onClick,
  className = '',
  ...props
}) => {
  return (
    <div
      className={`cn-list-item ${clickable ? 'cn-list-item-clickable' : ''} ${className}`.trim()}
      onClick={onClick}
      role={clickable ? 'button' : 'listitem'}
      tabIndex={clickable ? 0 : undefined}
      {...props}
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
};

ListItem.displayName = 'ListItem';

export default List;
