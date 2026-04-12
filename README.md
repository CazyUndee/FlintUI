# CronixUI

A multi-platform, multi-language UI toolkit with a dark theme, crimson accents, and Outfit typography.

> If you find this useful, consider starring this repo!

## Notices:
- Python installation should be fixed now, if not, start an issue and paste the logs
- working on a proper cli installation for flutter 
- it is still really early, so there might be issues
- start an issue if you encounter any of them

## Installation

### JavaScript/TypeScript

```bash
npm install cronixui
```

### React, Vue, Svelte, Solid

```bash
npm install @cronixui/react
npm install @cronixui/vue
npm install @cronixui/svelte
npm install @cronixui/solid
```

### Python

```bash
pip install cronixui
```

### Go

```bash
go get github.com/CazyUndee/CronixUI/packages/go/cronixui
```

### Rust

```toml
[dependencies]
cronixui = "1.1.2"
```

### Flutter

```yaml
dependencies:
  cronixui:
    git:
      url: https://github.com/CazyUndee/CronixUI.git
      path: packages/flutter
```

### CDN

```html
<link rel="stylesheet" href="https://unpkg.com/cronixui@1.1.2/packages/web/dist/cronixui.css">
<script src="https://unpkg.com/cronixui@1.1.2/packages/web/dist/cronixui.js"></script>
```

## Quick Start (Web)

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>My App</title>
<link rel="stylesheet" href="https://unpkg.com/cronixui@1.1.2/packages/web/dist/cronixui.css">
</head>
<body>
<div class="cn-container">
<h1 class="cn-h1">Hello, CronixUI!</h1>
<button class="cn-btn cn-btn-primary">Get Started</button>
</div>
<script src="https://unpkg.com/cronixui@1.1.2/packages/web/dist/cronixui.js"></script>
</body>
</html>
```

## Design Tokens

CronixUI uses CSS custom properties for consistent theming:

| Token | Value | Description |
|-------|-------|-------------|
| `--cn-bg` | `#0a0a0a` | Background |
| `--cn-surface` | `#111111` | Surface |
| `--cn-accent` | `#6b2323` | Crimson accent |
| `--cn-text` | `#f0ede8` | Primary text |
| `--cn-border` | `rgba(255,255,255,0.08)` | Border color |

## Components

### Typography

```html
<h1 class="cn-h1">Heading 1</h1>
<h2 class="cn-h2">Heading 2</h2>
<h3 class="cn-h3">Heading 3</h3>
<p class="cn-text-muted">Muted text</p>
<p class="cn-text-dim">Dim text</p>
<code class="cn-text-mono">code</code>
```

### Buttons

```html
<button class="cn-btn cn-btn-primary">Primary</button>
<button class="cn-btn">Default</button>
<button class="cn-btn cn-btn-ghost">Ghost</button>
<button class="cn-btn cn-btn-outline">Outline</button>
<button class="cn-btn cn-btn-success">Success</button>
<button class="cn-btn cn-btn-danger">Danger</button>

<!-- Sizes -->
<button class="cn-btn cn-btn-sm">Small</button>
<button class="cn-btn cn-btn-lg">Large</button>

<!-- Button Group -->
<div class="cn-btn-group">
  <button class="cn-btn">Left</button>
  <button class="cn-btn">Center</button>
  <button class="cn-btn">Right</button>
</div>
```

### Inputs

```html
<!-- Basic input -->
<input class="cn-input" placeholder="Enter text...">

<!-- With label -->
<div class="cn-form-group">
  <label class="cn-form-label">Email</label>
  <input class="cn-input" type="email" placeholder="you@example.com">
</div>

<!-- With error -->
<div class="cn-form-group">
  <label class="cn-form-label">Password</label>
  <input class="cn-input cn-input-error" type="password">
  <span class="cn-form-error">Password is required</span>
</div>

<!-- Sizes -->
<input class="cn-input cn-input-sm" placeholder="Small">
<input class="cn-input cn-input-lg" placeholder="Large">

<!-- Select -->
<div class="cn-select-wrapper">
  <select class="cn-select">
    <option>Option 1</option>
    <option>Option 2</option>
  </select>
</div>

<!-- Textarea -->
<textarea class="cn-input cn-textarea" placeholder="Long text..."></textarea>
```

### Checkbox & Radio

```html
<label class="cn-checkbox">
  <input type="checkbox" checked>
  <span class="cn-checkbox-box"></span>
  <span class="cn-checkbox-label">Checked</span>
</label>

<label class="cn-radio">
  <input type="radio" name="group" checked>
  <span class="cn-radio-box"></span>
  <span class="cn-radio-label">Option A</span>
</label>
```

### Toggle

```html
<div class="cn-toggle on"></div>
<span class="cn-toggle-label">Enabled</span>
```

```javascript
// Toggle state
document.querySelector('.cn-toggle').classList.toggle('on');
```

### Slider

```html
<input type="range" class="cn-slider" min="0" max="100" value="50">
```

### Badges

