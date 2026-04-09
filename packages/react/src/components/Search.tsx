import * as React from 'react';

export interface SearchItem {
  title: string;
  subtitle?: string;
}

export interface SearchProps extends Omit<React.HTMLAttributes<HTMLDivElement>, 'onSelect'> {
  items?: SearchItem[];
  placeholder?: string;
  onSelect?: (item: SearchItem) => void;
}

export const Search: React.FC<SearchProps> = ({
  items = [],
  placeholder = 'Search...',
  onSelect,
  className = '',
  ...props
}) => {
  const [query, setQuery] = React.useState('');
  const [isOpen, setIsOpen] = React.useState(false);
  const ref = React.useRef<HTMLDivElement>(null);

  const filtered = items.filter(
    (item) =>
      item.title.toLowerCase().includes(query.toLowerCase()) ||
      (item.subtitle && item.subtitle.toLowerCase().includes(query.toLowerCase()))
  );

  React.useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (ref.current && !ref.current.contains(e.target as Node)) {
        setIsOpen(false);
      }
    };

    document.addEventListener('click', handleClickOutside);
    return () => document.removeEventListener('click', handleClickOutside);
  }, []);

  const handleSelect = (item: SearchItem) => {
    setQuery(item.title);
    setIsOpen(false);
    onSelect?.(item);
  };

  return (
    <div ref={ref} className={`cn-search ${isOpen ? 'cn-search-open' : ''} ${className}`.trim()} {...props}>
      <svg className="cn-search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <circle cx="11" cy="11" r="8" />
        <line x1="21" y1="21" x2="16.65" y2="16.65" />
      </svg>
      <input
        type="search"
        className="cn-input cn-search-input"
        placeholder={placeholder}
        value={query}
        onChange={(e) => {
          setQuery(e.target.value);
          setIsOpen(true);
        }}
        onFocus={() => setIsOpen(true)}
        role="combobox"
        aria-autocomplete="list"
        aria-expanded={isOpen}
      />
      {isOpen && (
        <div className="cn-search-results" role="listbox">
          {filtered.length > 0 ? (
            filtered.map((item, idx) => (
              <div
                key={idx}
                className="cn-search-result"
                onClick={() => handleSelect(item)}
                role="option"
              >
                <div className="cn-search-result-title">{item.title}</div>
                {item.subtitle && (
                  <div className="cn-search-result-subtitle">{item.subtitle}</div>
                )}
              </div>
            ))
          ) : (
            <div className="cn-search-empty">No results found</div>
          )}
        </div>
      )}
    </div>
  );
};

Search.displayName = 'Search';

export default Search;
