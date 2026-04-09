<script>
  export let variant = '';
  export let size = 'base';
</script>

<p class="cn-text cn-text-{size}" class:cn-text-muted={variant === 'muted'} class:cn-text-dim={variant === 'dim'} class:cn-text-accent={variant === 'accent'} class:cn-text-mono={variant === 'mono'}>
  <slot />
</p>

<style>
  .cn-text {
    font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    color: #f0ede8;
    margin: 0;
    line-height: 1.6;
  }
  .cn-text-xs { font-size: 0.75rem; }
  .cn-text-sm { font-size: 0.875rem; }
  .cn-text-base { font-size: 1rem; }
  .cn-text-md { font-size: 1.125rem; }
  .cn-text-lg { font-size: 1.25rem; }
  .cn-text-xl { font-size: 1.5rem; }
  .cn-text-muted { color: #a0a0a0; }
  .cn-text-dim { color: #666666; }
  .cn-text-accent { color: #c97a7a; }
  .cn-text-mono {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.875em;
  }
</style>
