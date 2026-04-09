<script>
  export let value = 0;
  export let max = 100;
  export let variant = 'default';
  export let size = 'md';
  export let showLabel = false;
  export let label = '';

  $: percentage = Math.min(100, Math.max(0, (value / max) * 100));
  $: displayLabel = label || `${Math.round(percentage)}%`;
</script>

<div class="cn-progress cn-progress-{size}" class:cn-progress-success={variant === 'success'} class:cn-progress-warning={variant === 'warning'} class:cn-progress-error={variant === 'error'}>
  {#if showLabel}
    <div class="cn-progress-label">
      <span>
        <slot name="label">{displayLabel}</slot>
      </span>
    </div>
  {/if}
  <div
    class="cn-progress-track"
    role="progressbar"
    aria-valuenow={Math.round(percentage)}
    aria-valuemin={0}
    aria-valuemax={100}
  >
    <div class="cn-progress-bar" style="width: {percentage}%"></div>
  </div>
</div>

<style>
  .cn-progress {
    width: 100%;
  }

  .cn-progress-track {
    height: 4px;
    background: #222222;
    border-radius: 9999px;
    overflow: hidden;
  }

  .cn-progress-bar {
    height: 100%;
    background: #6b2323;
    border-radius: 9999px;
    transition: width 0.25s ease;
  }

  .cn-progress-success .cn-progress-bar {
    background: #6bc47a;
  }

  .cn-progress-warning .cn-progress-bar {
    background: #c4a43a;
  }

  .cn-progress-error .cn-progress-bar {
    background: #c46b6b;
  }

  .cn-progress-lg .cn-progress-track {
    height: 8px;
  }

  .cn-progress-label {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    color: rgba(240, 237, 232, 0.5);
    margin-bottom: 4px;
  }
</style>
