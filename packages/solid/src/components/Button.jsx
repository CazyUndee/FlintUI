import { mergeProps } from 'solid-js';

function ButtonGroup(props) {
  const merged = mergeProps({ class: '' }, props);
  return (
    <div class={`cn-btn-group ${merged.class}`.trim()} {...merged}>
      {merged.children}
    </div>
  );
}

export function Button(props) {
  const merged = mergeProps({ variant: 'default', size: 'md', icon: false, class: '' }, props);

  const getClass = () => {
    const classes = ['cn-btn'];
    if (merged.variant !== 'default') classes.push(`cn-btn-${merged.variant}`);
    if (merged.size !== 'md') classes.push(`cn-btn-${merged.size}`);
    if (merged.icon) classes.push('cn-btn-icon');
    if (merged.class) classes.push(merged.class);
    return classes.join(' ');
  };

  return (
    <button
      type="button"
      class={getClass()}
      disabled={merged.disabled}
      {...merged}
    >
      {merged.children}
    </button>
  );
}

Button.Group = ButtonGroup;

export default Button;
