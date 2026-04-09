import { mergeProps, createSignal, Show, For, createEffect, onCleanup } from 'solid-js';

export function Search(props) {
  const merged = mergeProps({
    placeholder: 'Search...',
    items: [],
    onSelect: () => {}
  }, props);

  const [query, setQuery] = createSignal('');
  const [isOpen, setIsOpen] = createSignal(false);
  let searchRef;

  const filteredItems = () => {
    const q = query().toLowerCase();
    if (!q) return [];
    return merged.items.filter(item => {
      const title = typeof item === 'string' ? item : (item.title || item.label);
      const subtitle = item.subtitle || '';
      return title.toLowerCase().includes(q) || subtitle.toLowerCase().includes(q);
    });
  };

  const handleSelect = (item) => {
    const label = typeof item === 'string' ? item : (item.title || item.label);
    setQuery(label);
    setIsOpen(false);
    merged.onSelect(item);
  };

  createEffect(() => {
    const handleClickOutside = (e) => {
      if (searchRef && !searchRef.contains(e.target)) {
        setIsOpen(false);
      }
    };

    document.addEventListener('click', handleClickOutside);
    return () => document.removeEventListener('click', handleClickOutside);
  });

  return (
    <div ref={searchRef} class={`cn-search ${isOpen() ? 'cn-search-open' : ''}`.trim()}>
      <svg class="cn-search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="11" cy="11" r="8" />
        <line x1="21" y1="21" x2="16.65" y2="16.65" />
      </svg>
      <input
        type="search"
        class="cn-input cn-search-input"
        placeholder={merged.placeholder}
        value={query()}
        onInput={(e) => {
          setQuery(e.target.value);
          setIsOpen(true);
        }}
        onFocus={() => setIsOpen(true)}
        role="combobox"
        aria-autocomplete="list"
        aria-expanded={isOpen()}
      />
      <Show when={isOpen()}>
        <div class="cn-search-results" role="listbox">
          {filteredItems().length > 0 ? (
            <For each={filteredItems()}>{(item) => (
              <div
                class="cn-search-result"
                onClick={() => handleSelect(item)}
                role="option"
              >
                <div class="cn-search-result-title">{typeof item === 'string' ? item : (item.title || item.label)}</div>
                <Show when={typeof item !== 'string' && item.subtitle}>
                  <div class="cn-search-result-subtitle">{item.subtitle}</div>
                </Show>
              </div>
            )}</For>
          ) : (
            <div class="cn-search-empty">No results found</div>
          )}
        </div>
      </Show>
    </div>
  );
}

export default Search;
