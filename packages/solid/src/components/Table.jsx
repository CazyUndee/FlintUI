import { mergeProps, createSignal, For, Show } from 'solid-js';

export function Table(props) {
  const merged = mergeProps({
    headers: [],
    rows: [],
    sortable: false
  }, props);

  const [sortColumn, setSortColumn] = createSignal(null);
  const [sortDirection, setSortDirection] = createSignal('asc');

  const handleSort = (index) => {
    if (!merged.sortable) return;

    if (sortColumn() === index) {
      setSortDirection(sortDirection() === 'asc' ? 'desc' : 'asc');
    } else {
      setSortColumn(index);
      setSortDirection('asc');
    }
  };

  const getAriaSort = (index) => {
    if (!merged.sortable || sortColumn() !== index) return undefined;
    return sortDirection() === 'asc' ? 'ascending' : 'descending';
  };

  const sortedRows = () => {
    if (!merged.sortable || sortColumn() === null) return merged.rows;

    return [...merged.rows].sort((a, b) => {
      const aVal = a[sortColumn()];
      const bVal = b[sortColumn()];

      if (aVal < bVal) return sortDirection() === 'asc' ? -1 : 1;
      if (aVal > bVal) return sortDirection() === 'asc' ? 1 : -1;
      return 0;
    });
  };

  return (
    <div class={`cn-table-wrapper ${merged.sortable ? 'cn-table-sortable' : ''}`.trim()}>
      <table class="cn-table">
        <thead>
          <tr>
            <For each={merged.headers}>{(header, index) => (
              <th
                class={`cn-table-header ${merged.sortable ? 'cn-table-header-sortable' : ''}`}
                onClick={() => handleSort(index())}
                aria-sort={getAriaSort(index())}
              >
                {header}
                <Show when={merged.sortable && sortColumn() === index()}>
                  <span class="cn-table-sort-icon">{sortDirection() === 'asc' ? '▲' : '▼'}</span>
                </Show>
              </th>
            )}</For>
          </tr>
        </thead>
        <tbody>
          <For each={sortedRows()}>{(row) => (
            <tr class="cn-table-row">
              <For each={row}>{(cell) => (
                <td class="cn-table-cell">{cell}</td>
              )}</For>
            </tr>
          )}</For>
        </tbody>
      </table>
    </div>
  );
}

export default Table;
