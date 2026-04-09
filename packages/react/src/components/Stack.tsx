import * as React from 'react';

export interface StackProps extends React.HTMLAttributes<HTMLDivElement> {
  spacing?: '1' | '2' | '4' | '6';
}

export const Stack: React.FC<StackProps> = ({
  children,
  spacing = '4',
  className = '',
  ...props
}) => {
  return (
    <div
      className={`cn-stack cn-stack-${spacing} ${className}`.trim()}
      {...props}
    >
      {children}
    </div>
  );
};

Stack.displayName = 'Stack';

export const HStack: React.FC<StackProps> = ({
  children,
  spacing = '4',
  className = '',
  ...props
}) => {
  return (
    <div
      className={`cn-hstack cn-hstack-${spacing} ${className}`.trim()}
      {...props}
    >
      {children}
    </div>
  );
};

HStack.displayName = 'HStack';

export interface DividerProps extends React.HTMLAttributes<HTMLHRElement> {
  orientation?: 'horizontal' | 'vertical';
}

export const Divider: React.FC<DividerProps> = ({
  className = '',
  orientation = 'horizontal',
  style,
  ...props
}) => {
  const dividerStyle: React.CSSProperties = orientation === 'vertical'
    ? { width: '1px', height: 'auto', minHeight: '100%', borderRight: 'none', borderBottom: '1px solid var(--cn-border)', ...style }
    : { height: '1px', border: 'none', backgroundColor: 'var(--cn-border)', ...style };

  return (
    <hr
      className={`cn-divider ${className}`.trim()}
      style={dividerStyle}
      role="separator"
      {...props}
    />
  );
};

Divider.displayName = 'Divider';

export default Stack;
