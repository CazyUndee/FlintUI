import { useState } from 'react';

export default function Tabs({ 
  defaultIndex = 0, 
  index: controlledIndex, 
  onChange, 
  children,
  className = '' 
}) {
  const [internalIndex, setInternalIndex] = useState(defaultIndex);
  const activeIndex = controlledIndex !== undefined ? controlledIndex : internalIndex;

  const handleTabClick = (idx) => {
    if (onChange) {
      onChange(idx);
    } else {
      setInternalIndex(idx);
    }
  };

  const tabs = [];
  const panels = [];

  children.forEach((child) => {
    if (child.type?.displayName === 'Tab') {
      tabs.push(child);
    } else if (child.type?.displayName === 'TabPanel') {
      panels.push(child);
    }
  });

  return (
    <div className={className}>
      <div className="cn-tabs">
        {tabs.map((tab, idx) => (
          <div
            key={idx}
            className={`cn-tab ${activeIndex === idx ? 'cn-tab-active' : ''}`}
            onClick={() => handleTabClick(idx)}
          >
            {tab.props.children}
          </div>
        ))}
      </div>
      {panels.map((panel, idx) => (
        <div
          key={idx}
          className={`cn-tab-panel ${activeIndex === idx ? 'cn-tab-panel-active' : ''}`}
        >
          {panel.props.children}
        </div>
      ))}
    </div>
  );
}

export function Tab({ children }) {
  return children;
}
Tab.displayName = 'Tab';

export function TabPanel({ children }) {
  return children;
}
TabPanel.displayName = 'TabPanel';
