import { useState, useRef } from 'react';

export default function FileInput({ 
  onFileSelect,
  accept,
  multiple = false,
  label = 'Drag and drop files here, or click to browse',
  className = '' 
}) {
  const [fileName, setFileName] = useState('');
  const inputRef = useRef(null);

  const handleChange = (e) => {
    const files = Array.from(e.target.files);
    if (files.length > 0) {
      setFileName(files.map(f => f.name).join(', '));
      onFileSelect?.(multiple ? files : files[0]);
    }
  };

  return (
    <div className={`cn-file-input ${fileName ? 'cn-file-input-has-file' : ''} ${className}`}>
      <input
        ref={inputRef}
        type="file"
        accept={accept}
        multiple={multiple}
        onChange={handleChange}
      />
      <div className="cn-file-input-label">
        <div className="cn-file-input-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
            <polyline points="17 8 12 3 7 8"></polyline>
            <line x1="12" y1="3" x2="12" y2="15"></line>
          </svg>
        </div>
        <div className="cn-file-input-text">
          {fileName ? <span>{fileName}</span> : label}
        </div>
      </div>
    </div>
  );
}