```html
<span class="cn-badge cn-badge-default">Default</span>
<span class="cn-badge cn-badge-accent">Accent</span>
<span class="cn-badge cn-badge-success">Success</span>
<span class="cn-badge cn-badge-warning">Warning</span>
<span class="cn-badge cn-badge-error">Error</span>
<span class="cn-badge cn-badge-info">Info</span>

<!-- Solid variants -->
<span class="cn-badge cn-badge-solid cn-badge-accent">Solid</span>
```

### Tags

```html
<span class="cn-tag">
  Tag Name
  <span class="cn-tag-remove">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <line x1="18" y1="6" x2="6" y2="18"/>
      <line x1="6" y1="6" x2="18" y2="18"/>
    </svg>
  </span>
</span>
```

### Stats

```html
<div class="cn-stat">
  <div class="cn-stat-value">2,847</div>
  <div class="cn-stat-label">Total runs</div>
  <div class="cn-stat-delta cn-stat-delta-up">+12%</div>
</div>
```

### Progress

```html
<div class="cn-progress-label"><span>Loading</span><span>68%</span></div>
<div class="cn-progress">
  <div class="cn-progress-bar" style="width: 68%;"></div>
</div>

<!-- Variants -->
<div class="cn-progress cn-progress-success">...</div>
<div class="cn-progress cn-progress-warning">...</div>
<div class="cn-progress cn-progress-error">...</div>
<div class="cn-progress cn-progress-lg">...</div>
```

### Cards

```html
<div class="cn-card">
  <h3 class="cn-card-title">Card Title</h3>
  <p class="cn-card-body">Card content.</p>
</div>

<!-- Clickable -->
<div class="cn-card cn-card-clickable">...</div>

<!-- With header/footer -->
<div class="cn-card">
  <div class="cn-card-header">
    <span class="cn-card-title">Title</span>
    <button class="cn-btn cn-btn-sm">Action</button>
  </div>
  <p class="cn-card-body">Content</p>
  <div class="cn-card-footer">Footer</div>
</div>
```

### Navigation

```html
<div class="cn-nav">
  <button class="cn-nav-item cn-nav-active">Home</button>
  <button class="cn-nav-item">Projects</button>
  <button class="cn-nav-item">Settings</button>
</div>
```

```javascript
CronixUI.Nav.init();
```

### Tabs

```html
<div class="cn-tabs">
  <div class="cn-tabs-list">
    <button class="cn-tab cn-tab-active">Tab 1</button>
    <button class="cn-tab">Tab 2</button>
    <button class="cn-tab">Tab 3</button>
  </div>
</div>
<div class="cn-tab-content">
  <div class="cn-tab-panel cn-tab-panel-active">Content 1</div>
  <div class="cn-tab-panel">Content 2</div>
  <div class="cn-tab-panel">Content 3</div>
</div>
```

### Breadcrumb

```html
<div class="cn-breadcrumb">
  <a href="#" class="cn-breadcrumb-item">Home</a>
  <span class="cn-breadcrumb-separator">/</span>
  <a href="#" class="cn-breadcrumb-item">Projects</a>
  <span class="cn-breadcrumb-separator">/</span>
  <span class="cn-breadcrumb-current">Current</span>
</div>
```

### Alerts

```html
<div class="cn-alert cn-alert-info">
  <div class="cn-alert-icon">...</div>
  <div class="cn-alert-content">
    <div class="cn-alert-title">Title</div>
    <div class="cn-alert-message">Message</div>
  </div>
  <button class="cn-alert-close">×</button>
</div>
```

Variants: `cn-alert-info`, `cn-alert-success`, `cn-alert-warning`, `cn-alert-error`

### Toast

```javascript
// Show toast
CronixUI.Toast.success('Operation completed!');
CronixUI.Toast.error('Something went wrong');
CronixUI.Toast.warning('Please review');
CronixUI.Toast.info('New updates');

// With title
CronixUI.Toast.show({
  title: 'Success',
  message: 'Your changes have been saved.',
  type: 'success',
  duration: 5000
});
```

### Modal

```html
<div class="cn-modal-backdrop" id="myModal">
  <div class="cn-modal">
    <div class="cn-modal-header">
      <h3 class="cn-modal-title">Modal Title</h3>
      <button class="cn-modal-close">×</button>
    </div>
    <div class="cn-modal-body">Content</div>
    <div class="cn-modal-footer">
      <button class="cn-btn cn-btn-ghost">Cancel</button>
      <button class="cn-btn cn-btn-primary">Confirm</button>
    </div>
  </div>
</div>
```

```javascript
const modal = document.getElementById('myModal');
modal._cnModal.open();
modal._cnModal.close();
```

### Dropdown

```html
<div class="cn-dropdown">
  <button class="cn-btn cn-dropdown-trigger">
    Menu <svg>...</svg>
  </button>
  <div class="cn-dropdown-menu">
    <div class="cn-dropdown-item">Profile</div>
    <div class="cn-dropdown-item">Settings</div>
    <div class="cn-dropdown-divider"></div>
    <div class="cn-dropdown-item">Logout</div>
  </div>
</div>
```

### Tooltip

```html
<div class="cn-tooltip">
  <button class="cn-btn">Hover me</button>
  <div class="cn-tooltip-content">Tooltip text</div>
</div>
```

