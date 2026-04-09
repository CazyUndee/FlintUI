import * as React from 'react';

export interface PaginationProps extends Omit<React.HTMLAttributes<HTMLDivElement>, 'onChange'> {
  total: number;
  current?: number;
  onChange?: (page: number) => void;
}

export const Pagination: React.FC<PaginationProps> = ({
  total,
  current = 1,
  onChange,
  className = '',
  ...props
}) => {
  const [page, setPage] = React.useState(current);

  const activePage = onChange !== undefined ? current : page;

  const getPages = (): (number | string)[] => {
    const pages: (number | string)[] = [];
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

  const goTo = (p: number) => {
    if (p < 1 || p > total || p === activePage) return;
    if (onChange) {
      onChange(p);
    } else {
      setPage(p);
    }
  };

  return (
    <nav className={`cn-pagination ${className}`.trim()} aria-label="Pagination" {...props}>
      <button
        className="cn-pagination-item"
        onClick={() => goTo(activePage - 1)}
        disabled={activePage === 1}
        aria-label="Previous page"
      >
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" width="16" height="16">
          <polyline points="15 18 9 12 15 6" />
        </svg>
      </button>
      {getPages().map((p, idx) =>
        p === '...' ? (
          <button
            key={idx}
            className="cn-pagination-item cn-pagination-ellipsis"
            disabled
            aria-label="More pages"
            aria-hidden="true"
            tabIndex={-1}
          >
            {p}
          </button>
        ) : (
          <button
            key={idx}
            className={`cn-pagination-item ${p === activePage ? 'cn-pagination-active' : ''}`.trim()}
            onClick={() => goTo(p)}
            aria-current={p === activePage ? 'page' : undefined}
          >
            {p}
          </button>
        )
      )}
      <button
        className="cn-pagination-item"
        onClick={() => goTo(activePage + 1)}
        disabled={activePage === total}
        aria-label="Next page"
      >
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" width="16" height="16">
          <polyline points="9 18 15 12 9 6" />
        </svg>
      </button>
    </nav>
  );
};

Pagination.displayName = 'Pagination';

export default Pagination;
