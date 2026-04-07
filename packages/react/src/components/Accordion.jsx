import { useState } from 'react';

export default function Accordion({ 
  allowMultiple = false, 
  defaultOpen = [],
  children,
  className = '' 
}) {
  const [openItems, setOpenItems] = useState(new Set(defaultOpen));

  const toggleItem = (index) => {
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

  const items = Array.isArray(children) ? children : [children];

  return (
    <div className={`cn-accordion ${className}`}>
      {items.map((child, idx) => (
        <div key={idx} className={`cn-accordion-item ${openItems.has(idx) ? 'cn-accordion-open' : ''}`}>
          <div className="cn-accordion-header" onClick={() => toggleItem(idx)}>
            <span>{child.props.title}</span>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" width="20" height="20">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </div>
          <div className="cn-accordion-content">
            {child.props.children}
          </div>
        </div>
      ))}
    </div>
  );
}

export function AccordionItem({ children }) {
  return children;
}
AccordionItem.displayName = 'AccordionItem';
