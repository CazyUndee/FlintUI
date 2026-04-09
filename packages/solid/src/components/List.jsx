import { mergeProps, For, Show } from 'solid-js';

export function ListItem(props) {
  const merged = mergeProps({ clickable: false, class: '' }, props);
  return (
    <div
      class={`cn-list-item ${merged.clickable ? 'cn-list-item-clickable' : ''} ${merged.class}`.trim()}
      onClick={merged.onClick}
      role={merged.clickable ? 'button' : 'listitem'}
      tabIndex={merged.clickable ? 0 : undefined}
      {...merged}
    >
      <Show when={merged.icon}>
        <div class="cn-list-item-icon">{merged.icon}</div>
      </Show>
      <Show when={merged.title || merged.subtitle || merged.children}>
        <div class="cn-list-item-content">
          <Show when={merged.title}>
            <div class="cn-list-item-title">{merged.title}</div>
          </Show>
          <Show when={merged.subtitle}>
            <div class="cn-list-item-subtitle">{merged.subtitle}</div>
          </Show>
          {merged.children}
        </div>
      </Show>
      <Show when={merged.actions}>
        <div class="cn-list-item-actions">{merged.actions}</div>
      </Show>
    </div>
  );
}

export function List(props) {
  const merged = mergeProps({ class: '' }, props);
  return (
    <div class={`cn-list ${merged.class}`.trim()} role="list" {...merged}>
      {merged.children}
    </div>
  );
}

List.Item = ListItem;

export default List;
