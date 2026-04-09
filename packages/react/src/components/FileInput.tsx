import * as React from 'react';

export interface FileInputProps {
  onFileSelect?: (file: File | File[]) => void;
  accept?: string;
  multiple?: boolean;
  label?: string;
  className?: string;
}

export const FileInput: React.FC<FileInputProps> = ({
  onFileSelect,
  accept,
  multiple = false,
  label = 'Drag and drop files here, or click to browse',
  className = '',
}) => {
  const [fileName, setFileName] = React.useState('');
  const [isDragging, setIsDragging] = React.useState(false);
  const inputRef = React.useRef<HTMLInputElement>(null);

  const processFiles = React.useCallback((files: File[]) => {
    if (files.length > 0) {
      setFileName(files.map(f => f.name).join(', '));
      onFileSelect?.(multiple ? files : files[0]);
    }
  }, [multiple, onFileSelect]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = Array.from(e.target.files || []);
    processFiles(files);
  };

  const handleDragOver = (e: React.DragEvent<HTMLLabelElement>) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(true);
  };

  const handleDragLeave = (e: React.DragEvent<HTMLLabelElement>) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
  };

  const handleDrop = (e: React.DragEvent<HTMLLabelElement>) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
    const files = Array.from(e.dataTransfer.files);
    processFiles(files);
  };

  return (
    <div className={`cn-file-input ${fileName ? 'cn-file-input-has-file' : ''} ${isDragging ? 'cn-file-input-dragging' : ''} ${className}`.trim()}>
      <label
        className="cn-file-input-label"
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
      >
        <input
          ref={inputRef}
          type="file"
          accept={accept}
          multiple={multiple}
          onChange={handleChange}
        />
        <div className="cn-file-input-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
            <polyline points="17 8 12 3 7 8" />
            <line x1="12" y1="3" x2="12" y2="15" />
          </svg>
        </div>
        <div className="cn-file-input-text">
          {fileName ? <span>{fileName}</span> : label}
        </div>
      </label>
    </div>
  );
};

FileInput.displayName = 'FileInput';

export default FileInput;
