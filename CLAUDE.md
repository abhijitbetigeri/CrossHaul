# CrossHaul — working context

Handoff for any agent picking this up mid-stream. Written 19 Sep 2026, 13:50 PDT.

**Read this before touching anything.** Several numbers here were corrected once already after
research contradicted them; reintroducing the originals would put a false claim on a pitch stage.

---

## 1. What this is, and the clock

**CrossHaul** — a Common Operating Environment for multi-site inventory. One primitive: *forecast
demand per site, net it against what sister sites already hold, buy only the remainder.* Physical AI
is embedded in the sense that decisions are execution-aware (vans, distance, spare capacity), **not**
in the sense that we build robots.

Food service is the **beachhead**, not the ceiling. That vertical is called **Mise** and it is the
only one built.

**Event:** Dream AI Hackathon 2026, Frontier Tower, 995 Market St, San Francisco.

| | |
|---|---|
| Build window | 10:00–16:30 |
| **Stop building, start rehearsing** | **15:30** |
| Submit | **16:15** (deadline 16:30 — submit early) |
| Finalists present | 17:10 |
| Awards | 18:20 |

**Founder is solo.** Everything is founder-executed.

### The rubric — eight criteria, zero technical

Problem Solution Fit · Market Potential · Business Model · Go-To-Market Strategy · Team ·
Pitch Delivery · Financial Projections · Impact & Vision

**No criterion rewards engineering.** Code earns points only as evidence for a business claim. The
organisers pointed entrants at Sequoia's business-plan template and pitch deck, and the rubric maps
onto it almost one-to-one. Do not spend remaining time building.

### Reuse rule

Existing code may be reused if you state clearly what pre-dated the event. We satisfy this with a
**directory boundary**: `product/` is July, everything else is 19 Sep. Do not blur it.

---

## 2. Locked numbers — do not contradict these

Every document reconciles to these. If you change one, re-run `model/financial_model.py` and update
every doc that cites it.

| | |
|---|---|
| Price | **$249 / location / month** ($2,988/yr) |
| Avg group | 6.0 → 6.5 locations |
| Groups | Y1 **16**, Y2 **58**, Y3 **167** |
| Locations, end Y3 | **1,083** |
| Ending ARR | Y1 $288K · Y2 $1.08M · Y3 **$3.24M** |
| Gross margin | 76% → 81% → **84%** |
| CAC | $2,000 (Y1, founder-led) → $5,500 |
| **CAC payback** | **4.0 months** |
| **LTV/CAC** | **7.5×** (deliberately capped at 36 months) |
| Opex | $210K / $860K / $1.85M at 2 / 6 / 12 people |
| Raise | $1.5M pre-seed, ~34 months runway, $1.08M ARR at month 24 |
| Waste per location | ~$72,000/yr, 4–10% of food purchased |
| Recovery rate assumed | **15%** — do not raise it under pressure; its smallness is the credibility |
| Impact, Y3 | 931 tons food, ~4,740 t CO2e |
| TAM (category) | $4.55B (2025) → $9.18B (2030) |
| US SAM | ~$672M/yr, 225,000 multi-site locations |

---

## 3. Corrections already made — DO NOT REINTRODUCE

These were stated wrongly earlier in the session and fixed. They are the likeliest things to
regress.

**1. MarketMan pricing.** It is **Starter $249 / Growth $299 / Enterprise from $449** per location
per month, **free setup** — verified directly against marketman.com/pricing on 19 Sep 2026. It is
*not* $199 + $500 setup (that is stale third-party data still circulating in review sites).

Consequence: $249 is at **parity with their Starter tier**, not a 25% premium. That is the stronger
position — we deliver at their entry price the inter-location capability they gate to Enterprise at
~1.8×. There is no premium to defend.

**2. The architecture argument.** "Their transaction-and-periodic-count data model cannot produce a
per-SKU forecast" is **false**. Depleting theoretical on-hand from POS sales against recipe cards is
standard practice — it is what actual-vs-theoretical variance reporting *is*. A judge who knows the
category will say so.

The defensible version is three-part: no confidence interval on on-hand; no write-side network
object to optimise against; no above-store workflow surface. See `docs/competition.md` §6.1.

**3. "Nobody does inter-location transfers."** False. MarketMan, Restaurant365 and Crunchtime all
ship them. The true distinction is **deciding vs recording** — every transfer verb in Crunchtime's
own training catalogue is a human one (*create*, *request*, *process*, *reconcile*); none is *review
a proposed transfer*.

**4. Do not use "42% of restaurants use pen and paper."** Traced to an unattributed vendor blog with
no study behind it. The adoption argument rests on structure instead — see §5 below.

---

## 4. Current status

