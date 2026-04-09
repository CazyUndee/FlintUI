<script>
import { createEventDispatcher } from 'svelte';

export let items = [];
export let allowMultiple = false;

const dispatch = createEventDispatcher();
let openItems = [];

function isOpen(index) {
  return openItems.includes(index);
}

function toggle(index) {
  if (allowMultiple) {
    if (isOpen(index)) {
      openItems = openItems.filter(i => i !== index);
    } else {
      openItems = [...openItems, index];
    }
  } else {
    openItems = isOpen(index) ? [] : [index];
  }
  dispatch('toggle', { index, open: isOpen(index), openItems });
}
</script>

<div class="cn-accordion">
  {#each items as item, index}
    <div class="cn-accordion-item" class:cn-accordion-open={isOpen(index)}>
      <div
        class="cn-accordion-header"
        on:click={() => toggle(index)}
        role="button"
        tabindex="0"
        aria-expanded={isOpen(index)}
      >
        <span class="cn-accordion-title">{item.title}</span>
        <span class="cn-accordion-icon">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="6 9 12 15 18 9"></polyline>
          </svg>
        </span>
      </div>
      <div class="cn-accordion-content">
        {item.content}
      </div>
    </div>
  {/each}
</div>

<style>
.cn-accordion {
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 10px;
  background: #111111;
}
.cn-accordion-item {
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}
.cn-accordion-item:last-child {
  border-bottom: none;
}
.cn-accordion-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px;
  cursor: pointer;
  transition: background 0.15s ease;
  color: #f0ede8;
}
.cn-accordion-header:hover {
  background: #111111;
}
.cn-accordion-title {
  font-weight: 500;
}
.cn-accordion-icon {
  transition: transform 0.15s ease;
  display: flex;
  align-items: center;
  color: rgba(240, 237, 232, 0.5);
}
.cn-accordion-item.cn-accordion-open .cn-accordion-icon {
  transform: rotate(180deg);
}
.cn-accordion-content {
  padding: 0 16px 16px;
  display: none;
  color: rgba(240, 237, 232, 0.5);
}
.cn-accordion-item.cn-accordion-open .cn-accordion-content {
  display: block;
}
</style>
