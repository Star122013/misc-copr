# rust-copr

## GitHub Actions: upstream change -> COPR rebuild

This repository contains a scheduled workflow at:

- `.github/workflows/copr-upstream-rebuild.yml`

It runs every 12 hours (and supports manual `workflow_dispatch`), checks upstream
commits, and triggers `copr-cli build-package` only when updates are detected.

### Recommended mode: multi-package config file

Create `.github/copr-packages.json`:

```json
{
  "packages": [
    {
      "id": "noctalia-shell-git",
      "upstream_repo": "noctalia-dev/noctalia-shell",
      "upstream_branch": "main",
      "copr_project": "yourname/yourproject",
      "copr_package": "noctalia-shell-git",
      "copr_url": "https://copr.fedorainfracloud.org"
    }
  ]
}
```

Use `.github/copr-packages.example.json` as the starting template.

Each package entry is checked independently, and builds run in parallel.

### Backward-compatible mode: single package via variables

If `.github/copr-packages.json` is absent, the workflow falls back to these repo
variables:

- `UPSTREAM_REPO`
- `UPSTREAM_BRANCH` (optional, defaults to `main`)
- `COPR_PROJECT`
- `COPR_PACKAGE`
- `COPR_URL` (optional, defaults to `https://copr.fedorainfracloud.org`)

### Required repository secrets

- `COPR_LOGIN`
- `COPR_USERNAME`
- `COPR_TOKEN`

### State tracking

The workflow stores last processed commits in repository Actions variables:

- `LAST_UPSTREAM_SHA_<ID>`

`<ID>` is your package `id` uppercased and sanitized to `A-Z0-9_`.
