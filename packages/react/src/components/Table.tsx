import * as React from 'react';

export interface TableColumn<T = Record<string, unknown>> {
  key: string;
  header: string;
  sortable?: boolean;
  render?: (row: T) => React.ReactNode;
}

export interface TableProps<T = Record<string, unknown>> extends React.HTMLAttributes<HTMLDivElement> {
  columns: TableColumn<T>[];
  data: T[];
  sortable?: boolean;
  onSort?: (key: string) => void;
}

export function Table<T extends Record<string, unknown> = Record<string, unknown>>({
  columns = [],
  data = [],
  sortable = false,
  onSort,
  className = '',
  ...props
}: TableProps<T>): React.ReactElement {
  const [sortState, setSortState] = React.useState<Record<string, 'none' | 'ascending' | 'descending'>>(
    Object.fromEntries(columns.map((col) => [col.key, 'none']))
  );

  const handleSort = (column: TableColumn<T>) => {
    if (!sortable || !column.sortable) return;

    const next: Record<string, 'none' | 'ascending' | 'descending'> = {};
    columns.forEach((col) => {
      next[col.key] = 'none';
    });

    const current = sortState[column.key] ?? 'none';
    if (current === 'none') {
      next[column.key] = 'ascending';
    } else if (current === 'ascending') {
      next[column.key] = 'descending';
    } else {
      next[column.key] = 'none';
    }

    setSortState(next);
    onSort?.(column.key);
  };

  return (
    <div className={`cn-table-wrapper ${sortable ? 'cn-table-sortable' : ''} ${className}`.trim()} {...props}>
      <table className="cn-table">
        <thead>
          <tr>
            {columns.map((col, idx) => {
              const sortDirection = sortState[col.key] ?? 'none';
              const sortIndicator = sortDirection === 'ascending' ? ' ↑' : sortDirection === 'descending' ? ' ↓' : col.sortable ? ' ↕' : '';
              return (
                <th
                  key={idx}
                  onClick={() => handleSort(col)}
                  data-sort={col.key}
                  aria-sort={col.sortable ? sortDirection : undefined}
                >
                  {col.header}
                  {sortIndicator}
                </th>
              );
            })}
          </tr>
        </thead>
        <tbody>
          {data.map((row, idx) => (
            <tr key={idx}>
              {columns.map((col, colIdx) => (
                <td key={colIdx}>
                  {col.render ? col.render(row) : (row as Record<string, unknown>)[col.key] as React.ReactNode}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

Table.displayName = 'Table';

export default Table;
