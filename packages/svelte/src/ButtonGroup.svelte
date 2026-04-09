<script>
  export let orientation = 'horizontal';
</script>

<div class="cn-btn-group" role="group" {orientation}>
  <slot />
</div>

<style>
  .cn-btn-group {
    display: inline-flex;
    align-items: center;
    gap: 0;
  }
  .cn-btn-group :global(.cn-btn) {
    border-radius: 0;
  }
  .cn-btn-group :global(.cn-btn:first-child) {
    border-radius: 10px 0 0 10px;
  }
  .cn-btn-group :global(.cn-btn:last-child) {
    border-radius: 0 10px 10px 0;
  }
  .cn-btn-group :global(.cn-btn:not(:last-child)) {
    border-right: none;
  }
</style>
