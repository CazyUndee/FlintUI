<script>
  export let items = [];
  export let clickable = false;
</script>

<style>
  .cn-list {
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    overflow: hidden;
  }

  .cn-list-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 16px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    transition: background 0.15s ease;
  }

  .cn-list-item:last-child {
    border-bottom: none;
  }

  .cn-list-item:hover {
    background: #111111;
  }

  .cn-list-item-clickable {
    cursor: pointer;
  }

  .cn-list-item-icon {
    flex-shrink: 0;
  }

  .cn-list-item-content {
    flex: 1;
  }

  .cn-list-item-title {
    font-size: 13px;
    color: #f0ede8;
  }

  .cn-list-item-subtitle {
    font-size: 12px;
    color: rgba(240, 237, 232, 0.5);
  }
</style>

<div class="cn-list" role="list">
  {#each items as item}
    <div class="cn-list-item" class:cn-list-item-clickable={clickable} role="listitem">
      {#if item.icon}
        <div class="cn-list-item-icon">
          <svelte:component this={item.icon} />
        </div>
      {/if}
      <div class="cn-list-item-content">
        <div class="cn-list-item-title">{item.title}</div>
        {#if item.subtitle}
          <div class="cn-list-item-subtitle">{item.subtitle}</div>
        {/if}
      </div>
    </div>
  {/each}
</div>
