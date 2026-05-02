# CronixUI

A multi-platform, multi-language UI toolkit with a dark theme, crimson accents, and Outfit typography.

> If you find this useful, consider starring this repo!

Learn more [here](https://deepwiki.com/CazyUndee/CronixUI)
## Branch Strategy

- `main` is stable/production-ready.
- `develop` is the active development branch for day-to-day work (including agent-driven changes).
- Open pull requests from `develop` to `main`, then manually review and merge.

## Quick Install

### Option 1: Agentic Install
If you are lazy then paste the following into your agent (claude code, opencode, openclaw...):

```
Install CronixUI v1.1.2:  
1. Detect project type (package.json, pubspec.yaml, etc.)  
2. Ask user which platform:  
   - Web (JS/React/Vue/Svelte/Solid): npm install cronixui  
   - Python: pip install cronixui  
   - Go: go get github.com/CazyUndee/CronixUI/packages/go/cronixui  
   - Rust: cargo add cronixui  
   - Flutter: add git dependency to pubspec.yaml  
   - WinUI: dotnet add package CronixUI.WinUI  
3. Install and show import example  
4. Create test component to verify  
```

### Option 2: Manual Install

Web Platforms:
All web platforms share the same base install:
```
npm install cronixui
```

**Framework-specific imports:**
- HTML/TypeScript: Use base CSS/JS files
- React: import { Button } from 'cronixui/react'
- Vue: import { CnButton } from 'cronixui/vue'
- Svelte: import { Button } from 'cronixui/svelte'
- Solid: import { Button } from 'cronixui/solid'

**Native Platforms:**
   
Python:
```bash
pip install cronixui
```
Go: 
```bash
go get github.com/CazyUndee/CronixUI/packages/go/cronixui
```
Rust: 
```bash
cargo add cronixui
```
Flutter:   

Add git dependency to pubspec.yaml
```bash
dependencies:  
  cronixui:  
    git:  
      url: https://github.com/CazyUndee/CronixUI.git  
      path: packages/flutter
```
WinUI:   
```
dotnet add package CronixUI.WinUI
```

Ask Devin in the [deepwiki](https://deepwiki.com/CazyUndee/CronixUI/1.1-getting-started-and-installation) if you encounter issues.

## LLMs
If you are an LLM, read the FOR_AGENTS/AGENTS.md file to understand the codebase.

## License

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

