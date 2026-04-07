import { useState, useEffect, useRef } from 'react';

export default function CommandPalette({ 
  items = [],
  isOpen = false,
  onClose,
  onSelect,
  placeholder = 'Search commands...',
  className = '' 
}) {
  const [query, setQuery] = useState('');
  const [activeIndex, setActiveIndex] = useState(0);
  const inputRef = useRef(null);

  const filtered = items.filter(item =>
    item.title.toLowerCase().includes(query.toLowerCase()) ||
    (item.subtitle && item.subtitle.toLowerCase().includes(query.toLowerCase()))
  );

  useEffect(() => {
    if (isOpen) {
      setQuery('');
      setActiveIndex(0);
      setTimeout(() => inputRef.current?.focus(), 100);
    }
  }, [isOpen]);

  useEffect(() => {
    const handleKeyDown = (e) => {
      if (!isOpen) return;

      if (e.key === 'Escape') {
        onClose?.();
      } else if (e.key === 'ArrowDown') {
        e.preventDefault();
        setActiveIndex(i => Math.min(i + 1, filtered.length - 1));
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        setActiveIndex(i => Math.max(i - 1, 0));
      } else if (e.key === 'Enter' && filtered[activeIndex]) {
        handleSelect(filtered[activeIndex]);
      }
    };

    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, filtered, activeIndex, onClose]);

  const handleSelect = (item) => {
    item.action?.();
    onSelect?.(item);
    onClose?.();
  };

  if (!isOpen) return null;

  return (
    <div className={`cn-command-palette cn-command-palette-open ${className}`} onClick={(e) => e.target === e.currentTarget && onClose?.()}>
      <div className="cn-command-palette-inner">
        <input
          ref={inputRef}
          type="text"
          className="cn-command-palette-input"
          placeholder={placeholder}
          value={query}
          onChange={(e) => {
            setQuery(e.target.value);
            setActiveIndex(0);
          }}
        />
        <div className="cn-command-palette-results">
          {filtered.map((item, idx) => (
            <div
              key={idx}
              className={`cn-command-item ${idx === activeIndex ? 'cn-command-item-active' : ''}`}
              onClick={() => handleSelect(item)}
              onMouseEnter={() => setActiveIndex(idx)}
            >
              {item.icon && <div className="cn-command-item-icon">{item.icon}</div>}
              <div className="cn-command-item-content">
                <div className="cn-command-item-title">{item.title}</div>
                {item.subtitle && (
                  <div className="cn-command-item-subtitle">{item.subtitle}</div>
                )}
              </div>
              {item.kbd && <div className="cn-command-item-kbd">{item.kbd}</div>}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
