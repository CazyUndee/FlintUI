import * as React from 'react';

export interface CommandPaletteItem {
  title: string;
  subtitle?: string;
  icon?: React.ReactNode;
  kbd?: string;
  action?: () => void;
}

export interface CommandPaletteProps extends Omit<React.HTMLAttributes<HTMLDivElement>, 'onSelect'> {
  items?: CommandPaletteItem[];
  isOpen?: boolean;
  onClose?: () => void;
  onSelect?: (item: CommandPaletteItem) => void;
  placeholder?: string;
}

export const CommandPalette: React.FC<CommandPaletteProps> = ({
  items = [],
  isOpen = false,
  onClose,
  onSelect,
  placeholder = 'Search commands...',
  className = '',
  ...props
}) => {
  const [query, setQuery] = React.useState('');
  const [activeIndex, setActiveIndex] = React.useState(0);
  const inputRef = React.useRef<HTMLInputElement>(null);

  const filtered = items.filter(
    (item) =>
      item.title.toLowerCase().includes(query.toLowerCase()) ||
      (item.subtitle && item.subtitle.toLowerCase().includes(query.toLowerCase()))
  );

  React.useEffect(() => {
    if (isOpen) {
      setQuery('');
      setActiveIndex(0);
      setTimeout(() => inputRef.current?.focus(), 100);
    }
  }, [isOpen]);

  React.useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (!isOpen) return;

      if (e.key === 'Escape') {
        onClose?.();
      } else if (e.key === 'ArrowDown') {
        e.preventDefault();
        setActiveIndex((i) => Math.min(i + 1, filtered.length - 1));
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        setActiveIndex((i) => Math.max(i - 1, 0));
      } else if (e.key === 'Enter' && filtered[activeIndex]) {
        handleSelect(filtered[activeIndex]);
      }
    };

    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, filtered, activeIndex, onClose]);

  const handleSelect = (item: CommandPaletteItem) => {
    item.action?.();
    onSelect?.(item);
    onClose?.();
  };

  if (!isOpen) return null;

  return (
    <div
      className={`cn-command-palette cn-command-palette-open ${className}`.trim()}
      onClick={(e) => e.target === e.currentTarget && onClose?.()}
      role="dialog"
      aria-modal="true"
      aria-label="Command palette"
      {...props}
    >
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
          role="combobox"
          aria-autocomplete="list"
          aria-expanded={filtered.length > 0}
        />
        <div className="cn-command-palette-results" role="listbox">
          {filtered.length > 0 ? (
            filtered.map((item, idx) => (
              <div
                key={idx}
                className={`cn-command-item ${idx === activeIndex ? 'cn-command-item-active' : ''}`.trim()}
                onClick={() => handleSelect(item)}
                onMouseEnter={() => setActiveIndex(idx)}
                role="option"
                aria-selected={idx === activeIndex}
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
            ))
          ) : (
            <div className="cn-command-empty">No commands found</div>
          )}
        </div>
      </div>
    </div>
  );
};

CommandPalette.displayName = 'CommandPalette';

export default CommandPalette;
