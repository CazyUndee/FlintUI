import * as React from 'react';
import '../styles.css';

export type ButtonVariant = 'primary' | 'ghost' | 'outline' | 'danger' | 'success' | 'default';
export type ButtonSize = 'sm' | 'md' | 'lg';

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant;
  size?: ButtonSize;
  icon?: boolean;
}

export interface ButtonGroupProps extends React.HTMLAttributes<HTMLDivElement> {}

export const Button: React.FC<ButtonProps> & {
  Group: React.FC<ButtonGroupProps>;
} = Object.assign(
  React.forwardRef<HTMLButtonElement, ButtonProps>(
    ({ children, variant = 'default', size = 'md', icon = false, disabled = false, className = '', ...props }, ref) => {
      const variantClass = variant !== 'default' ? `cn-btn-${variant}` : '';
      const sizeClass = size !== 'md' ? `cn-btn-${size}` : '';
      const iconClass = icon ? 'cn-btn-icon' : '';

      return (
        <button
          ref={ref}
          className={`cn-btn ${variantClass} ${sizeClass} ${iconClass} ${className}`.trim()}
          disabled={disabled}
          {...props}
        >
          {children}
        </button>
      );
    }
  ),
  {
    Group: ({ children, className = '', ...props }: ButtonGroupProps) => (
      <div className={`cn-btn-group ${className}`.trim()} {...props}>
        {children}
      </div>
    ),
  }
);

Button.displayName = 'Button';
Button.Group.displayName = 'Button.Group';

export default Button;
