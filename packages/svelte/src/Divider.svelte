<script>
  export let orientation = 'horizontal';
</script>

{#if orientation === 'vertical'}
  <div class="cn-divider cn-divider-vertical" role="separator"></div>
{:else}
  <hr class="cn-divider" role="separator" />
{/if}

<style>
  .cn-divider {
    height: 1px;
    border: none;
    background: rgba(255, 255, 255, 0.08);
    margin: 16px 0;
  }
  .cn-divider-vertical {
    width: 1px;
    height: auto;
    min-height: 100%;
    background: rgba(255, 255, 255, 0.08);
    margin: 0 16px;
    border: none;
  }
</style>
