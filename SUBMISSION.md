# Submission — Dream AI Hackathon 2026

Paste-ready answers for the submission form. **Submit by 16:15**, deadline is 16:30.

---

## Sponsor tools used

☑️ **ElevenLabs** &nbsp;&nbsp; ☑️ **Nebius** — tick both.

### How ElevenLabs is used

**As the product's approval channel, not a voiceover.**

The failure mode of this category is not features — it is that site managers are on their feet for
ten hours and never open a dashboard. So CrossHaul calls them, states the decision it has already
made, and takes "yes" for an answer:

> *"Downtown is thirty-six units short for the weekend. Marina is ten over par on a lot that expires
> in two days, so I moved those across on a vehicle already running the route — no purchase, no
> write-off. The remaining twenty-six went to RFQ and Bay Supply won it at two-oh-five a unit.
> Fifty-three thirty. Want me to release it?"*

- **Conversational agent**, published and live, embedded at
  [k3trn3a2.insforge.site/voice.html](https://k3trn3a2.insforge.site/voice.html). Authentication
  off, domain allowlisted, origin check on — the public-widget posture, so no key reaches the
  browser.
- **Text-to-speech** renders a pre-recorded copy of the same call that plays from disk, so the stage
  demo cannot fail on venue wifi.
- Agent configuration and prompt: [`voice/agent-prompt.md`](voice/agent-prompt.md) ·
  page: [`voice/console.html`](voice/console.html) · fallback:
  [`voice/render_fallback.sh`](voice/render_fallback.sh)

Voice is a go-to-market argument as much as a product one: a system you answer like a phone call has
a lower adoption cost than one more tab, and lower adoption cost means a shorter sales cycle.

### How Nebius is used

**Inference routing by reasoning complexity — a gross-margin decision, not a sponsor bolt-on.**

Routing every call to a frontier model is the same mistake as running every query on your largest
database instance. Matching an ingredient is not the same problem as clearing a multi-constraint
rebalance across seven sites against supplier minimums and expiry windows.

| Call class | Reasoning | Routed to | All-frontier | Routed |
|---|---|---|---:|---:|
| Demand forecast | low | **Nebius** | $3.015 | $0.046 |
| Market intelligence | low | **Nebius** | $0.600 | $0.010 |
| Promotion sweep | low | Haiku 4.5 | $0.108 | $0.022 |
| Operator dialogue | medium | Sonnet 5 | $1.050 | $0.420 |
| Rebalance + procurement | **high** | Opus 5 | $0.385 | $0.385 |
| **Per location / month** | | | **$5.16** | **$0.88** |

**83% of inference cost removed, and the one call that decides how money gets spent stays on the
frontier model.** Verified live against Nebius Token Factory (OpenAI-compatible API,
`openai/gpt-oss-120b`): it returned days-of-cover correctly for **$0.000083** against **$0.006580**
for the same call on a frontier model — a 79× difference on a call that needs no judgement.

Code: [`inference/router.py`](inference/router.py) — run `python3 inference/router.py --live`.

*Stated honestly: inference is not the dominant cost-of-revenue line — customer success is. Routing
contributes roughly a fifth of the modelled $60 → $40 per-location reduction that carries gross
margin from 76% to 84%.*

---

## Project links

| | |
|---|---|
| **Pitch deck** | *(the Slides artifact link — **must be shared for "anyone with the link" first**)* |
| **Live demo** | https://k3trn3a2.insforge.site |
| ↳ voice approval channel | https://k3trn3a2.insforge.site/voice.html |
| ↳ agent mesh negotiating | https://k3trn3a2.insforge.site/mesh.html |
| ↳ site operations | https://k3trn3a2.insforge.site/branch.html |
| **GitHub** | https://github.com/abhijitbetigeri/CrossHaul |
| Embodied simulation | https://abhijitbetigeri.github.io/Project-SCIM/ |
| Pre-existing codebase | https://github.com/abhijitbetigeri/SC-Intelligence |

---

## One-paragraph project description

CrossHaul is a Common Operating Environment for multi-site inventory. A company with ten sites runs
ten separate inventory ledgers, so site four buys what site seven is three days from throwing away.
CrossHaul forecasts demand per site, nets it against what sister sites already hold, and sends a
supplier only the remainder — as one purchase order for one human approval. The primitive is
sector-independent: it applies wherever multiple sites sit under one owner, stock dates, site demand
varies independently, and a transfer costs less than a purchase. Food service is the beachhead, not
the ceiling.

---

## Reuse disclosure

Per the reuse rule, the boundary is a directory:

- **`product/`** — the July 2026 codebase: the coordination mesh,
  six agent capabilities, the Postgres schema and the hosted UI. Pre-existing. See
  [`product/PROVENANCE.md`](product/PROVENANCE.md).
- **Everything else** — built 19 Sep 2026. The repository was created at 11:26 that morning and
  every commit is timestamped that day: the platform thesis, market research, the financial model,
  go-to-market, competitive analysis, the physical-AI feasibility study, the ElevenLabs voice
  channel, and the Nebius inference router.

The earlier codebase could coordinate a restock. It had no answer for the only question an operator
actually asks: **what is that worth, and what does it cost me?** That is what today built.

---

## Form field: Project Links

```
Pitch Deck: <paste the shared deck or Google Slides link>
Live Demo: https://k3trn3a2.insforge.site
  — voice approval channel: https://k3trn3a2.insforge.site/voice.html
  — agent mesh negotiating: https://k3trn3a2.insforge.site/mesh.html
  — site operations console: https://k3trn3a2.insforge.site/branch.html
GitHub Repository: https://github.com/abhijitbetigeri/CrossHaul
Robot simulation (playable): https://abhijitbetigeri.github.io/Project-SCIM/sim/
```

## Form field: Project Overview

```
Every site in a multi-site operation forecasts alone, orders alone, and writes off alone. There
is no shared picture of what the business is holding, so one branch buys what another is days
away from discarding. Waste runs 4-10% of everything purchased — around $72,000 per site per
year, and $162B a year in US food service alone.

CrossHaul is a Common Operating Environment for multi-site inventory. It forecasts demand per
branch, explodes it through the recipe bill-of-materials, nets each shortage against surplus
already held at other branches of the same franchise, and sends a supplier only the remainder —
as one purchase order, for one human approval. Stock close to expiry is flagged for markdown
rather than written off. Nothing moves without a person tapping accept.

Target users: multi-site operators running 3-20 locations, clustered within driving distance of
each other. The champion is whoever does the ordering; the owner signs. Food service is the
beachhead, not the ceiling — the primitive applies wherever four conditions hold: multiple sites
under one owner, stock that dates, site-level demand that varies independently, and a transfer
that costs less than a purchase. FMCG manufacturing, grocery and pharmacy are structurally
identical; none of them is built.
```

## Form field: AI & Hackathon Build

```
HOW IT USES AI — three layers, routed by reasoning complexity rather than by vendor.

1. Coordination. Each branch and each supplier is an autonomous agent. A shortage posts to a
shared channel and anycast routes it to the branches holding surplus; nearest branch and
nearest-expiry lot claims it. Claude Opus 5 makes the multi-constraint decision — expiry windows,
distance, supplier minimums, landed cost — and drafts the purchase order for approval.

2. High-volume, low-reasoning work runs on open-weights models via Nebius Token Factory
(openai/gpt-oss-120b, OpenAI-compatible API): per-SKU demand forecasting and bulk extraction of
market data. This removes 83% of inference cost per location per month ($5.16 to $0.88), verified
live — the forecast call costs 79x less there — while the one call that decides how money is spent
stays on the frontier model. Code: inference/router.py.

3. Operator dialogue runs on Claude Sonnet 5 behind an ElevenLabs conversational agent. The
product calls the operator, states the decision it already made, and takes approval by voice,
because the person who owns the stock is not sitting at a screen.

BUILT DURING THE HACKATHON (19 Sep 2026)

- The ElevenLabs voice approval channel: a published conversational agent, an embedded console at
  /voice.html, and a TTS-rendered fallback clip that plays from disk so the demo cannot fail.
- The Nebius inference router and its cost model, verified against the live API.
- The entire commercial case, which the system previously had no answer for: layered TAM with an
  independent bottom-up triangulation, a monthly-cohort three-year financial model, go-to-market
  with seven ranked falsifiers and test dates, competitive analysis resolving what incumbents do
  and do not do, and a physical-AI feasibility study that reaches negative conclusions where the
  evidence points that way.

PRE-EXISTING, DISCLOSED — built July 2026 and vendored under product/ with a PROVENANCE file: the
coordination mesh, six agent capabilities, the Postgres schema and the hosted UI. The boundary is a
directory: product/ is July, everything else is
today. This repository was created at 11:26 on 19 Sep 2026 and every commit is timestamped that
day.

The earlier codebase could coordinate a restock. It had no answer for the only question an operator
actually asks: what is that worth, and what does it cost me. That is what today built.
```

## Form field addendum: the multi-agent coordination, in detail

Use this in place of point 1 in "AI & Hackathon Build" if there is room, or as the answer if asked
to elaborate.

```
MULTI-AGENT COORDINATION — no central planner

Every branch and every supplier is a node on a coordination mesh, not a row in one planner's
database. Nodes hold presence and talk over shared channels: #demand, #rebalance, #procurement,
#promotions, #decisions. The reference franchise runs three branch nodes, a rebalance coordinator,
a procurement node and two supplier bidders.

One cycle runs like this.

1. FORECAST. Each branch node predicts next-7-day demand per menu item, then explodes it through
   the recipe bill-of-materials into ingredient requirements, and derives par levels, reorder
   points and days-of-cover from its own burn rate.

2. POST. Shortages and surpluses post to #rebalance as stock alerts — keyed off days-of-cover and
   spoil risk rather than a hand-authored reorder point, so the signal reflects actual demand.

3. ANYCAST. A shortage is not broadcast to a planner; it is anycast to whichever nodes are holding
   surplus. Holders claim it competitively — nearest branch first, nearest-expiry lot first, so the
   stock most at risk of being written off moves first. The claimant proposes a transfer.

4. CONFIRM. The rebalance coordinator confirms the transfer and writes it to shared state.

5. NET, THEN BUY. Only the residual franchise-wide shortage escalates to #procurement as an RFQ.
   Supplier agents bid with unit price and lead time; the lowest landed cost wins and becomes a
   single purchase order for one human approval. This is the step that makes the system a decision
   layer rather than a ledger: the group buys once, for what it genuinely does not have.

6. CLEAR SURPLUS. In parallel, near-expiry stock that no branch needs is converted into a menu
   promotion so it clears through demand instead of being written off.

Why a mesh and not a solver. Each site holds its own local state and its own constraints, and the
question "who can cover this, at what cost, before it spoils" is naturally a negotiation between
holders rather than a single global optimisation. It also degrades correctly: a node that is offline
simply does not claim, and the shortage still reaches procurement.

Implementation. Coordination runs on Cotal (agent nodes, presence, channels, anycast). Reasoning
runs as six capabilities — weekly_forecast, rebalance_and_procure, promotion_sweep,
consumer_concierge, inventory_admin, menu_intelligence — exposed over an MCP bridge that mesh nodes
call as tools, so the coordination layer and the reasoning layer stay separable. Shared state
(inventory, transfers, RFQs, bids, purchase orders, forecasts) lives in Postgres. The
multi-constraint rebalance and procurement decision runs on Claude Opus 5; forecasting and bulk
extraction route to open-weights models on Nebius.

Worked example, from the live system. Downtown is 36 kg short of tomatoes. Marina holds 34 kg
against a par of 24, expiring in two days. Mission holds 16 kg but is itself below par, so it does
not claim. Marina's claim wins; 10 kg moves branch to branch at zero purchase cost, rescuing stock
that would have spoiled. Only the net 26 kg reaches procurement, where two suppliers bid — Bay Foods
at $2.05 beats NorCal at $2.20 — producing one $53.30 purchase order for the owner to approve. One
shortage in, one decision out.
```
