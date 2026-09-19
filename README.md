# CrossHaul

### The Common Operating Ecosystem for Supply Chain Intelligence, with Physical AI

**Forecast demand. Rebalance stock. Reduce waste. Then buy.**

Every site in a multi-site operation forecasts alone, orders alone, and writes off alone. There is no
shared picture of what the business is holding — so one branch buys what another is days away from
discarding. CrossHaul gives the group one operational picture and one decision on top of it.

**Dream AI Hackathon 2026** · Frontier Tower, San Francisco · 19 September 2026

---

## Start here

| | |
|---|---|
| 🎤 **Pitch deck** | https://claude.ai/code/artifact/8781c258-bcc0-447e-83a9-d4eb99fae94e |
| 🖥️ **Live product** | **https://k3trn3a2.insforge.site** |
| ☎️ Voice approval channel *(ElevenLabs)* | https://k3trn3a2.insforge.site/voice.html |
| 🔀 Agent mesh negotiating a shortage | https://k3trn3a2.insforge.site/mesh.html |
| 📋 Site operations console | https://k3trn3a2.insforge.site/branch.html |
| 📊 Market intelligence | https://k3trn3a2.insforge.site/market.html |
| 🤖 **Playable robot simulation** | https://abhijitbetigeri.github.io/Project-SCIM/sim/ |

