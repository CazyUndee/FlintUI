import { forwardRef } from 'react';

const Table = forwardRef(function Table({ 
  columns = [], 
  data = [],
  sortable = false,
  onSort,
  className = '' 
}, ref) {
  const handleSort = (column) => {
    if (!sortable || !column.sortable) return;
    onSort?.(column.key);
  };

  return (
    <div className={`cn-table-wrapper ${sortable ? 'cn-table-sortable' : ''} ${className}`}>
      <table className="cn-table" ref={ref}>
        <thead>
          <tr>
            {columns.map((col, idx) => (
              <th 
                key={idx}
                onClick={() => handleSort(col)}
                data-sort={col.key}
              >
                {col.header}
                {col.sortable && ' ↕'}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map((row, idx) => (
            <tr key={idx}>
              {columns.map((col, colIdx) => (
                <td key={colIdx}>
                  {col.render ? col.render(row) : row[col.key]}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
});

export default Table;
