import { mergeProps, createSignal, For, Show } from 'solid-js';

export function Accordion(props) {
  const merged = mergeProps({
    items: [],
    allowMultiple: false
  }, props);

  const [openIndices, setOpenIndices] = createSignal([]);

  const toggleItem = (index) => {
    const current = openIndices();
    if (merged.allowMultiple) {
      if (current.includes(index)) {
        setOpenIndices(current.filter(i => i !== index));
      } else {
        setOpenIndices([...current, index]);
      }
    } else {
      if (current.includes(index)) {
        setOpenIndices([]);
      } else {
        setOpenIndices([index]);
      }
    }
  };

  const isOpen = (index) => openIndices().includes(index);

  return (
    <div class="cn-accordion">
      <For each={merged.items}>{(item, index) => (
        <div class={`cn-accordion-item ${isOpen(index()) ? 'cn-accordion-open' : ''}`}>
          <button
            type="button"
            class="cn-accordion-header"
            onClick={() => toggleItem(index())}
            aria-expanded={isOpen(index())}
          >
            <span class="cn-accordion-title">{item.title}</span>
            <span class="cn-accordion-icon">{isOpen(index()) ? '−' : '+'}</span>
          </button>
          <Show when={isOpen(index())}>
            <div class="cn-accordion-content">{item.content}</div>
          </Show>
        </div>
      )}</For>
    </div>
  );
}

export default Accordion;
