import { useState, useEffect, useRef } from 'react';

export default function Search({ 
  items = [],
  placeholder = 'Search...',
  onSelect,
  className = '' 
}) {
  const [query, setQuery] = useState('');
  const [isOpen, setIsOpen] = useState(false);
  const ref = useRef(null);

  const filtered = items.filter(item =>
    item.title.toLowerCase().includes(query.toLowerCase()) ||
    (item.subtitle && item.subtitle.toLowerCase().includes(query.toLowerCase()))
  );

  useEffect(() => {
    const handleClickOutside = (e) => {
      if (ref.current && !ref.current.contains(e.target)) {
        setIsOpen(false);
      }
    };

    document.addEventListener('click', handleClickOutside);
    return () => document.removeEventListener('click', handleClickOutside);
  }, []);

  const handleSelect = (item) => {
    setQuery(item.title);
    setIsOpen(false);
    onSelect?.(item);
  };

  return (
    <div ref={ref} className={`cn-search ${isOpen ? 'cn-search-open' : ''} ${className}`}>
      <svg className="cn-search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <circle cx="11" cy="11" r="8"></circle>
        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
      </svg>
      <input
        type="text"
        className="cn-input cn-search-input"
        placeholder={placeholder}
        value={query}
        onChange={(e) => {
          setQuery(e.target.value);
          setIsOpen(true);
        }}
        onFocus={() => setIsOpen(true)}
      />
      {isOpen && filtered.length > 0 && (
        <div className="cn-search-results">
          {filtered.map((item, idx) => (
            <div
              key={idx}
              className="cn-search-result"
              onClick={() => handleSelect(item)}
            >
              <div className="cn-search-result-title">{item.title}</div>
              {item.subtitle && (
                <div className="cn-search-result-subtitle">{item.subtitle}</div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
