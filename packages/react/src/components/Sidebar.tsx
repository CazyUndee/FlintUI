import * as React from 'react';

export interface SidebarProps extends React.HTMLAttributes<HTMLElement> {
  header?: React.ReactNode;
  footer?: React.ReactNode;
}

export interface SidebarItemProps extends React.HTMLAttributes<HTMLAnchorElement | HTMLDivElement> {
  active?: boolean;
  icon?: React.ReactNode;
  href?: string;
}

export const Sidebar: React.FC<SidebarProps> & {
  Item: React.FC<SidebarItemProps>;
} = Object.assign(
  ({ header, footer, children, className = '', ...props }: SidebarProps) => {
    return (
      <aside className={`cn-sidebar ${className}`.trim()} {...props}>
        {header && <div className="cn-sidebar-header">{header}</div>}
        <div className="cn-sidebar-nav">{children}</div>
        {footer && <div className="cn-sidebar-footer">{footer}</div>}
      </aside>
    );
  },
  {
    Item: ({ children, active = false, icon, href, className = '', ...props }: SidebarItemProps) => {
      const content = (
        <>
          {icon && <span className="cn-sidebar-item-icon">{icon}</span>}
          {children}
        </>
      );

      if (href) {
        return (
          <a
            href={href}
            className={`cn-sidebar-item ${active ? 'cn-sidebar-active' : ''} ${className}`.trim()}
            role="menuitem"
            {...(props as React.AnchorHTMLAttributes<HTMLAnchorElement>)}
          >
            {content}
          </a>
        );
      }

      return (
        <div
          className={`cn-sidebar-item ${active ? 'cn-sidebar-active' : ''} ${className}`.trim()}
          role="menuitem"
          {...(props as React.HTMLAttributes<HTMLDivElement>)}
        >
          {content}
        </div>
      );
    },
  }
);

Sidebar.displayName = 'Sidebar';
(Sidebar.Item as React.FC<SidebarItemProps> & { displayName?: string }).displayName = 'SidebarItem';

export default Sidebar;
