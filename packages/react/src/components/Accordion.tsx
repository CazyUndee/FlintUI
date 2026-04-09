import * as React from 'react';

export interface AccordionProps extends React.HTMLAttributes<HTMLDivElement> {
  allowMultiple?: boolean;
  defaultOpen?: number[];
}

export interface AccordionItemProps {
  title: string;
  children: React.ReactNode;
}

export const Accordion: React.FC<AccordionProps> & {
  Item: React.FC<AccordionItemProps>;
} = Object.assign(
  ({ allowMultiple = false, defaultOpen = [], children, className = '', ...props }: AccordionProps) => {
    const [openItems, setOpenItems] = React.useState(new Set(defaultOpen));

    const toggleItem = (index: number) => {
      setOpenItems((prev) => {
        const next = new Set(prev);
        if (next.has(index)) {
          next.delete(index);
        } else {
          if (!allowMultiple) {
            next.clear();
          }
          next.add(index);
        }
        return next;
      });
    };

    const items = React.Children.toArray(children);

    return (
      <div className={`cn-accordion ${className}`.trim()} {...props}>
        {items.map((child, idx) => {
          if (React.isValidElement<AccordionItemProps>(child)) {
            return (
              <div
                key={idx}
                className={`cn-accordion-item ${openItems.has(idx) ? 'cn-accordion-open' : ''}`.trim()}
              >
                <div
                  className="cn-accordion-header"
                  onClick={() => toggleItem(idx)}
                  role="button"
                  tabIndex={0}
                  aria-expanded={openItems.has(idx)}
                  onKeyDown={(e) => {
                    if (e.key === 'Enter' || e.key === ' ') {
                      e.preventDefault();
                      toggleItem(idx);
                    }
                  }}
                >
                  <span className="cn-accordion-title">{child.props.title}</span>
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" width="20" height="20" className="cn-accordion-icon">
                    <polyline points="6 9 12 15 18 9" />
                  </svg>
                </div>
                <div className="cn-accordion-content">
                  {child.props.children}
                </div>
              </div>
            );
          }
          return child;
        })}
      </div>
    );
  },
  {
    Item: ({ children }: AccordionItemProps) => <>{children}</>,
  }
);

Accordion.displayName = 'Accordion';
(Accordion.Item as React.FC<AccordionItemProps> & { displayName?: string }).displayName = 'AccordionItem';

export default Accordion;
