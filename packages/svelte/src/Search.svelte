<script>
import { createEventDispatcher } from 'svelte';

export let placeholder = 'Search...';
export let items = [];

const dispatch = createEventDispatcher();

let query = '';
let open = false;
let selectedIndex = -1;

$: filteredItems = items.filter(item =>
  item.title.toLowerCase().includes(query.toLowerCase()) ||
  (item.subtitle && item.subtitle.toLowerCase().includes(query.toLowerCase()))
);

function handleInput() {
  open = filteredItems.length > 0 && query.length > 0;
  selectedIndex = -1;
}

function handleFocus() {
  if (filteredItems.length > 0 && query.length > 0) {
    open = true;
  }
}

function handleBlur() {
  setTimeout(() => {
    open = false;
    selectedIndex = -1;
  }, 150);
}

function handleKeydown(event) {
  if (!open) return;

  if (event.key === 'ArrowDown') {
    event.preventDefault();
    selectedIndex = Math.min(selectedIndex + 1, filteredItems.length - 1);
  } else if (event.key === 'ArrowUp') {
    event.preventDefault();
    selectedIndex = Math.max(selectedIndex - 1, 0);
  } else if (event.key === 'Enter' && selectedIndex >= 0) {
    event.preventDefault();
    selectItem(filteredItems[selectedIndex]);
  } else if (event.key === 'Escape') {
    open = false;
    selectedIndex = -1;
  }
}

function selectItem(item) {
  dispatch('select', item);
  query = '';
  open = false;
  selectedIndex = -1;
}
</script>

<div class="cn-search" class:cn-search-open={open}>
  <svg class="cn-search-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="11" cy="11" r="8"/>
    <path d="m21 21-4.35-4.35"/>
  </svg>

  <input
    type="search"
    class="cn-search-input"
    {placeholder}
    bind:value={query}
    on:input={handleInput}
    on:focus={handleFocus}
    on:blur={handleBlur}
    on:keydown={handleKeydown}
  />

  {#if open && filteredItems.length > 0}
    <div class="cn-search-results">
      {#each filteredItems as item, i}
        <div
          class="cn-search-result"
          class:cn-search-result-selected={i === selectedIndex}
          on:click={() => selectItem(item)}
          on:keydown={() => {}}
          role="option"
          aria-selected={i === selectedIndex}
        >
          <div class="cn-search-result-title">{item.title}</div>
          {#if item.subtitle}
            <div class="cn-search-result-subtitle">{item.subtitle}</div>
          {/if}
        </div>
      {/each}
    </div>
  {:else if open && query.length > 0}
    <div class="cn-search-empty">No results found</div>
  {/if}
</div>

<style>
.cn-search {
  position: relative;
}

.cn-search-input {
  font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  font-size: 13px;
  background: #111111;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 10px;
  padding: 8px 12px;
  padding-left: 40px;
  padding-right: 40px;
  color: #f0ede8;
  outline: none;
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
  width: 100%;
}

.cn-search-input:hover {
  border-color: rgba(255, 255, 255, 0.15);
}

.cn-search-input:focus {
  border-color: #6b2323;
  box-shadow: 0 0 0 3px rgba(107, 35, 35, 0.3);
}

.cn-search-input::placeholder {
  color: rgba(240, 237, 232, 0.25);
}

.cn-search-icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: rgba(240, 237, 232, 0.5);
  pointer-events: none;
}

.cn-search-results {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  margin-top: 4px;
  background: #111111;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
  max-height: 300px;
  overflow-y: auto;
  z-index: 100;
}

.cn-search.cn-search-open .cn-search-results {
  display: block;
}

.cn-search-result {
  padding: 12px 16px;
  cursor: pointer;
  transition: background 0.15s ease;
}

.cn-search-result:hover,
.cn-search-result-selected {
  background: #1a1a1a;
}

.cn-search-result-title {
  font-size: 13px;
  color: #f0ede8;
}

.cn-search-result-subtitle {
  font-size: 12px;
  color: rgba(240, 237, 232, 0.5);
  margin-top: 2px;
}

.cn-search-empty {
  padding: 24px;
  text-align: center;
  color: rgba(240, 237, 232, 0.4);
  font-size: 13px;
  font-family: 'Outfit', sans-serif;
}
</style>
