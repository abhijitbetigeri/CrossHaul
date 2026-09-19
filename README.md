# Mise — the supply chain that decides for itself

**A restaurant group's branches can't talk to each other. Mise makes them.**

Mise forecasts demand per menu item per branch, explodes it through recipe bills-of-materials into
ingredient requirements, and — when a branch runs short — finds the surplus sitting in a sister
branch and moves it *before* anyone buys anything. Only the net franchise shortage reaches a
supplier, as a single purchase order for one human approval.

**Dream AI Hackathon 2026** · Frontier Tower, San Francisco · 19 Sep 2026

| | |
|---|---|
| Live product | https://k3trn3a2.insforge.site |
| Mesh Console (agents negotiating) | https://k3trn3a2.insforge.site/mesh.html |
| Branch Operations | https://k3trn3a2.insforge.site/branch.html |

---

## What existed before today, and what was built during the event

Per the hackathon's reuse rule, stated plainly.

**Existed before (built July 2026, AGI Summit — [SC-Intelligence](https://github.com/abhijitbetigeri/SC-Intelligence), winner):**

- The multi-agent coordination mesh — branch and supplier agents, anycast rebalancing over channels
- Six Runtype capabilities (forecast, rebalance+procure, promotion sweep, concierge, inventory admin, menu intelligence)
- InsForge Postgres schema, the Trattoria Verde seed franchise, and the hosted three-view UI
- The embodied extension — [Project-SCIM](https://github.com/abhijitbetigeri/Project-SCIM), a Unity 6 back-of-house simulation

**Built during the event (19 Sep 2026):**

- *(in progress — this section is filled as the day's work lands)*

The July system proved that agents *can* coordinate a restock. It had no answer for the only
question an operator actually asks: **what is that worth, and what does it cost me?** That is what
today is for.

---

## The business case

Full working: [docs/market-research.md](docs/market-research.md)

| | |
|---|---|
| Buyer | Franchise procurement manager / multi-unit operator, 3–20 locations |
| Pain | ~$72,000 per location per year in food waste; 4–10% of everything purchased |
| Price | $249 / location / month |
| Category TAM | $4.55B (2025) → $9.18B (2030), 15% CAGR |
| US SAM | ~$672M/yr — 225,000 multi-unit locations |

**Why an incumbent hasn't already won this.** MarketMan and Restaurant365 both ship inter-location
transfers — but as *bookkeeping*: a human notices the imbalance and the software records the move.
Mise makes the decision itself, from a continuous per-SKU forecast. And MarketMan gates transfers
behind its Enterprise tier, so the 3–20 unit operator either pays enterprise pricing or goes
without. That gap is the beachhead.

---

## Repo layout

```
docs/market-research.md    TAM / SAM / SOM, competitive landscape, pricing, sources
```

## Related work

| Repo | What it is |
|---|---|
| [SC-Intelligence](https://github.com/abhijitbetigeri/SC-Intelligence) | The July system — agent mesh, Runtype capabilities, InsForge backend, hosted UI |
| [Project-SCIM](https://github.com/abhijitbetigeri/Project-SCIM) | Physical-AI extension — Unity 6 back-of-house sim where a robot executes the transfer and emits demonstration data |
