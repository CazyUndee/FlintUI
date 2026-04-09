import * as React from 'react';

export interface FormGroupProps extends React.HTMLAttributes<HTMLDivElement> {
  label?: React.ReactNode;
  error?: React.ReactNode;
  help?: React.ReactNode;
  required?: boolean;
}

export const FormGroup: React.FC<FormGroupProps> = ({
  children,
  label,
  error,
  help,
  required = false,
  className = '',
  ...props
}) => {
  return (
    <div className={`cn-form-group ${className}`.trim()} {...props}>
      {label && (
        <label className="cn-form-label">
          {label}
          {required && <span style={{ color: 'var(--cn-error-text)', marginLeft: 'var(--cn-space-1)' }}>*</span>}
        </label>
      )}
      {children}
      {error && <div className="cn-form-error">{error}</div>}
      {!error && help && <div className="cn-form-help">{help}</div>}
    </div>
  );
};

FormGroup.displayName = 'FormGroup';

export default FormGroup;
