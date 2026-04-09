<script>
  export let headers = [];
  export let rows = [];
  export let sortable = false;

  let sortColumn = -1;
  let sortDirection = 'asc';
  let sortedRows = [...rows];

  $: {
    if (sortColumn >= 0 && sortable) {
      sortedRows = [...rows].sort((a, b) => {
        const aVal = a[sortColumn];
        const bVal = b[sortColumn];
        if (aVal < bVal) return sortDirection === 'asc' ? -1 : 1;
        if (aVal > bVal) return sortDirection === 'asc' ? 1 : -1;
        return 0;
      });
    } else {
      sortedRows = [...rows];
    }
  }

  function handleSort(index) {
    if (!sortable) return;
    if (sortColumn === index) {
      sortDirection = sortDirection === 'asc' ? 'desc' : 'asc';
    } else {
      sortColumn = index;
      sortDirection = 'asc';
    }
  }

  function getAriaSort(index) {
    if (!sortable || sortColumn !== index) return undefined;
    return sortDirection === 'asc' ? 'ascending' : 'descending';
  }
</script>

<style>
  .cn-table-wrapper {
    overflow-x: auto;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px;
  }

  .cn-table {
    width: 100%;
    border-collapse: collapse;
  }

  .cn-table th,
  .cn-table td {
    padding: 12px 16px;
    text-align: left;
  }

  .cn-table th {
    background: #111111;
    font-size: 11px;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: rgba(240,237,232,0.5);
    border-bottom: 1px solid rgba(255,255,255,0.08);
  }

  .cn-table th.sortable {
    cursor: pointer;
    user-select: none;
  }

  .cn-table th.sortable:hover {
    color: rgba(240,237,232,0.8);
  }

  .cn-table td {
    border-bottom: 1px solid rgba(255,255,255,0.08);
    font-size: 13px;
    color: #f0ede8;
  }

  .cn-table tbody tr:last-child td {
    border-bottom: none;
  }

  .cn-table tbody tr:hover {
    background: #111111;
  }

  .sort-indicator {
    margin-left: 4px;
    opacity: 0.5;
  }

  .sort-indicator.active {
    opacity: 1;
  }
</style>

<div class="cn-table-wrapper">
  <table class="cn-table">
    <thead>
      <tr>
        {#each headers as header, index}
          <th
            class={sortable ? 'sortable' : ''}
            on:click={() => handleSort(index)}
            aria-sort={getAriaSort(index)}
          >
            {header}
            {#if sortable && sortColumn === index}
              <span class="sort-indicator active">
                {sortDirection === 'asc' ? '↑' : '↓'}
              </span>
            {:else if sortable}
              <span class="sort-indicator">↑</span>
            {/if}
          </th>
        {/each}
      </tr>
    </thead>
    <tbody>
      {#each sortedRows as row}
        <tr>
          {#each row as cell}
            <td>{cell}</td>
          {/each}
        </tr>
      {/each}
    </tbody>
  </table>
</div>
