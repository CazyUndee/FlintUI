# WORKFLOW.md

## Versioning

Semantic versioning: `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking API changes
- **MINOR**: Backward-compatible features
- **PATCH**: Backward-compatible fixes

## Branching Model

- `main`: Stable branch, only updated through reviewed pull requests.
- `develop`: Default working branch for local work and agent-authored changes.
- Flow: push work to `develop` -> open PR `develop` -> `main` -> manual verify/merge.

## Publishing Protocol

### Before Publishing

1. Version bump is correct.
2. Build scripts pass.
3. Tests pass.
4. Relevant docs in `README.md` and `FOR_AGENTS/*.md` are updated.
5. User approval is received before publishing.

### Publishing Commands

```bash
# npm (JavaScript/TypeScript)
npm publish --access public

# PyPI (Python)
pip install build
python -m build
twine upload dist/*

# crates.io (Rust)
cargo publish

# Go proxy (via tags)
git tag v1.0.X
git push --tags
```

## NPM Authentication

```bash
npm config set //registry.npmjs.org/:_authToken <TOKEN>
```

Never commit tokens.

## Git Commit Guidelines

### Before Committing

1. Review changes for intent.
2. Update relevant docs under `FOR_AGENTS/` if structure/tokens/components changed.
3. Verify locally.
4. Ask user before committing.

### Commit Message Format

```text
type(scope): description

[optional body]

[optional footer]
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## Important Rules

1. Ask before committing.
2. Ask before publishing.
3. Keep tokens synchronized across languages.
4. Keep `FOR_AGENTS/*.md` current when the system changes.
5. Follow semver.