**Try this first:** open the [voice console](https://k3trn3a2.insforge.site/voice.html) and press
*Talk to CrossHaul*. The system states a decision it has already made and asks for approval — that is
the product, in fifteen seconds.

---

## What it does

**One primitive, stated once:** forecast demand per branch, net it against what other branches of the
same franchise already hold, and send a supplier only the remainder — as one purchase order, for one
human approval.

```
   READS                        DECIDES                      ACTS
   ─────────────────────        ──────────────────────       ──────────────────────────
   Sales      POS API      ┐    1  Forecast per branch   ┐    Transfer proposed
   Recipes    BOM          ├──▶ 2  Explode through BOM   ├──▶   → donor taps accept
   Prices     Invoices     │    3  One franchise position│    Purchase order drafted
   On hand    Their counts ┘    4  Match surplus↔shortage│      → owner releases it
              + confidence      5  Tender the remainder  ┘    Dated stock marked down
                                                              And it calls you
```

Everything on the left already exists in the business. **Nothing moves without a person tapping
accept.**

### Multi-agent coordination, no central planner

Each branch and supplier is a node on a mesh with presence and shared channels (`#demand`,
`#rebalance`, `#procurement`, `#promotions`, `#decisions`). A shortage is **anycast** to whoever
holds surplus; holders claim competitively — nearest branch first, nearest-expiry lot first, so the
stock most at risk of being written off moves first. Only the residual franchise-wide shortage
becomes an RFQ, suppliers bid, and the lowest landed cost becomes one PO.

*Worked example, live:* Downtown is 36 kg short. Marina holds 34 against a par of 24, expiring in two
days. Mission is itself below par so it does not claim. Marina wins — 10 kg moves at zero purchase
cost, rescuing stock that would have spoiled. Only the net 26 kg reaches procurement, where Bay Foods
at $2.05 beats NorCal at $2.20: **one $53.30 purchase order, one approval.**

---

## How the sponsor tools are used

### ElevenLabs — the approval channel, not a voiceover

The failure mode of this category is not features. It is that the person who owns the stock is on
their feet all day and never opens a dashboard. So CrossHaul **calls them**:

> *"Downtown is thirty-six units short for the weekend. Marina is ten over par on a lot that expires
> in two days, so I moved those across on a vehicle already running the route — no purchase, no
> write-off. The remaining twenty-six went to RFQ and Bay Supply won it at two-oh-five a unit.
> Fifty-three thirty. Want me to release it?"*

A published conversational agent is embedded in the product ([try it
live](https://k3trn3a2.insforge.site/voice.html)); text-to-speech renders the same call to disk so a
demo cannot fail on venue wifi. Authentication off, domain allowlisted, origin check on — no key
reaches the browser. → [`voice/`](voice/) · [`docs/elevenlabs-integration.md`](docs/elevenlabs-integration.md)

### Nebius — routing by reasoning complexity

Sending every call to a frontier model is the same mistake as running every query on your largest
database instance.

| Call class | Reasoning | Routed to | All-frontier | Routed |
|---|---|---|---:|---:|
| Demand forecast | low | **Nebius** | $3.015 | $0.046 |
| Market intelligence | low | **Nebius** | $0.600 | $0.010 |
| Promotion sweep | low | Haiku 4.5 | $0.108 | $0.022 |
| Operator dialogue | medium | Sonnet 5 | $1.050 | $0.420 |
| Rebalance + procurement | **high** | Opus 5 | $0.385 | $0.385 |
| **Per location / month** | | | **$5.16** | **$0.88** |

**83% of inference cost removed — and the one call that decides how money gets spent stays on the
frontier model.** Verified live against Nebius Token Factory (`openai/gpt-oss-120b`): the forecast
call cost **$0.000083** against **$0.006580** frontier, a 79× difference on a call needing no
judgement. → [`inference/router.py`](inference/router.py), run it with `--live`

*Stated honestly: inference is not the dominant cost-of-revenue line — customer success is. Routing
contributes about a fifth of the modelled $60 → $40 per-location reduction.*

---

## The business case

| | |
|---|---|
| Buyer | Multi-site operator, 3–20 locations, clustered within driving distance |
| Pain | ~$72,000 per site per year; 4–10% of everything purchased |
| Price | $249 / location / month — **parity with MarketMan's Starter tier**, which gates inter-location transfers to Enterprise at $449 |
| Return to the customer | $10,800 recovered against $2,988 paid — **3.6×** |
| Category TAM | $4.55B (2025) → $9.18B (2030) · US SAM ~$672M/yr |
| Year 3 | $3.24M ARR · 84% gross margin · 4.0-month CAC payback · 7.5× LTV/CAC |

**Documents, in reading order:**

| | |
|---|---|
| [`docs/platform.md`](docs/platform.md) | The Common Operating Environment thesis, the four conditions, the sector map, and where physical AI genuinely sits |
| [`docs/market-research.md`](docs/market-research.md) | Layered TAM with an independent bottom-up triangulation, SAM, the beachhead, pricing |
| [`docs/competition.md`](docs/competition.md) | *"Don't they already have this?"* — capability matrix, adoption reality, rebuttal script, seven ranked threats |
| [`docs/financial-model.md`](docs/financial-model.md) | Three-year P&L, unit economics, and a defence for every assumption |
| [`docs/go-to-market.md`](docs/go-to-market.md) | Beachhead filters, the paid waste-audit wedge, 90-day plan, **seven falsifiers with test dates** |
| [`docs/physical-ai.md`](docs/physical-ai.md) | Feasibility analysis — including the negative findings |
| [`docs/vision.md`](docs/vision.md) | Impact quantified: 931 tons of food, ~4,740 t CO2e at year 3 |
| [`docs/qa-prep.md`](docs/qa-prep.md) | The questions this project gets asked, and the honest answers |
| [`model/financial_model.py`](model/financial_model.py) | The model itself — every figure derives from one inputs block |

Two things named openly rather than buried: **there has been no customer discovery** — nobody has
agreed to pay $249 — and **a single-item transfer is economically marginal** at courier prices, which
is why batching onto trips that already exist is the lever. Both are worked through in the docs.

---

## What existed before today, and what was built during the event

Per the hackathon's reuse rule — **the boundary is a directory.**

**Pre-existing** — [`product/`](product/), built July 2026 as
[SC-Intelligence](https://github.com/abhijitbetigeri/SC-Intelligence), winner of the AGI Summit
hackathon: the coordination mesh, six agent capabilities, the Postgres schema and the hosted UI. See
[`product/PROVENANCE.md`](product/PROVENANCE.md).

**Built 19 September 2026** — everything else. This repository was created at **11:26 that morning**
and every commit is timestamped that day:

- [`voice/`](voice/) — the ElevenLabs approval channel, live in the product
- [`inference/router.py`](inference/router.py) — the Nebius routing layer, verified against the live API
- [`docs/`](docs/) + [`model/`](model/) — the entire commercial case
- [`deck/`](deck/) — the pitch deck source

> The July system proved agents *can* coordinate a restock. It had no answer for the only question an
> operator actually asks: **what is that worth, and what does it cost me?** That is what today built.

---

## Running it

```bash
python3 model/financial_model.py          # the three-year model
python3 inference/router.py --live        # the Nebius routing cost model (needs NEBIUS_API_KEY)
./voice/render_fallback.sh                # render the voice clip (needs ELEVENLABS_API_KEY)
```

Secrets go in `.env` — see [`.env.example`](.env.example). Nothing in this repository contains a key.

## Related

| | |
|---|---|
| [SC-Intelligence](https://github.com/abhijitbetigeri/SC-Intelligence) | The July system — agent mesh, capabilities, backend, UI |
| [Project-SCIM](https://github.com/abhijitbetigeri/Project-SCIM) | Physical-AI extension — Unity 6 simulation where a robot executes the transfer and emits the task record |
| [`SUBMISSION.md`](SUBMISSION.md) | Submission details and sponsor-tool write-ups |
| [`CLAUDE.md`](CLAUDE.md) | Working context — locked numbers, corrections, known weaknesses |
