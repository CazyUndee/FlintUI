<script>
  export let title = '';
  export let subtitle = '';
  export let clickable = false;
</script>

<div class="cn-card" class:cn-card-clickable={clickable}>
  {#if $$slots.icon || $$slots.title || title || $$slots.subtitle || subtitle}
    <div class="cn-card-header">
      {#if $$slots.icon}
        <div class="cn-card-icon">
          <slot name="icon" />
        </div>
      {/if}
      <div class="cn-card-header-content">
        {#if $$slots.title}
          <slot name="title" />
        {:else if title}
          <h3 class="cn-card-title">{title}</h3>
        {/if}
        {#if $$slots.subtitle}
          <slot name="subtitle" />
        {:else if subtitle}
          <p class="cn-card-subtitle">{subtitle}</p>
        {/if}
      </div>
    </div>
  {/if}
  <div class="cn-card-body">
    <slot />
  </div>
  {#if $$slots.footer}
    <div class="cn-card-footer">
      <slot name="footer" />
    </div>
  {/if}
</div>

<style>
  .cn-card {
    background: #111111;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 20px;
    transition: border-color 0.15s ease;
  }
  .cn-card:hover { border-color: rgba(255, 255, 255, 0.15); }
  .cn-card-clickable { cursor: pointer; }
  .cn-card-clickable:hover { background: #1a1a1a; }
  .cn-card-header { display: flex; align-items: center; gap: 12px; margin-bottom: 16px; }
  .cn-card-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    width: 40px;
    height: 40px;
    border-radius: 10px;
    background: rgba(107, 35, 35, 0.15);
    color: #c97a7a;
  }
  .cn-card-header-content { flex: 1; }
  .cn-card-title { font-size: 14px; font-weight: 500; color: #f0ede8; }
  .cn-card-subtitle { font-size: 12px; color: rgba(240, 237, 232, 0.5); margin-top: 4px; }
  .cn-card-body { color: rgba(240, 237, 232, 0.5); }
  .cn-card-footer { margin-top: 16px; padding-top: 16px; border-top: 1px solid rgba(255, 255, 255, 0.08); }
</style>
