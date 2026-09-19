# Mise — market research

Compiled 19 Sep 2026. Every figure is either **sourced** (linked) or **constructed** (an estimate
built from sourced inputs, with the arithmetic shown). The distinction is marked throughout,
because a model whose assumptions are visible survives questioning and one whose assumptions are
hidden does not.

---

## 1. TAM — four layers, narrowing

Analysts disagree by definition boundary, so the honest move is to show the layers rather than
pick the flattering number.

| Layer | What it measures | Size | Source |
|---|---|---|---|
| **0 — Industry backdrop** *(not a market)* | Global food service spend | $3.44T (2025) → $3.60T (2026) | [Statista](https://www.statista.com/statistics/1095667/global-food-service-market-size/) |
| **1 — All restaurant software** | Every category, POS included | $8.13B (2026) → $29.92B (2034), 17.7% CAGR | [Fortune Business Insights](https://www.fortunebusinessinsights.com/restaurant-management-software-market-116505) |
| **2 — The actual category** | Restaurant inventory management & purchasing | **$4.55B (2025) → $9.18B (2030), 15% CAGR** | [Research and Markets](https://www.researchandmarkets.com/reports/5533246/restaurant-inventory-management-and-purchasing) |
| **3 — Adjacent** | Food supply chain management software | $3.05–4.85B (2025), ~6% CAGR | [Bosson Research](https://www.marketresearch.com/Bosson-Research-v4252/Global-Food-Supply-Chain-Management-44584230/) |

**Layer 2 is the TAM to quote: $4.55B growing to $9.18B by 2030.**

A second, corroborating estimate at $3.1B (2024) → $7.5B (2033) at 10.5% CAGR appears in
[Verified Market Reports](https://www.verifiedmarketreports.com/product/restaurant-inventory-management-software-market/) —
same order of magnitude, different methodology.

### Bottom-up triangulation *(constructed)*

Quoting an analyst figure alone is weak; deriving the same number independently is what makes it
credible.

```
  ~750,000  US restaurant locations                    [sourced]
×    $249   per location per month                     [constructed — see §3]
×      12   months
= $2.24B/yr  US-only, full penetration
```

US locations: [CKitchen / NRA, 2026](https://www.ckitchen.com/blog/2026/2/how-many-restaurants-are-in-the-u-s-2026.html)
(broader definitions reach [1M+ foodservice outlets](https://get.apicbase.com/restaurant-industry-statistics/)).

A US-only bottom-up of $2.24B against a global category of $4.55B is internally consistent — the US
is roughly half the addressable software spend. **Two independent methods agreeing is the point.**

---

## 2. SAM and beachhead

### SAM — US multi-unit locations *(constructed)*

Single-site restaurants have no coordination problem. The product only means anything at 2+
locations, so the addressable set is the multi-unit population.

```
   750,000  US locations
×      30%  chain / multi-unit share                   [sourced]
=  225,000  addressable locations
×   $2,988  per location per year
=   $672M/yr  US SAM
```

Multi-unit share: [~70% of US restaurants are independent](https://www.gofoodservice.com/blog/independent-vs-chain-restaurants-an-uphill-battle)
(NRA). In full-service specifically, independents hold [78.6%](https://www.mordorintelligence.com/industry-reports/united-states-full-service-restaurants-market) —
so 30% is the generous end of the multi-unit estimate and should be presented as such.

### Beachhead — operators running 3–20 units

This is the wedge, and the supporting data is unusually good:

- **[63.5% of multi-concept companies operate fewer than 20 locations](https://restaurantchains.net/multi-concept-restaurant-operators-emerging-chains/)**, and the median operator runs 3 concepts, 13 units, across 2 states. The mid-market is the market.
- **[3,381 planned locations documented across the 1→2 through 18→19 unit transitions in 2026](https://www.restaurantnews.com/restaurant-growth-in-2026-extends-from-second-locations-to-19-units-080326/)** — operators are crossing into multi-site *right now*.
- Within that, [the 5–19 unit cohort accounts for 1,136 records and 33.6% of measured growth transitions](https://restaurantdata.com/new-weekly-alerts-2026-emerging-restaurant-growth-report/).

**This is the Why Now, with evidence.** The moment an operator opens a third location they acquire
a coordination problem they have never had before — and the tool that solves it is priced for
50-unit chains.

---

## 3. Competitive landscape

| | Position | Pricing | Source |
|---|---|---|---|
| **Restaurant365** | Category leader — $445M raised, $1B valuation, ~$132M ARR, 40K customers | Enterprise, custom | [Latka](https://getlatka.com/companies/restaurant365) |
| **Crunchtime** | Built for 50+ location chains | Custom, thousands/mo | [RIT](https://restaurantinventorytools.com/best-inventory-software-multi-location-restaurants/) |
| **MarketMan** | Mid-market incumbent | $199/loc/mo + $500 setup | [RIT](https://restaurantinventorytools.com/restaurant-inventory-software-cost/) |
| **Square × MarketMan** | Entry tier | $99/loc/mo | [Square](https://squareup.com/us/en/inventory-management/restaurants) |

Typical category pricing runs [$100–$500 per location per month](https://restaurantinventorytools.com/restaurant-inventory-software-cost/).

That R365 reached $1B and $132M ARR settles "is this a real market." It does not settle "is there
room" — which is the next section.

### ⚠️ The differentiation claim, stated correctly

**MarketMan and Restaurant365 already ship inter-location transfers.** Any pitch claiming otherwise
is false and will be caught:

- [MarketMan's inter-location transfer records items sent between restaurant sites, updating both locations automatically](https://www.marketman.com/platform/multi-unit-restaurant-commissary-kitchen-inventory-software) — on the **Enterprise** plan.
- [Restaurant365 connects commissary operations with kitchens and stores](https://www.restaurant365.com/inventory/commissary/).

The real difference is **who decides**:

| | Incumbents | Mise |
|---|---|---|
| Who initiates | A human notices the imbalance | The system detects it |
| What the software does | Records the move, reconciles counts | Forecasts the shortage, locates the surplus, matches them, proposes the transfer |
| When | After someone notices | Before anyone notices |
| Data model | Human-initiated transactions, periodic counts | Continuous per-SKU demand forecast |

Their feature is **bookkeeping for a decision already made.** Mise *is* the decision. That framing
is defensible under questioning, and it explains why copying it is not a feature ticket — it
requires a forecasting substrate their architecture doesn't have.

**Second gap: the Enterprise gate.** MarketMan restricts transfers to Enterprise. A six-location
operator therefore cannot buy the capability at mid-market pricing from the mid-market incumbent.
That is a pricing-shaped hole in exactly the beachhead segment.

---

## 4. Pricing *(constructed)*

**$249 / location / month.**

Positioned deliberately: a 25% premium over MarketMan's $199 mid-market tier, and far below the
enterprise tier that currently gates automated transfers. The premium is defensible because the
product sells decisions rather than record-keeping.

### The ROI argument

| | |
|---|---|
| Food waste per location per year | **~$72,000** ([USDA ERS via OysterLink](https://oysterlink.com/spotlight/restaurant-food-waste-statistics/)) |
| As share of food purchased | **4–10%** ([same](https://oysterlink.com/spotlight/restaurant-food-waste-statistics/)) |
| US industry-wide waste | **$162B/yr** ([Gitnux](https://gitnux.org/restaurant-food-waste-statistics/)) |

For a five-location group *(constructed)*:

```
  5 × $72,000  = $360,000/yr   waste exposure
×         15%  = $54,000/yr    recovered  [assumption — see below]
  5 × $2,988   = $14,940/yr    cost of Mise
              → $39,060/yr net, 3.6× return, ~3.3 month payback
```

**The 15% is an assumption and must be labelled one.** Mise cannot touch over-portioning, theft, or
prep loss — only the spoilage and stockout component visible in inventory data. Claiming a higher
recovery rate is where this model would stop being credible. Under-claiming here is deliberate.

---

## 5. Physical AI — feasibility assessment

Mise has a shipped embodied extension: [Project-SCIM](https://github.com/abhijitbetigeri/Project-SCIM),
a Unity 6 back-of-house simulation where a robot executes a rebalance transfer and every session
emits trajectory, pick/place and handoff data.

**Verdict: a Vision asset, not a product line. One slide, fifteen seconds, at the Vision beat — and nowhere else in the pitch.**

**Why not nearer term:**

- The core Mise loop is *inter-branch logistics* — 10kg of tomatoes crossing San Francisco. That is a van and a courier, not a manipulation problem. Robotics adds nothing to the economics of the thing the product actually does.
- Restaurant back-of-house is close to the hardest indoor environment for embodied AI: cluttered, wet, hot, hectic, dense with moving humans. Deployed food-service robotics today is confined to far easier problems — front-of-house running (Bear Robotics, Pudu) and fixed-station fry automation (Miso).
- Introducing robot capex into a pitch judged on **Business Model** and **Financial Projections** invites questions — deployment cost, payback, maintenance — that weaken a SaaS story with 80%+ gross margins.
- Project-SCIM's own README is candid that nothing is learned there; the robot follows a scripted task. Overclaiming against your own documentation is an avoidable risk.

**Why it still earns its slide:**

- **Impact & Vision is one of the eight scored criteria**, and this is a genuine five-year answer rather than a hand-wave: *Mise decides what moves; over time, robots execute it; every transfer logged today is the demonstration data that trains them.*
- It is **built and playable**, not speculative — evidence, which is rare on a Vision slide.
- It reframes the data asset. Every rebalance decision Mise records is simultaneously a labelled example of an embodied logistics task. That is a compounding-moat argument an investor understands: the dataset accrues from day one and cannot be bought.

**The line to use, and to stop at:** *"Every transfer Mise decides today is training data for the
robot that executes it tomorrow — we've already built the simulation where that happens."* Then move
on. It is a closing note, not an act.

---

## 6. Open items

- Crunchtime's transfer behaviour is unverified — whether it automates rebalancing or, like the others, records it. Worth five minutes before claiming the category is empty of decision automation.
- The 30% multi-unit share is the generous end of the range; full-service-only data suggests ~21%. SAM at the conservative end is ~$470M/yr.
- No customer discovery has been done. Zero operator interviews. The pain is sourced from industry data, not from a buyer who has said they would pay — and a judge may well ask.
