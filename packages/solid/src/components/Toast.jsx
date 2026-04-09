import { mergeProps, createSignal, createEffect, onCleanup, Show } from 'solid-js';

export function Toast(props) {
  const merged = mergeProps({
    message: '',
    type: 'info',
    duration: 3000,
    onClose: () => {}
  }, props);

  const [isLeaving, setIsLeaving] = createSignal(false);

  createEffect(() => {
    if (merged.message && merged.duration > 0) {
      const timer = setTimeout(() => {
        handleRemove();
      }, merged.duration);

      onCleanup(() => clearTimeout(timer));
    }
  });

  const handleRemove = () => {
    setIsLeaving(true);
    setTimeout(() => merged.onClose(), 200);
  };

  const typeIcons = {
    info: 'ℹ',
    success: '✓',
    warning: '⚠',
    error: '✕'
  };

  return (
    <Show when={merged.message}>
      <div class={`cn-toast cn-toast-${merged.type} ${isLeaving() ? 'cn-toast-leaving' : ''}`.trim()}>
        <span class="cn-toast-icon">{typeIcons[merged.type]}</span>
        <span class="cn-toast-message">{merged.message}</span>
        <button class="cn-toast-close" onClick={handleRemove}>×</button>
      </div>
    </Show>
  );
}

export default Toast;