### Table

```html
<div class="cn-table-wrapper cn-table-sortable">
  <table class="cn-table">
    <thead>
      <tr>
        <th data-sort="name">Name</th>
        <th data-sort="value">Value</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Item 1</td>
        <td>100</td>
      </tr>
    </tbody>
  </table>
</div>
```

### List

```html
<div class="cn-list">
  <div class="cn-list-item cn-list-item-clickable">
    <div class="cn-list-item-content">
      <div class="cn-list-item-title">Title</div>
      <div class="cn-list-item-subtitle">Subtitle</div>
    </div>
  </div>
</div>
```

### Accordion

```html
<div class="cn-accordion">
  <div class="cn-accordion-item cn-accordion-open">
    <div class="cn-accordion-header">
      <span class="cn-accordion-title">Section 1</span>
      <svg class="cn-accordion-icon">...</svg>
    </div>
    <div class="cn-accordion-content">Content</div>
  </div>
</div>
```

### Avatar

```html
<div class="cn-avatar">JD</div>
<div class="cn-avatar cn-avatar-sm">AB</div>
<div class="cn-avatar cn-avatar-lg">XY</div>
<div class="cn-avatar cn-avatar-xl">ZZ</div>

<!-- Group -->
<div class="cn-avatar-group">
  <div class="cn-avatar">A</div>
  <div class="cn-avatar">B</div>
  <div class="cn-avatar">+5</div>
</div>
```

### Pagination

```html
<div class="cn-pagination" id="pagination"></div>
```

```javascript
new CronixUI.Pagination(document.getElementById('pagination'), {
  total: 10,
  current: 1,
  onChange: (page) => console.log('Page:', page)
});
```

### File Input

```html
<div class="cn-file-input">
  <input type="file">
  <div class="cn-file-input-label">
    <svg class="cn-file-input-icon">...</svg>
    <div class="cn-file-input-text">
      <span>Click to upload</span> or drag and drop
    </div>
  </div>
</div>
```

### Search

```html
<div class="cn-search">
  <svg class="cn-search-icon">...</svg>
  <input class="cn-input cn-search-input" placeholder="Search...">
  <div class="cn-search-results"></div>
</div>
```

```javascript
const search = document.querySelector('.cn-search');
search._cnSearch.setItems([
  { title: 'Result 1', subtitle: 'Description', action: () => {} },
  { title: 'Result 2', action: () => {} }
]);
```

### Command Palette

```html
<div class="cn-command-palette" id="cmd">
  <div class="cn-command-palette-inner">
    <input class="cn-command-palette-input" placeholder="Type a command...">
    <div class="cn-command-palette-results"></div>
  </div>
</div>
```

```javascript
const cmd = document.getElementById('cmd');
new CronixUI.CommandPalette(cmd);
cmd._cnCommandPalette.setItems([
  { title: 'New File', kbd: 'Ctrl+N', action: () => {} },
  { title: 'Save', kbd: 'Ctrl+S', action: () => {} }
]);

// Open
cmd._cnCommandPalette.open();
```

### Loading States

```html
<!-- Spinner -->
<div class="cn-spinner"></div>
<div class="cn-spinner cn-spinner-sm"></div>
<div class="cn-spinner cn-spinner-lg"></div>

<!-- Skeleton -->
<div class="cn-skeleton cn-skeleton-title"></div>
<div class="cn-skeleton cn-skeleton-text"></div>
<div class="cn-skeleton cn-skeleton-avatar"></div>
```

### Layout

```html
<!-- Container -->
<div class="cn-container">...</div>
<div class="cn-container-sm">...</div>
<div class="cn-container-lg">...</div>

<!-- Flex -->
<div class="cn-flex cn-items-center cn-gap-4">...</div>

<!-- Grid -->
<div class="cn-grid cn-grid-3">...</div>

<!-- Stack -->
<div class="cn-stack">...</div>
<div class="cn-hstack">...</div>

<!-- Sections -->
<div class="cn-section">...</div>
<div class="cn-divider"></div>
```

## JavaScript API

### Global Object

```javascript
// Initialize all components
CronixUI.init();

// Utilities
CronixUI.$(selector);
CronixUI.$$(selector);
CronixUI.createEl(tag, className, attrs);
```

### Classes

| Class | Methods |
|-------|---------|
| `CronixUI.Toggle` | `toggle()`, `isOn()`, `setOn(bool)` |
| `CronixUI.Modal` | `open()`, `close()` |
| `CronixUI.Dropdown` | `open()`, `close()`, `toggle()` |
| `CronixUI.Toast` | `show(opts)`, `success()`, `error()`, `warning()`, `info()` |
| `CronixUI.Tabs` | `setActive(index)` |
| `CronixUI.Accordion` | `toggle(item)`, `openAll()`, `closeAll()` |
| `CronixUI.Pagination` | `goTo(page)`, `render()` |
| `CronixUI.CommandPalette` | `open()`, `close()`, `setItems([])` |
| `CronixUI.Search` | `setItems([])`, `filter()`, `open()`, `close()` |

## Browser Support

- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

## License

GPL 3.0, see LICENSE for details.
