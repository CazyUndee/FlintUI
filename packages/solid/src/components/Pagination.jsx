import { mergeProps, For, Show } from 'solid-js';

export function Pagination(props) {
  const merged = mergeProps({
    total: 1,
    current: 1,
    onChange: () => {}
  }, props);

  const totalPages = () => Math.max(1, merged.total);

  const handlePageClick = (page) => {
    if (page >= 1 && page <= totalPages() && page !== merged.current) {
      merged.onChange(page);
    }
  };

  const visiblePages = () => {
    const pages = [];
    const total = totalPages();
    const current = merged.current;

    let start = Math.max(1, current - 2);
    let end = Math.min(total, current + 2);

    if (start > 1) pages.push(1);
    if (start > 2) pages.push('...');

    for (let i = start; i <= end; i++) {
      pages.push(i);
    }

    if (end < total - 1) pages.push('...');
    if (end < total) pages.push(total);

    return pages;
  };

  return (
    <nav class="cn-pagination" aria-label="Pagination">
      <button
        class="cn-pagination-btn cn-pagination-prev"
        disabled={merged.current === 1}
        onClick={() => handlePageClick(merged.current - 1)}
        aria-label="Previous page"
      >
        ←
      </button>
      <For each={visiblePages()}>{(page) => (
        <Show when={page === '...'} fallback={
          <button
            class={`cn-pagination-btn ${page === merged.current ? 'cn-pagination-active' : ''}`}
            onClick={() => handlePageClick(page)}
            aria-current={page === merged.current ? 'page' : undefined}
          >
            {page}
          </button>
        }>
          <button
            class="cn-pagination-btn cn-pagination-ellipsis"
            disabled
            aria-label="More pages"
            aria-hidden="true"
            tabIndex={-1}
          >
            ...
          </button>
        </Show>
      )}</For>
      <button
        class="cn-pagination-btn cn-pagination-next"
        disabled={merged.current === totalPages()}
        onClick={() => handlePageClick(merged.current + 1)}
        aria-label="Next page"
      >
        →
      </button>
    </nav>
  );
}

export default Pagination;
