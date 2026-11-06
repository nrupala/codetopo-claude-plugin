# Changelog

All notable changes to the codetopo Claude plugin are recorded here, per release, in plain language
a user can act on — never a raw commit log. Entries are added with the change itself
(see CONTRIBUTING), and any security fix names the CVE or similar identifier where
one exists.

## [Unreleased]

## [0.5.0] — 2026-11-06

First GitHub Release of the already-published 0.5.0 plugin package (the version
declared in `.claude-plugin/plugin.json` and shipped as `codetopo-0.5.0.mcpb`).

### Added

- Claude plugin manifest (`.claude-plugin/plugin.json`) declaring the codetopo
  MCP server, plus the `.mcp.json` server definition (`codetopo-mcp` over stdio).
- Bundled skill (`skills/codetopo/SKILL.md`) teaching the index → search → query loop.
- `codetopo-0.5.0.mcpb` bundle for Claude Desktop: on first run its launcher
  downloads the pinned platform build and verifies its SHA-256 before running it.
- Project documentation set: CONTRIBUTING, SECURITY (private vulnerability
  reporting), TEST-PLAN, and a CI validation suite for the plugin manifests.
