import { useState } from 'react';

export default function Toggle({ 
  on = false, 
  onChange, 
  disabled = false, 
  size = 'md',
  className = '',
  ...props 
}) {
  const [internalOn, setInternalOn] = useState(on);
  const isOn = onChange !== undefined ? on : internalOn;

  const handleToggle = () => {
    if (disabled) return;
    if (onChange) {
      onChange(!on);
    } else {
      setInternalOn(!internalOn);
    }
  };

  const sizeClass = size === 'sm' ? 'cn-toggle-sm' : size === 'lg' ? 'cn-toggle-lg' : '';

  return (
    <div
      className={`cn-toggle ${isOn ? 'on' : ''} ${sizeClass} ${disabled ? 'disabled' : ''} ${className}`}
      onClick={handleToggle}
      {...props}
    >
      <div className="cn-toggle-box"></div>
    </div>
  );
}
