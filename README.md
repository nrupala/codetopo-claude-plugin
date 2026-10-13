# codetopo — Claude plugin

Domain-blind code graphs for AI agents: symbols, calls, blast radius, proof-checked snapshots.

codetopo turns any source repository into a deterministic, queryable code graph and serves it over MCP — 12 tools for indexing, symbol search, call/import traversal, blast radius, path finding, and verification of a tamper-evident audit chain. It runs entirely on your machine: no accounts, no API keys, no telemetry, no network calls at runtime.

- Engine and full documentation: https://github.com/nrupala/codetopo
- Live demo on its own repository: https://aimlds.org/codetopo
- Also on the Official MCP Registry as `io.github.nrupala/codetopo`, and on crates.io as `codetopo-mcp`.

## Install

**Prerequisite (plugin route):** a stable Rust toolchain, then:

```sh
cargo install codetopo-mcp
```

**Claude Code:** add this repository as a plugin — it declares the `codetopo` MCP server in `.mcp.json` (`codetopo-mcp` over stdio, no arguments) and ships a skill that teaches the index → search → query loop.

**Claude Desktop:** download `codetopo-0.3.5.mcpb` from this repository and open it (or drag it into Claude Desktop's Extensions). The bundle needs no pre-installed binary: on first run its launcher downloads the pinned build for your platform from the project's GitHub release and refuses to run it unless the SHA-256 matches the pin baked into the bundle.

## Privacy

codetopo runs entirely on your machine. It collects no usage data, has no accounts, and sends nothing to the developer or any third party. Repositories you index are parsed locally and never uploaded; index databases and snapshots are files on your disk, kept until you delete them. The one network action is the bundle launcher's first-run download described above. Full text: the Privacy Policy section of the main repository's README.

## License

AGPL-3.0-or-later (see `LICENSE`).

Owned by [Nrupal Akolkar](https://nrupalakolkar.com) · Built with [Muse by Meta](https://muse.ai/join) — join Muse, then redeem code **101EEK** in Settings within 48 hours of joining and we both earn tokens.

Support: info@nrupalakolkar.com
