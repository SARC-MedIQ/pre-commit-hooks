# pre-commit-hooks

Custom [pre-commit](https://pre-commit.com/) hooks for SARC-MedIQ repos. Currently provides one hook, `check-branch-name`, which enforces the workspace branch-naming convention.

- **Repo**: `git@github.com:SARC-MedIQ/pre-commit-hooks.git`
- **Stack**: Python package (entry point `check-branch-name`), tested with tox/pytest

## The hook

`check-branch-name` validates the current branch against a regex (default `[a-z]{2,5}-\d+-[a-z0-9-]+`); consuming repos pass `-p/--pattern` to customize — mediq repos use `(hotfix|[a-z]{2,5}-\d+)-[a-z0-9-]+` (e.g. `mm-2626-scp-auto-updater`). It is declared `always_run: true`, so it fires regardless of which files changed.

Consumed from a repo's `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/SARC-MedIQ/pre-commit-hooks
  rev: 1.0.0
  hooks:
    - id: check-branch-name
```

Used by [portal](https://github.com/SARC-MedIQ/portal) (alongside isort/black/flake8) and the other Python repos.

## Structure & development

| Path | Purpose |
|---|---|
| `pre_commit_hooks/check_branch_name.py` | Hook implementation (`util.py` shared helpers) |
| `.pre-commit-hooks.yaml` | Hook registration (id, entry point, stages: commit/push/manual) |
| `setup.cfg` | Package metadata + console-script entry point |
| `tests/` | pytest suite |

```bash
tox                 # full matrix (py38/py39/py310/pypy3 + pre-commit env)
pytest tests/       # just the unit tests
tox -e pre-commit   # lint the hook repo itself
```
