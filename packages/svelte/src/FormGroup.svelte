<script>
  export let label = '';
  export let error = '';
  export let help = '';
  export let required = false;
</script>

<div class="cn-form-group">
  {#if label}
    <label class="cn-form-label">
      <slot name="label">{label}</slot>
      {#if required}
        <span class="cn-form-required">*</span>
      {/if}
    </label>
  {/if}
  <slot />
  {#if error}
    <div class="cn-form-error">
      <slot name="error">{error}</slot>
    </div>
  {:else if help}
    <div class="cn-form-help">
      <slot name="help">{help}</slot>
    </div>
  {/if}
</div>

<style>
  .cn-form-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  .cn-form-label {
    font-size: 13px;
    font-weight: 500;
    color: #f0ede8;
  }
  .cn-form-required {
    color: #b82020;
    margin-left: 4px;
  }
  .cn-form-error {
    font-size: 12px;
    color: #b82020;
  }
  .cn-form-help {
    font-size: 12px;
    color: rgba(240, 237, 232, 0.5);
  }
</style>
