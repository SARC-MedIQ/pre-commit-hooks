[![build status](https://github.com/SARC-MedIQ/pre-commit-hooks/actions/workflows/main.yml/badge.svg)](https://github.com/SARC-MedIQ/pre-commit-hooks/actions/workflows/main.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/SARC-MedIQ/pre-commit-hooks/main.svg)](https://results.pre-commit.ci/latest/github/SARC-MedIQ/pre-commit-hooks/main)

pre-commit-hooks
================

Some out-of-the-box hooks for pre-commit.

See also: https://github.com/pre-commit/pre-commit


### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/SARC-MedIQ/pre-commit-hooks
    rev: 1.0.0  # Use the ref you want to point at
    hooks:
    -   id: check-branch-name
```

### Hooks available

#### `check-branch-name`
Check the branch name meets the format requirements
  - `-p, --pattern` - Provide pattern the branch must match (default [a-z]{2,5)-\d+-[a-z0-9-]+), can be used multiple times

Note that `check-branch-name` is configured by default to [`always_run`](https://pre-commit.com/#config-always_run).
As a result, it will ignore any setting of [`files`](https://pre-commit.com/#config-files),
[`exclude`](https://pre-commit.com/#config-exclude), [`types`](https://pre-commit.com/#config-types)
or [`exclude_types`](https://pre-commit.com/#config-exclude_types).
Set [`always_run: false`](https://pre-commit.com/#config-always_run) to allow this hook to be skipped according to these
file filters. Caveat: In this configuration, empty commits (`git commit --allow-empty`) would always be allowed by this hook.
