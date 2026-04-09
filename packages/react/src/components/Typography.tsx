import * as React from 'react';

export interface HeadingProps extends React.HTMLAttributes<HTMLHeadingElement> {
  level?: 1 | 2 | 3 | 4 | 5 | 6;
}

export const H1: React.FC<React.HTMLAttributes<HTMLHeadingElement>> = ({ className = '', ...props }) => (
  <h1 className={`cn-h1 ${className}`.trim()} {...props} />
);
H1.displayName = 'H1';

export const H2: React.FC<React.HTMLAttributes<HTMLHeadingElement>> = ({ className = '', ...props }) => (
  <h2 className={`cn-h2 ${className}`.trim()} {...props} />
);
H2.displayName = 'H2';

export const H3: React.FC<React.HTMLAttributes<HTMLHeadingElement>> = ({ className = '', ...props }) => (
  <h3 className={`cn-h3 ${className}`.trim()} {...props} />
);
H3.displayName = 'H3';

export const H4: React.FC<React.HTMLAttributes<HTMLHeadingElement>> = ({ className = '', ...props }) => (
  <h4 className={`cn-h4 ${className}`.trim()} {...props} />
);
H4.displayName = 'H4';

export const H5: React.FC<React.HTMLAttributes<HTMLHeadingElement>> = ({ className = '', ...props }) => (
  <h5 className={`cn-h5 ${className}`.trim()} {...props} />
);
H5.displayName = 'H5';

export const H6: React.FC<React.HTMLAttributes<HTMLHeadingElement>> = ({ className = '', ...props }) => (
  <h6 className={`cn-h6 ${className}`.trim()} {...props} />
);
H6.displayName = 'H6';

export interface TextProps extends React.HTMLAttributes<HTMLParagraphElement> {
  variant?: 'muted' | 'dim' | 'accent' | 'mono';
  size?: 'xs' | 'sm' | 'base' | 'md' | 'lg' | 'xl';
}

export const Text: React.FC<TextProps> = ({
  variant,
  size,
  className = '',
  ...props
}) => {
  const variantClass = variant ? `cn-text-${variant}` : '';
  const sizeClass = size ? `cn-text-${size}` : '';

  return (
    <p className={`cn-text-base ${variantClass} ${sizeClass} ${className}`.trim()} {...props} />
  );
};

Text.displayName = 'Text';

export interface LabelProps extends React.LabelHTMLAttributes<HTMLLabelElement> {}

export const Label: React.FC<LabelProps> = ({ className = '', ...props }) => (
  <label className={`cn-label ${className}`.trim()} {...props} />
);

Label.displayName = 'Label';

export default H1;
