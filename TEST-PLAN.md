# Test plan — codetopo-claude-plugin

## Scope

This repository is a plugin package — JSON manifests, a skill document, and a
pre-built MCPB bundle; it contains no compiled or interpreted product code.
Testing covers the package surface a consumer's installer reads: the plugin
manifest (`.claude-plugin/plugin.json`), the MCP server definition
(`.mcp.json`), the bundled skill (`skills/codetopo/SKILL.md`), and agreement
between the declared version, the shipped bundle filename, and the README's
download instructions. The codetopo engine itself is tested in its own
repository (nrupala/codetopo) and is out of scope here.

## Suites

| Suite | Covers | Run it | Runs in CI |
|---|---|---|---|
| Plugin manifest validation (`tests/test_plugin_manifests.py`) | JSON validity and required fields; referenced-file existence (MCP definition, skill, LICENSE); MCP server name/command shape; version consistency across plugin.json, the `.mcpb` bundle filename, the README, and the bundle's internal manifest + download pins (incl. SHA-256 pin shape) | `python3 -m unittest discover -s tests` | Yes — CI workflow |

## CI gates

- Full validation suite green on every push and pull request to `main`.
- Lint step: every `*.json` file in the repo must parse (`python3 -m json.tool`).
- No merge with a red CI run (per CONTRIBUTING).

## Cadence

- Every pull request: the full suite + JSON lint.
- Nightly / weekly: none — the package changes only with a codetopo release.
- Every release candidate: the release-readiness run (checker + evidence reads),
  per the house Release-Readiness Standard.

## Coverage bar

No numeric floor; new package content (a new manifest field, skill, or bundle)
lands with validation coverage per CONTRIBUTING.
