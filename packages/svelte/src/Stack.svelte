<script>
  export let spacing = '4';
</script>

<div class="cn-stack cn-stack-{spacing}">
  <slot />
</div>

<style>
  .cn-stack {
    display: flex;
    flex-direction: column;
  }
  .cn-stack-1 { gap: 0.25rem; }
  .cn-stack-2 { gap: 0.5rem; }
  .cn-stack-4 { gap: 1rem; }
  .cn-stack-6 { gap: 1.5rem; }
</style>
