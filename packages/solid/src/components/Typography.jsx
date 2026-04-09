import { mergeProps } from 'solid-js';

export function H1(props) {
  const merged = mergeProps({ class: '' }, props);
  return <h1 class={`cn-h1 ${merged.class}`.trim()} {...merged} />;
}

export function H2(props) {
  const merged = mergeProps({ class: '' }, props);
  return <h2 class={`cn-h2 ${merged.class}`.trim()} {...merged} />;
}

export function H3(props) {
  const merged = mergeProps({ class: '' }, props);
  return <h3 class={`cn-h3 ${merged.class}`.trim()} {...merged} />;
}

export function H4(props) {
  const merged = mergeProps({ class: '' }, props);
  return <h4 class={`cn-h4 ${merged.class}`.trim()} {...merged} />;
}

export function H5(props) {
  const merged = mergeProps({ class: '' }, props);
  return <h5 class={`cn-h5 ${merged.class}`.trim()} {...merged} />;
}

export function H6(props) {
  const merged = mergeProps({ class: '' }, props);
  return <h6 class={`cn-h6 ${merged.class}`.trim()} {...merged} />;
}

export function Text(props) {
  const merged = mergeProps({ class: '' }, props);
  const variantClass = merged.variant ? `cn-text-${merged.variant}` : '';
  const sizeClass = merged.size ? `cn-text-${merged.size}` : '';

  return (
    <p class={`cn-text-base ${variantClass} ${sizeClass} ${merged.class}`.trim()} {...merged} />
  );
}

export function Label(props) {
  const merged = mergeProps({ class: '' }, props);
  return <label class={`cn-label ${merged.class}`.trim()} {...merged} />;
}

export default H1;
