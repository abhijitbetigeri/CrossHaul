# CrossHaul — the Common Operating Environment for multi-site inventory

**A company with ten sites runs ten separate inventory ledgers. So site four buys what site seven
is three days from throwing away.**

CrossHaul gives multi-site operators one operational picture and one decision on top of it:
**forecast demand per site, net it against what sister sites already hold, and buy only the
remainder.** Physical AI is embedded because a decision is only worth what it costs to execute — the
system reasons about vans, distances and spare capacity, not just quantities.

The primitive is sector-independent. **Food service is the beachhead, not the ceiling.**

**Dream AI Hackathon 2026** · Frontier Tower, San Francisco · 19 Sep 2026

| | |
|---|---|
| **The platform thesis** | [docs/platform.md](docs/platform.md) |
| Live product (food-service vertical) | https://k3trn3a2.insforge.site |
| Mesh Console — agents negotiating | https://k3trn3a2.insforge.site/mesh.html |
| Branch Operations | https://k3trn3a2.insforge.site/branch.html |

---

## The four conditions

CrossHaul applies wherever all four hold: **multiple sites under one owner · stock that dates ·
site-level demand that varies independently · a transfer that costs less than a purchase.**

| Sector | Status |
|---|---|
| **Food service** — the *Mise* vertical | **Built, live, won AGI Summit 2026** |
| FMCG manufacturing — inter-plant transfers | Adjacent, structurally identical |
| Grocery, convenience, bakery, pharma | Thesis. Not built. |

**Why the breadth is credible rather than hand-waving:** in every one of those sectors, the
coordination layer *exists at enterprise scale and does not exist at mid-market price.* SAP has run
inter-plant stock transfer orders for decades — a six-plant manufacturer does not run SAP.
Crunchtime serves 850 brands averaging 176 locations; the median multi-concept restaurant operator
runs 13 units. The mid-market of every sector has the same problem and the same non-solution. That
is one market, not five.

---

## What existed before today, and what was built during the event

Per the hackathon's reuse rule, stated plainly.

**Existed before (built July 2026, AGI Summit — [SC-Intelligence](https://github.com/abhijitbetigeri/SC-Intelligence), winner):**

- The multi-agent coordination mesh — site and supplier agents, anycast rebalancing over channels
- Six Runtype capabilities (forecast, rebalance+procure, promotion sweep, concierge, inventory admin, market intelligence)
- InsForge Postgres schema, the demo franchise seed, and the hosted three-view UI
- The embodied extension — [Project-SCIM](https://github.com/abhijitbetigeri/Project-SCIM), a Unity 6 simulation

All of it is vendored into [`product/`](product/) so this repo runs from one link — see
[product/PROVENANCE.md](product/PROVENANCE.md). **The boundary is the directory: `product/` is
July, everything else is today.**

**Built during the event (19 Sep 2026):**

- [`docs/platform.md`](docs/platform.md) — the Common Operating Environment thesis, the four conditions, the sector map, and where physical AI genuinely sits
- [`docs/market-research.md`](docs/market-research.md) — layered TAM with independent bottom-up triangulation, SAM, the beachhead, competitive landscape, pricing with the ROI working
- [`model/financial_model.py`](model/financial_model.py) + [`docs/financial-model.md`](docs/financial-model.md) — a monthly cohort model to year 3: $3.24M ARR, 84% gross margin, 4.0-month CAC payback, 7.5× LTV/CAC
- [`docs/go-to-market.md`](docs/go-to-market.md) — beachhead filters, channel ranking, the paid Cross-Branch Waste Audit wedge, 90-day plan, seven ranked falsifiers with test dates
- [`docs/competition.md`](docs/competition.md) — the "don't they already have this?" objection: capability matrix, adoption reality, rebuttal script, seven ranked threats
- [`docs/physical-ai.md`](docs/physical-ai.md) — feasibility analysis: where embodied AI pays across the chain, the transfer-economics arithmetic, and an honest negative finding on the training-data claim
- [`docs/team.md`](docs/team.md) — the solo-founder case, dated hiring plan reconciled to the model, and the honest gaps
- [`docs/vision.md`](docs/vision.md) — impact quantified (931 tons of food, ~4,740 t CO2e at year 3) and the physical-AI arc correctly bounded
- [`docs/elevenlabs-integration.md`](docs/elevenlabs-integration.md) + [`voice/`](voice/) — the voice approval channel: a console page with an embedded ElevenLabs agent, the paste-ready agent configuration, and a stdlib script that renders the stage fallback clip
- [`inference/router.py`](inference/router.py) — routing by reasoning complexity across Nebius Token Factory and Claude. Removes 83% of inference cost while the decision that spends money stays on the frontier model. Runs live against Nebius.

The git history is the evidence: this repository was created at 11:26 on 19 Sep 2026 and every
commit is timestamped that day.

The July system proved that agents *can* coordinate a restock. It had no answer for the only
question an operator actually asks: **what is that worth, and what does it cost me?** That is what
today is for.

---

## The business case — food service vertical

Full working: [docs/market-research.md](docs/market-research.md) · [docs/platform.md](docs/platform.md)

| | |
|---|---|
| Buyer | Multi-site operator, 3–20 locations — the person who does the ordering; the owner signs |
| Pain | ~$72,000 per location per year in food waste; 4–10% of everything purchased |
| Price | $249 / location / month |
| Category TAM | $4.55B (2025) → $9.18B (2030), 15% CAGR |
| US SAM | ~$672M/yr — 225,000 multi-site locations |

**Why an incumbent hasn't already won this.** MarketMan, Restaurant365 and Crunchtime all ship
inter-location transfers — but as *bookkeeping*: a human notices the imbalance and the software
records the move. Every transfer verb in Crunchtime's own training catalogue is a human one —
*create*, *request*, *process*, *reconcile*. None is *review a proposed transfer*. CrossHaul makes
the decision itself.

And the capability is priced out of the segment that needs it: MarketMan's Starter tier is $249 per
location per month, but inter-location transfers arrive with Enterprise, from $449. CrossHaul is
$249 — their entry price for the thing they charge ~1.8× for. That gap is the beachhead.

---

## Repo layout

```
docs/platform.md           the COE thesis — sector map, four conditions, physical AI   ← today
docs/market-research.md    TAM / SAM / SOM, competitive landscape, pricing             ← today
docs/competition.md        the incumbent objection, answered                           ← today
docs/financial-model.md    3-year P&L, unit economics, cash, assumption defences       ← today
docs/go-to-market.md       beachhead, channels, the wedge, falsifiers                  ← today
docs/physical-ai.md        feasibility analysis, with negative findings kept            ← today
docs/team.md               solo-founder case and hiring plan                           ← today
docs/vision.md             impact quantified, physical-AI arc bounded                  ← today
docs/elevenlabs-integration.md  the voice layer                                        ← today
model/financial_model.py   the model — monthly cohort, all inputs at the top           ← today
inference/router.py        inference routing — Nebius + Claude, with the cost model      ← today
voice/                     the ElevenLabs approval channel — console, prompt, fallback   ← today
product/                   the July system, vendored — see product/PROVENANCE.md       ← pre-existing
```

## Related work

| Repo | What it is |
|---|---|
| [SC-Intelligence](https://github.com/abhijitbetigeri/SC-Intelligence) | The July system — agent mesh, Runtype capabilities, InsForge backend, hosted UI |
| [Project-SCIM](https://github.com/abhijitbetigeri/Project-SCIM) | Embodied extension — Unity 6 simulation where a robot executes the transfer and emits a task record |
