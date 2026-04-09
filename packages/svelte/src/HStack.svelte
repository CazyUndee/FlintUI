<script>
  export let spacing = '4';
</script>

<div class="cn-hstack cn-hstack-{spacing}">
  <slot />
</div>

<style>
  .cn-hstack {
    display: flex;
    flex-direction: row;
    align-items: center;
  }
  .cn-hstack-1 { gap: 0.25rem; }
  .cn-hstack-2 { gap: 0.5rem; }
  .cn-hstack-4 { gap: 1rem; }
  .cn-hstack-6 { gap: 1.5rem; }
</style>