| Criterion | State |
|---|---|
| Problem Solution Fit | ✅ |
| Market Potential | ✅ |
| Business Model | ✅ |
| Financial Projections | ✅ |
| Go-To-Market | ✅ |
| Team | ✅ |
| Impact & Vision | ✅ |
| **Pitch Delivery** | ❌ **needs rehearsal — 1/8 of the score** |

**Built today, all committed:** platform thesis, market research, financial model, GTM, competition,
physical-AI feasibility, team, vision, ElevenLabs voice console (live), Nebius inference router
(live-verified).

**Not done:**
1. **The deck** — not started. ~45 min. The only thing between the founder and rehearsal.
2. **Fallback `.mp3`** — needs an ElevenLabs API key; 2 min. Insurance against venue wifi at 17:10.
3. **Rehearsal** — from 15:30, non-negotiable.

---

## 5. The arguments that actually win, and why

**The objection the founder keeps getting: "don't restaurants already have this software?"**
The 30-second answer is in `docs/competition.md` §8.1. Its spine: *partly yes, and the true part is
worth pressing on* — they all ship transfers, but as accounting. Then the buyer argument:

> Crunchtime runs 150,000 locations across 850 brands — 176 locations per brand. My buyer has nine.

**Adoption rests on structure, not surveys.** Crunchtime self-selects for 10+ unit brands with
$5K–50K implementations; R365 is quoted at $499–749/location; MarketMan gates transfers at 1.8×
entry. *A 9-unit group cannot buy Crunchtime economics and does not want R365's general ledger. That
is the buyer.*

**Why the platform breadth is credible.** In every sector the coordination layer *exists at
enterprise scale and does not exist at mid-market price.* SAP has run inter-plant stock transfer
orders for decades — a six-plant manufacturer does not run SAP. **One market, not five.**

**The GTM insight that shapes everything:** CrossHaul **cannot run a single-location pilot** — one
site has no counterparty. Minimum deployment is a 2–3 site cluster, so the land is $8,964 ARR, never
one seat. This removes the standard vertical-SaaS land motion and forces the wedge.

**The wedge:** a paid, read-only **Cross-Branch Waste Audit** ($500 founding → $2,500, credited
against implementation) producing a *retro-transfer ledger* from the operator's own invoices. Needs
no new engineering, and doubles as the customer discovery the model names as its weakness.

**The kill criterion, stated openly:** if the median retro-transfer ledger comes back under ~$8,000
per location per year, the ROI collapses and nothing else matters. Ten audits answer it by day 90.

**Physical AI — one slide, fifteen seconds, at the Vision beat only.** The strongest honest line:

> CrossHaul is a beneficiary of transport and warehouse autonomy, not a producer of it. When an
> intra-city 10 kg drop costs $2 instead of $7, every marginal transfer turns positive. All of the
> upside, none of the capex.

Do not say: robots in kitchens, "the robot learned", digital twin, sim-to-real. Project-SCIM's own
README says nothing is learned and the robot follows a scripted task — contradicting your own public
documentation is fatal. Full do/don't table in `docs/vision.md` §7.

---

## 6. Known weaknesses — name them before a judge does

- **Zero customer discovery.** Nobody has agreed to pay $249. Pricing comes from competitor
  comparables, pain from industry data. The credible answer is naming the next step, not bluffing.
- **A single-item transfer is economically marginal.** $20–41 of value against $5–10 courier or
  $22–35 own-staff. The answer is batching and routing onto trips that already exist (~$0 marginal).
  Worked in `docs/physical-ai.md` §4.2.
- **The data-moat claim is half true.** "Every rebalance decision is a labelled embodied-logistics
  example" holds for task *specification*, not embodied *behaviour* — 1,000 locations for a year is
  ~73 MB and zero state-action pairs. Prepared answer in `docs/physical-ai.md` §5.6.
- **Beachhead geography is contested.** Own bottom-up finds ~150 qualifying Bay Area groups against
  a funnel needing ~430. Drives the month-6 widening to Sacramento and LA.
- **Count discipline is the quiet killer.** If operators' on-hand numbers are unreliable, CrossHaul
  proposes transfers against fiction. It fails at pilot *looking like a sales problem*.
- **Solo founder, never hired or managed.** Stated plainly in `docs/team.md` with no mitigation
  claimed.

---

## 7. Where everything lives

**Repo:** https://github.com/abhijitbetigeri/CrossHaul (public). Local clone is still at
`~/projects/mise` — directory name is cosmetic, the remote is correct.

