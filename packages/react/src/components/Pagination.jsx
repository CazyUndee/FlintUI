import { useState } from 'react';

export default function Pagination({ 
  total, 
  current = 1, 
  onChange,
  className = '' 
}) {
  const [page, setPage] = useState(current);

  const activePage = onChange !== undefined ? current : page;

  const getPages = () => {
    const pages = [];
    const maxVisible = 5;

    if (total <= maxVisible) {
      for (let i = 1; i <= total; i++) pages.push(i);
    } else {
      if (activePage <= 3) {
        for (let i = 1; i <= 4; i++) pages.push(i);
        pages.push('...');
        pages.push(total);
      } else if (activePage >= total - 2) {
        pages.push(1);
        pages.push('...');
        for (let i = total - 3; i <= total; i++) pages.push(i);
      } else {
        pages.push(1);
        pages.push('...');
        for (let i = activePage - 1; i <= activePage + 1; i++) pages.push(i);
        pages.push('...');
        pages.push(total);
      }
    }

    return pages;
  };

  const goTo = (p) => {
    if (p < 1 || p > total || p === activePage) return;
    if (onChange) {
      onChange(p);
    } else {
      setPage(p);
    }
  };

  return (
    <div className={`cn-pagination ${className}`}>
      <button
        className="cn-pagination-item"
        onClick={() => goTo(activePage - 1)}
        disabled={activePage === 1}
      >
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" width="16" height="16">
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
      </button>
      {getPages().map((p, idx) => (
        <button
          key={idx}
          className={`cn-pagination-item ${p === activePage ? 'cn-pagination-active' : ''}`}
          onClick={() => typeof p === 'number' && goTo(p)}
          disabled={p === '...'}
        >
          {p}
        </button>
      ))}
      <button
        className="cn-pagination-item"
        onClick={() => goTo(activePage + 1)}
        disabled={activePage === total}
      >
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" width="16" height="16">
          <polyline points="9 18 15 12 9 6"></polyline>
        </svg>
      </button>
    </div>
  );
}
