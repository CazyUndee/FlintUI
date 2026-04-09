import { mergeProps, For, Show } from 'solid-js';

function SidebarItem(props) {
  const merged = mergeProps({ active: false, class: '' }, props);

  const content = (
    <>
      <Show when={merged.icon}>
        <span class="cn-sidebar-item-icon">{merged.icon}</span>
      </Show>
      {merged.children}
    </>
  );

  if (merged.href) {
    return (
      <a
        href={merged.href}
        class={`cn-sidebar-item ${merged.active ? 'cn-sidebar-active' : ''} ${merged.class}`.trim()}
        role="menuitem"
        {...merged}
      >
        {content}
      </a>
    );
  }

  return (
    <div
      class={`cn-sidebar-item ${merged.active ? 'cn-sidebar-active' : ''} ${merged.class}`.trim()}
      role="menuitem"
      {...merged}
    >
      {content}
    </div>
  );
}

export function Sidebar(props) {
  const merged = mergeProps({ class: '' }, props);

  return (
    <aside class={`cn-sidebar ${merged.class}`.trim()} {...merged}>
      <Show when={merged.header}>
        <div class="cn-sidebar-header">{merged.header}</div>
      </Show>
      <div class="cn-sidebar-nav">
        {merged.children}
      </div>
      <Show when={merged.footer}>
        <div class="cn-sidebar-footer">{merged.footer}</div>
      </Show>
    </aside>
  );
}

Sidebar.Item = SidebarItem;

export default Sidebar;
