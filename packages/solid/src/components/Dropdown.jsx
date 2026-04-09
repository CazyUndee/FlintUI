import { mergeProps, createSignal, Show, createEffect, onCleanup } from 'solid-js';

function DropdownItem(props) {
  const merged = mergeProps({ class: '' }, props);
  return (
    <div
      class={`cn-dropdown-item ${merged.class}`.trim()}
      onClick={merged.onClick}
      role="menuitem"
      tabIndex={0}
      {...merged}
    >
      {merged.icon && <span class="cn-dropdown-item-icon">{merged.icon}</span>}
      {merged.children}
    </div>
  );
}

function DropdownDivider() {
  return <div class="cn-dropdown-divider" role="separator" />;
}

export function Dropdown(props) {
  const merged = mergeProps({ class: '' }, props);
  const [isOpen, setIsOpen] = createSignal(false);
  let dropdownRef;

  const toggle = () => setIsOpen((prev) => !prev);
  const close = () => setIsOpen(false);

  createEffect(() => {
    const handleClickOutside = (e) => {
      if (dropdownRef && !dropdownRef.contains(e.target)) {
        close();
      }
    };

    if (isOpen()) {
      document.addEventListener('click', handleClickOutside);
    }

    return () => {
      document.removeEventListener('click', handleClickOutside);
    };
  });

  return (
    <div
      ref={dropdownRef}
      class={`cn-dropdown ${isOpen() ? 'cn-dropdown-open' : ''} ${merged.class}`.trim()}
      {...merged}
    >
      <div
        class="cn-dropdown-trigger"
        onClick={toggle}
        role="button"
        aria-haspopup="true"
        aria-expanded={isOpen()}
        tabIndex={0}
        onKeyDown={(e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            toggle();
          }
        }}
      >
        {merged.trigger}
      </div>
      <Show when={isOpen()}>
        <div class="cn-dropdown-menu" role="menu" onClick={close}>
          {merged.children}
        </div>
      </Show>
    </div>
  );
}

Dropdown.Item = DropdownItem;
Dropdown.Divider = DropdownDivider;

export default Dropdown;
