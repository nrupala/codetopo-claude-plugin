---
name: codetopo
description: Answer structural questions about a codebase — what calls this, what breaks if this changes, how are these connected — from a codetopo code graph instead of reading whole files. Use when exploring an unfamiliar repository, tracing call chains, estimating change impact, or verifying a snapshot's integrity.
---

# codetopo

codetopo indexes a repository once into a local graph database (symbols and typed relationships: calls, imports, overrides, implementations) and answers structural questions over MCP. Output is aggregate-first — counts before full lists — to keep token budgets sane. Nothing in the indexed code is executed.

## The loop

1. **Index** — `codetopo_index` with `repo_path` and a `db_path` for the graph database. Re-index after the code changes; an index is a snapshot, not a live view.
2. **Orient** — `codetopo_describe_schema` (no database needed) for node/edge kinds and tier rules; `codetopo_stats` for the size of an index.
3. **Discover** — `codetopo_search_symbols` finds exact node ids by name fragment. Never guess an id; the exact-id queries error on unknown ids by design.
4. **Query** — `codetopo_get_symbol` (one node in full), `codetopo_descendants` / `codetopo_ancestors` (transitive reach over calls and imports), `codetopo_blast_radius` (dependents, overriders, implementers), `codetopo_path` (shortest typed path between two nodes), `codetopo_neighborhood` (the subgraph around a node).
5. **Trust** — `codetopo_verify` checks the index's tamper-evident audit chain before reasoning over it; `codetopo_snapshot` exports the graph bound to the audit head.

## Working rules

- Use exact node ids from search or schema output.
- Re-index after edits before trusting answers about changed code.
- Verify before citing a snapshot as evidence.
- Report structure only — codetopo proves what the graph contains, not whether code is correct.
