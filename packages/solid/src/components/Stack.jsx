import { mergeProps } from 'solid-js';

export function Stack(props) {
  const merged = mergeProps({ spacing: '4', class: '' }, props);
  return (
    <div class={`cn-stack cn-stack-${merged.spacing} ${merged.class}`.trim()} {...merged}>
      {merged.children}
    </div>
  );
}

export function HStack(props) {
  const merged = mergeProps({ spacing: '4', class: '' }, props);
  return (
    <div class={`cn-hstack cn-hstack-${merged.spacing} ${merged.class}`.trim()} {...merged}>
      {merged.children}
    </div>
  );
}

export function Divider(props) {
  const merged = mergeProps({ orientation: 'horizontal', class: '' }, props);

  const dividerStyle = merged.orientation === 'vertical'
    ? 'width: 1px; height: auto; min-height: 100%; border-right: none; border-bottom: 1px solid var(--cn-border);'
    : 'height: 1px; border: none; background-color: var(--cn-border);';

  return (
    <hr
      class={`cn-divider ${merged.class}`.trim()}
      style={dividerStyle}
      role="separator"
      {...merged}
    />
  );
}

export default Stack;
