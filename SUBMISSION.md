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
| Prior system (July) | https://github.com/abhijitbetigeri/SC-Intelligence |

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

- **`product/`** — the July 2026 system (SC-Intelligence, AGI Summit winner): the coordination mesh,
  six agent capabilities, the Postgres schema and the hosted UI. Pre-existing. See
  [`product/PROVENANCE.md`](product/PROVENANCE.md).
- **Everything else** — built 19 Sep 2026. The repository was created at 11:26 that morning and
  every commit is timestamped that day: the platform thesis, market research, the financial model,
  go-to-market, competitive analysis, the physical-AI feasibility study, the ElevenLabs voice
  channel, and the Nebius inference router.

The July system proved agents *can* coordinate a restock. It had no answer for the only question an
operator actually asks: **what is that worth, and what does it cost me?** That is what today built.
