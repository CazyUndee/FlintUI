import { forwardRef } from 'react';

const Slider = forwardRef(function Slider({ 
  value = 0, 
  min = 0, 
  max = 100, 
  step = 1,
  onChange,
  disabled = false,
  className = '',
  ...props 
}, ref) {
  return (
    <input
      ref={ref}
      type="range"
      className={`cn-slider ${className}`}
      value={value}
      min={min}
      max={max}
      step={step}
      onChange={(e) => onChange?.(Number(e.target.value))}
      disabled={disabled}
      {...props}
    />
  );
});

export default Slider;
