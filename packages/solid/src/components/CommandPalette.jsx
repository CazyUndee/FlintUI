import { mergeProps, createSignal, Show, For, createEffect, onCleanup } from 'solid-js';

export function CommandPalette(props) {
  const merged = mergeProps({
    open: false,
    items: [],
    onSelect: () => {},
    onClose: () => {},
    placeholder: 'Search commands...'
  }, props);

  const [query, setQuery] = createSignal('');
  const [selectedIndex, setSelectedIndex] = createSignal(0);

  createEffect(() => {
    if (merged.open) {
      setQuery('');
      setSelectedIndex(0);
    }
  });

  createEffect(() => {
    if (merged.open) {
      const handleKeyDown = (e) => {
        if (e.key === 'Escape') {
          merged.onClose();
        } else if (e.key === 'ArrowDown') {
          e.preventDefault();
          setSelectedIndex(Math.min(selectedIndex() + 1, filteredItems().length - 1));
        } else if (e.key === 'ArrowUp') {
          e.preventDefault();
          setSelectedIndex(Math.max(selectedIndex() - 1, 0));
        } else if (e.key === 'Enter' && filteredItems()[selectedIndex()]) {
          handleSelect(filteredItems()[selectedIndex()]);
        }
      };

      window.addEventListener('keydown', handleKeyDown);
      onCleanup(() => window.removeEventListener('keydown', handleKeyDown));
    }
  });

  const filteredItems = () => {
    const q = query().toLowerCase();
    if (!q) return merged.items;
    return merged.items.filter(item =>
      (item.label || item.title || '').toLowerCase().includes(q)
    );
  };

  const handleSelect = (item) => {
    merged.onSelect(item.value !== undefined ? item.value : item);
    merged.onClose();
  };

  return (
    <Show when={merged.open}>
      <div class="cn-command-palette-backdrop" onClick={merged.onClose}>
        <div class="cn-command-palette" onClick={(e) => e.stopPropagation()}>
          <input
            type="text"
            class="cn-command-palette-input"
            placeholder={merged.placeholder}
            value={query()}
            onInput={(e) => {
              setQuery(e.target.value);
              setSelectedIndex(0);
            }}
            autofocus
          />
          <div class="cn-command-palette-list">
            {filteredItems().length > 0 ? (
              <For each={filteredItems()}>{(item, index) => (
                <div
                  class={`cn-command-palette-item ${index() === selectedIndex() ? 'cn-command-palette-item-selected' : ''}`}
                  onClick={() => handleSelect(item)}
                >
                  <Show when={item.icon}>
                    <span class="cn-command-palette-item-icon">{item.icon}</span>
                  </Show>
                  <span class="cn-command-palette-item-label">{item.label || item.title}</span>
                  <Show when={item.shortcut}>
                    <span class="cn-command-palette-item-shortcut">{item.shortcut}</span>
                  </Show>
                </div>
              )}</For>
            ) : (
              <div class="cn-command-empty">No commands found</div>
            )}
          </div>
        </div>
      </div>
    </Show>
  );
}

export default CommandPalette;
