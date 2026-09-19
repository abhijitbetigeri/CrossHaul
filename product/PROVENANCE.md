# Provenance of `product/`

**Everything in this directory pre-dates the Dream AI Hackathon.**

It is a snapshot of [SC-Intelligence](https://github.com/abhijitbetigeri/SC-Intelligence), built
July 2026. It is vendored here so the submission is one
self-contained repo that a judge can read and run from a single link — not to present it as work
done on 19 Sep 2026.

Taken 19 Sep 2026 from the SC-Intelligence `master` branch.

## What it contains

| | |
|---|---|
| `cotal.yaml` | The coordination mesh — branch and supplier agent nodes, channels, anycast rebalancing |
| `runtype/` | Six agent/flow capabilities: forecast, rebalance+procure, promotion sweep, concierge, inventory admin, menu intelligence |
| `db/` | InsForge Postgres schema, the Trattoria Verde seed franchise, scraped market-intelligence data |
| `web/` | The hosted UI — landing, Branch Operations, Mesh Console, Market Intelligence |
| `docs/` | Architecture, the mesh use case, the July demo script |

## Excluded from the snapshot

Deliberately not copied: `.insforge/` (holds a live API key), `.env`, agent-tool config
directories, and build scratch. The `ct_live_*` tokens that remain in `web/branch.html` and
`runtype/BUILD.md` are Persona **client** tokens — publishable by design, embedded in the page for
the chat widget, and carrying no privileged access.

## Where today's work lives

Everything built on 19 Sep 2026 sits at the repo root — [`docs/`](../docs/) and
[`model/`](../model/) — and is listed in the root [README](../README.md). The boundary is the
directory: `product/` is July, everything else is today.
