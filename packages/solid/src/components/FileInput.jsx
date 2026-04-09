import { mergeProps, createSignal, Show } from 'solid-js';

export function FileInput(props) {
  const merged = mergeProps({
    accept: '',
    multiple: false,
    label: 'Drag and drop files here, or click to browse',
    onFileSelect: () => {},
    class: ''
  }, props);

  const [fileName, setFileName] = createSignal('');
  const [isDragging, setIsDragging] = createSignal(false);

  const processFiles = (files) => {
    if (files.length > 0) {
      setFileName(files.map(f => f.name).join(', '));
      merged.onFileSelect(merged.multiple ? files : files[0]);
    }
  };

  const handleChange = (e) => {
    const files = Array.from(e.target.files || []);
    processFiles(files);
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(true);
  };

  const handleDragLeave = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
    const files = Array.from(e.dataTransfer.files);
    processFiles(files);
  };

  return (
    <div class={`cn-file-input ${fileName() ? 'cn-file-input-has-file' : ''} ${isDragging() ? 'cn-file-input-dragging' : ''} ${merged.class}`.trim()}>
      <label
        class="cn-file-input-label"
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
      >
        <input
          type="file"
          accept={merged.accept}
          multiple={merged.multiple}
          onChange={handleChange}
        />
        <div class="cn-file-input-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
            <polyline points="17 8 12 3 7 8" />
            <line x1="12" y1="3" x2="12" y2="15" />
          </svg>
        </div>
        <div class="cn-file-input-text">
          {fileName() ? <span>{fileName()}</span> : merged.label}
        </div>
      </label>
    </div>
  );
}

export default FileInput;
