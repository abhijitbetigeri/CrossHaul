# Mise — team

**Abhijit Betigeri, solo founder.** One person today, with a dated plan for the next eleven.

---

## The case, stated directly

The strongest argument is not the résumé. It is that this exact product has already been built,
already been built and deployed — in July 2026, as
[SC-Intelligence](https://github.com/abhijitbetigeri/SC-Intelligence). Today's repository extends
that system rather than introducing it. A panel is not being asked to believe a solo founder *could*
ship this. It already shipped, and the mesh is live at a URL.

The second argument is fit. Mise is not a restaurant product with a software layer bolted on. It is
a distributed coordination problem — branches holding inconsistent local state, an anycast search
for surplus, agents negotiating a transfer, and one reconciled purchase order surfacing to a human.
That is the founder's actual training. The 2014 foundation is NDN simulation on NS-3, SDN,
Emulab, and a JOS hypervisor with a virtualisation benchmark. When the deck claims branches can be
made to coordinate, it is a claim this founder has implemented before, in the layer where such
claims are hard.

The third is that solo is a stage, not an identity. The financial model already carries a second
person in year 1, six in year 2, twelve in year 3. Those seats are named below.

---

## Velocity: what roughly 16 projects in four months proves

| Period | Output | Cadence |
|---|---|---|
| May 2026 – Sep 2026 | ~16 shipped projects | one every 1–2 weeks |

Shipped means a deployed site or a runnable repository, generally with a voiceover demo video, a
before/after table, and real terminal output rather than mockups.

**What it demonstrates.**

- **Scope control under a hard deadline.** Sixteen finishes in four months is mostly a scoping skill.
  Someone who cannot cut scope produces two finishes and fourteen abandoned branches.
- **Time-to-competence in an unfamiliar stack.** The range is wide on purpose: Unitree G1 locomotion
  on ice and snow, a G1 PPO policy in MuJoCo with an LLM failure-diagnosis loop, SO-101 arm
  teleoperation, ExecuTorch running offline on a Galaxy S25 Ultra with a CPU/NPU toggle for
  air-gapped sites, an agent sandbox enforcing signed capability manifests and 3-of-5 peer signatures
  for irreversible actions.
- **Reading other people's systems critically.** In Isaac Lab's G1 configuration, static friction min
  equals max — one surface for the whole of training — while quadruped Spot in the same tree gets
  proper randomisation. That is a benchmark defect, not a preference. The same instinct produced a
  measured 56% null-rate data-contract defect, which is what an incident-response pipeline (alert →
  triage → automated fix → human gate → re-verify) was then built around. Mise's hardest real-world
  surface is dirty POS and invoice data. This is the relevant muscle.
- **Problem reframing.** Agent memory treated as a *ranking* problem rather than a storage problem,
  with an adversarial corpus in which stale entries run about 3× longer, so BM25 and embeddings both
  prefer the wrong answer on merit.

**What it does not demonstrate, and should not be claimed.** Nothing here is evidence of retention,
of a system maintained across years, of working inside a team, of managing anyone, or of a customer
paying money. Sixteen projects in four months is also compatible with an inability to stay on one
thing. The counter-evidence is this product specifically: built in July, returned to in September,
and the September work is the commercial case — market sizing, a cohort financial model, unit
economics — not another prototype. Depth is being demonstrated now, and is fairly judged as
in-progress rather than proven.

---

## Domain credibility

| Claim in the deck | What backs it |
|---|---|
| Agents can coordinate a multi-branch restock | Built and deployed July 2026, the same product |
| Distributed coordination is tractable at 3–20 branches | NDN/NS-3, SDN, Emulab, JOS hypervisor — the 2014 foundation |
| Forecast → BOM explosion → net shortage is a real pipeline | Six Runtype capabilities and an InsForge Postgres schema, live |
| Physical AI is the extension, not a slogan | [Project-SCIM](https://github.com/abhijitbetigeri/Project-SCIM), a Unity 6 back-of-house simulation in which a robot executes the transfer and emits demonstration data |

The gap this founder does *not* have is the technical one. It is stated plainly further down.

---

## Hiring plan

The model is the constraint. Year 1 opex is $210K, year 2 is $860K at 6 people, year 3 is $1.85M at
12 people, with two account-executive seats carried from month 13. Every hire below fits inside
those envelopes; none of it requires re-running the model.

### Hire 1 — Founding engineer, data and forecasting. Month 3.

| | |
|---|---|
| Role | Own the per-SKU demand forecast and the ingestion layer beneath it |
| Unlocks | POS and invoice ingestion at production quality, which is the single dependency every other claim rests on. The forecast is what makes Mise a decision system rather than the bookkeeping MarketMan and Restaurant365 already ship. It is also the thing the founder is slowest at doing alone and to a standard. |
| Profile | 4–8 years, time-series or demand forecasting in a messy-data domain — retail, logistics, grocery. Ships to production, not to notebooks. |
| Cost | ~$110K cash, ~$125K fully loaded |
| Equity | 1.5–3.0%, four-year vest, one-year cliff |
| Trigger | Signed at close of the pre-seed; starts month 3 |

Year 1 reconciliation to the modelled $210K: founder ~$75K fully loaded, engineer ~$125K fully
loaded, ~$10K non-payroll (hosting, inference, incorporation, accounting). Both salaries are below
San Francisco market, deliberately and visibly — that is what $210K actually buys, and the offer is
cash-light and equity-heavy to compensate. If that offer does not close, the fallback is a later
start at a market band rather than a worse hire; year-1 recognised revenue is only $107K, so the
schedule can absorb a three-month slip without moving the month-24 ARR milestone.

### Hire 2 — Account executive, mid-market restaurant groups. Month 13.

| | |
|---|---|
| Role | Take over the selling the founder does in year 1 |
| Unlocks | The entire year-2 and year-3 growth curve. 16 → 58 → 167 groups is not a founder-led number; the model attributes it to two AEs at roughly 5 groups/month each, which is ordinary mid-market productivity at a $19K ACV. |
| Profile | Has sold restaurant or hospitality technology into 3–20 unit operators. Knows the buyer is a procurement manager, not a CTO, and that the deal is closed in a walk-in, not a conference room. |
| Cost | ~$90K base / ~$180K OTE, inside the two AE seats the model already carries from month 13 |
| Trigger | Founder-led selling must have closed year 1's ~16 groups first. If it has not, the problem is the product or the price, and hiring a seller hides that rather than fixing it. |

Sequencing note: the model funds both AE seats from month 13. The intent is to fill AE #1 at month
13 and AE #2 at month 15, once the first has closed, which spends slightly under the modelled line
rather than over it.

### The rest of the plan

| | Headcount | Opex | Added that year |
|---|---:|---:|---|
| Year 1 | 2 | $210K | Founding engineer (data/forecasting) |
| Year 2 | 6 | $860K | 2 AEs from month 13; integrations engineer (Toast, Square, broadline distributor EDI); implementation and customer success lead |
| Year 3 | 12 | $1.85M | 3 engineering (2 platform/integrations, 1 ML), 1 sales lead, 2 customer success |

Sanity check: $860K over 6 people is ~$143K average fully loaded; $1.85M over 12 is ~$154K. Neither
is a number that requires explaining away.

The third-year customer-success weighting is deliberate. Gross margin is modelled at 84% with COGS
falling from $60 to $40 per location per month, and a material share of that is human support. At
1,083 locations, support is a staffing line, not a footnote.

---

## Advisors to recruit

Two, both operating rather than ornamental, both targeted before the pre-seed closes.

**A multi-unit restaurant operator, 5–20 locations, ideally multi-concept.** Needed because the
financial model's honest weakness is zero customer discovery: no operator has yet said they would
pay $249 per location per month. An operator advisor converts that from an unanswered question into
a tested one, and tells the founder which of the six Runtype capabilities an operator would actually
open on a Tuesday. *Route:* the three Bay Area multi-unit groups already named as the next step for
letters of intent — the first one that engages seriously is the advisor candidate. Local California
Restaurant Association chapters and the Founder Institute mentor network are the second and third
routes.

**A food distribution executive — broadline (Sysco, US Foods, Performance) or a strong regional.**
Needed because Mise's output is a purchase order, and the person who knows what a distributor will
accept, how order minimums and delivery windows actually bind, and whether inter-branch transfers
threaten or help the rep's book, is worth more than any amount of desk research. This advisor also
de-risks the channel question: distribution reps are a plausible route to market. *Route:* start
with the district sales reps calling on the target groups and work upward to their managers.

*Terms:* 0.25–0.50% each, two-year vest, one-year cliff, on a standard FAST-style agreement.
A monthly call and one introduction per quarter is the actual ask. Anyone unwilling to commit to
that is a logo, and a logo on an advisor slide is worth nothing to this panel.

---

## The honest gaps

| Gap | Why it matters | Mitigation, and its limit |
|---|---|---|
| No restaurant industry operating experience | Every assumption about how a kitchen actually runs is inferred from industry data, not lived | Operator advisor, then customer discovery. Neither is done yet. |
| No enterprise or mid-market sales experience | Year 1 is entirely founder-led selling, by someone who has never carried a quota | AE at month 13 — but year 1 has to be survived first, and that is genuine execution risk |
| Zero customer discovery | $249/location/month is derived from competitor comparables, not from anyone agreeing to pay it | Three Bay Area groups, LOIs, pricing tested against real procurement managers before the number is treated as fact |
| Has never hired or managed | Year 2 goes from 2 people to 6 | Nothing yet offsets this. The first hire is the test. |
| Bus factor of one | The entire system lives in one head today | Partly why the founding engineer is hire 1 and starts in month 3 |
| No multi-year maintenance record | Sixteen projects in four months is not evidence of anything surviving eighteen months | Honestly, none. It will be demonstrated or it won't. |

Naming these is not modesty. A panel that has seen thousands of pitches will find them in ten
minutes of diligence, and finding them after the founder has already listed them is a very different
conversation from finding them instead.

---

## Why me — the spoken line

> I am
> not a restaurant person. I am a distributed systems person, and a group whose twelve branches
> cannot see each other's inventory has a coordination problem, not a cooking problem. I know what I
> am missing — an operator and a seller. Both are hires, both are dated, both are in the model. The
> coordination layer already works.

*(76 words)*
