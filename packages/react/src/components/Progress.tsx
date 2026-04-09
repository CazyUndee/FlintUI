import * as React from 'react';

export type ProgressVariant = 'default' | 'success' | 'warning' | 'error';
export type ProgressSize = 'sm' | 'md' | 'lg';

export interface ProgressProps extends React.HTMLAttributes<HTMLDivElement> {
  value?: number;
  max?: number;
  showLabel?: boolean;
  label?: string;
  variant?: ProgressVariant;
  size?: ProgressSize;
}

export const Progress: React.FC<ProgressProps> = ({
  value = 0,
  max = 100,
  showLabel = false,
  label,
  variant = 'default',
  size = 'md',
  className = '',
  ...props
}) => {
  const percentage = Math.min(Math.max((value / max) * 100, 0), 100);

  return (
    <div className={className} {...props}>
      {showLabel && (
        <div className="cn-progress-label">
          <span>{label ?? `${percentage.toFixed(0)}%`}</span>
        </div>
      )}
      <div
        className={`cn-progress ${size !== 'md' ? `cn-progress-${size}` : ''} ${variant !== 'default' ? `cn-progress-${variant}` : ''}`.trim()}
        role="progressbar"
        aria-valuenow={percentage}
        aria-valuemin={0}
        aria-valuemax={100}
      >
        <div className="cn-progress-bar" style={{ width: `${percentage}%` }} />
      </div>
    </div>
  );
};

Progress.displayName = 'Progress';

export default Progress;
