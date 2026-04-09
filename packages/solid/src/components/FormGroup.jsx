import { mergeProps, Show } from 'solid-js';

export function FormGroup(props) {
  const merged = mergeProps({
    required: false,
    class: ''
  }, props);

  return (
    <div class={`cn-form-group ${merged.class}`.trim()} {...merged}>
      <Show when={merged.label}>
        <label class="cn-form-label">
          {merged.label}
          <Show when={merged.required}>
            <span style={{ color: 'var(--cn-error-text)', 'margin-left': 'var(--cn-space-1)' }}>*</span>
          </Show>
        </label>
      </Show>
      {merged.children}
      <Show when={merged.error}>
        <div class="cn-form-error">{merged.error}</div>
      </Show>
      <Show when={!merged.error && merged.help}>
        <div class="cn-form-help">{merged.help}</div>
      </Show>
    </div>
  );
}

export default FormGroup;
