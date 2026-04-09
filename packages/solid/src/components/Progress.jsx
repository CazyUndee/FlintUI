import { mergeProps, Show } from 'solid-js';

export function Progress(props) {
  const merged = mergeProps({
    value: 0,
    max: 100,
    variant: 'default',
    size: 'md',
    showLabel: false,
    label: ''
  }, props);

  const percentage = () => {
    return Math.min(Math.max((merged.value / merged.max) * 100, 0), 100);
  };

  const sizeClasses = {
    sm: 'cn-progress-sm',
    md: 'cn-progress-md',
    lg: 'cn-progress-lg'
  };

  return (
    <div>
      <Show when={merged.showLabel}>
        <div class="cn-progress-label">
          <span>{merged.label || `${Math.round(percentage())}%`}</span>
        </div>
      </Show>
      <div
        class={`cn-progress ${sizeClasses[merged.size] || 'cn-progress-md'} ${merged.variant !== 'default' ? `cn-progress-${merged.variant}` : ''}`.trim()}
        role="progressbar"
        aria-valuenow={Math.round(percentage())}
        aria-valuemin={0}
        aria-valuemax={100}
      >
        <div class="cn-progress-track">
          <div
            class={`cn-progress-bar cn-progress-${merged.variant}`}
            style={`width: ${percentage()}%`}
          />
        </div>
      </div>
    </div>
  );
}

export default Progress;