```
CLAUDE.md                  this file
README.md                  platform framing + reuse disclosure
docs/platform.md           the COE thesis, sector map, physical-AI placement
docs/market-research.md    TAM/SAM/beachhead, competition, pricing
docs/competition.md        the incumbent objection + rebuttal script  ← highest-value doc
docs/financial-model.md    P&L, unit economics, assumption defences
docs/go-to-market.md       beachhead filters, wedge, 90-day plan, 7 falsifiers
docs/physical-ai.md        feasibility analysis, incl. negative findings
docs/team.md               solo-founder case, hiring plan, honest gaps
docs/vision.md             impact quantified, physical-AI bounded, what-not-to-say
docs/elevenlabs-integration.md
model/financial_model.py   monthly cohort model — all inputs at the top
inference/router.py        Nebius + Claude routing, with live check
voice/                     console.html (deployed), agent-prompt.md, render_fallback.sh
product/                   the July system, vendored — PRE-EXISTING, see PROVENANCE.md
```

**Live URLs** (InsForge, deployed from `~/projects/agisummit/web/`, not from this repo):

| | |
|---|---|
| Landing | https://k3trn3a2.insforge.site |
| Mesh Console | https://k3trn3a2.insforge.site/mesh.html |
| Branch Operations | https://k3trn3a2.insforge.site/branch.html |
| Market Intelligence | https://k3trn3a2.insforge.site/market.html |
| **Voice Console** | **https://k3trn3a2.insforge.site/voice.html** |

To redeploy: `cd ~/projects/agisummit && npx @insforge/cli deployments deploy web`. Copy any changed
`voice/console.html` to `~/projects/agisummit/web/voice.html` first — that project holds the
InsForge link, this one does not.

**Related repos:** [SC-Intelligence](https://github.com/abhijitbetigeri/SC-Intelligence) (the July
system) · [Project-SCIM](https://github.com/abhijitbetigeri/Project-SCIM) (Unity 6 embodied sim).

⚠️ An older `github.com/abhijitbetigeri/mise` repo still exists with identical early history. Delete
or archive it — two public repos with the same content confuses a judge who finds both.

### Credentials — locations, never values

| | |
|---|---|
| Nebius | `~/projects/syntropimaxx/.env` → `NEBIUS_API_KEY`. Works on both `api.studio.nebius.com/v1` and `api.tokenfactory.nebius.com/v1`. |
| ElevenLabs agent id | `agent_9301m2xnptxgezd9mtebyh2p4ezm` — **public by design**, already in `voice/console.html` |
| ElevenLabs API key | **Not yet obtained.** Only needed for `voice/render_fallback.sh`. |
| InsForge | `~/projects/agisummit/.insforge/` — gitignored, never vendor it |

**Never commit key material.** Scan the staged diff before every commit. The `ct_live_*` Persona
tokens inside `product/` are publishable browser tokens and are fine.

---

## 8. ElevenLabs — current configuration

Agent **CrossHaul**, published. Authentication **off**; allowlist `k3trn3a2.insforge.site`; **Fail
when Origin header is missing** ON; all overrides off. That is the intended public-widget posture —
the embed needs only the public agent id, no key reaches the browser, and the worst an abuser gets
is our own call minutes.

Creator plan: **275 agent minutes/month, 10 concurrent calls** — quota is not a constraint; venue
wifi is. Hence the two-path design: recorded `.mp3` for the stage, live agent for the judges' table.

**Known trap:** a find-and-replace on the placeholder `AGENT_ID_HERE` also rewrote the guard that
*checks* for the placeholder, inverting it so the widget stayed hidden with a valid id in place. The
guard now tests `/^agent_/`. Don't reintroduce a literal comparison.

---

## 9. Nebius — the argument, not the integration

Routing by reasoning complexity: high-volume, low-reasoning calls (forecasting, bulk extraction) go
to open-weights models on Nebius Token Factory; the multi-constraint rebalance decision stays on
`claude-opus-5`. **$5.16 → $0.88 per location per month, 83% removed** — verified live.

**State the limit honestly:** inference is *not* the dominant cost-of-revenue line — customer success
is. Routing contributes ~21% of the modelled $60 → $40 reduction. Claiming it carries the whole
margin story will not survive a question.

---

## 10. If you are picking this up now

1. **Do not build.** Zero of eight criteria reward it. Everything needed is committed.
2. **Write the deck** if it still doesn't exist — ten slides on the Sequoia spine, each mapped to a
   scored criterion. Numbers come from §2 of this file; do not recompute them.
3. **Protect the 15:30 rehearsal.** Pitch Delivery is worth as much as Business Model, and the
   founder has never pitched. Four run-throughs aloud, minimum.
4. **Submit at 16:15**, not 16:30.
5. When you correct something, correct it *everywhere* and note it in §3 here. The docs cross-cite
   heavily and a half-applied correction is worse than none.
