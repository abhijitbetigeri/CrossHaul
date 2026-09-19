# CrossHaul — a Common Operating Environment for multi-site inventory

## The problem, stated once, for every sector

A company with *N* sites runs *N* independent inventory ledgers. Each site forecasts alone, orders
alone, and writes off alone. There is no shared operational picture, and no mechanism to act on one
if there were.

So site four buys what site seven is three days from throwing away.

This is not a food problem. It is the structure of every multi-site operation holding stock that
dates.

## What "Common Operating Environment" means here

The term is borrowed from defence, where it means one thing: **every unit sees the same picture, and
decisions are made against the position of the whole force rather than the position of one unit.**

Applied to physical inventory, that reduces to a single operation:

> **Forecast demand per site, net it against what sister sites already hold, and buy only the
> remainder.**

Everything else — recipes, production schedules, category hierarchies — is sector-specific
decoration sitting on top of that primitive. The primitive itself does not care what is in the
crate.

## The four conditions

CrossHaul applies wherever all four hold at once:

1. **Multiple sites under one owner** — otherwise there is no counterparty
2. **Perishable or dated stock** — otherwise waiting costs nothing
3. **Site-level demand that varies independently** — otherwise every site is short at the same time
4. **A transfer that costs less than a purchase** — otherwise the arithmetic never clears

## Why this is one platform and not five products

What changes between sectors is the demand model and the unit of stock. The netting logic, the
network position, and the approval surface do not.

| Sector | Stock that dates | Sector-specific layer | Status |
|---|---|---|---|
| **Food service** | Ingredients, shelf life in days | Recipe bill-of-materials | **Built and live** |
| FMCG manufacturing | Raw materials, WIP, batch expiry | Production schedule + BOM | Adjacent — structurally the same shape |
| Grocery / convenience | Dated SKUs, high cardinality | Category hierarchy | Nearest adjacency |
| Specialty food, bakery | Very short shelf life | Production planning | Most natural second vertical |
| Pharma | Expiry-dated, high unit value | Regulated chain of custody | Highest value, highest cost to enter |

**Only the first row is built.** Everything below it is a thesis, and should be presented as one.

## The insight that makes the breadth credible

Breadth claims are usually hand-waving. This one rests on a structural fact that is true in every
row of that table:

> **The coordination layer exists at enterprise scale and does not exist at mid-market price.**

- **Manufacturing.** SAP and Oracle have handled inter-plant stock transfer orders for decades. A
  six-plant manufacturer does not run SAP.
- **Food service.** Crunchtime serves 850 brands averaging ~176 locations each; Restaurant365 is
  quoted third-party at $499–749 per location per month. The median US multi-concept operator runs
  **13 units**, and [63.5% of them run fewer than 20](https://restaurantchains.net/multi-concept-restaurant-operators-emerging-chains/).
- **The affordable tier gates it.** MarketMan's Starter plan is $249 per location per month;
  inter-location transfers arrive with Enterprise, from $449
  ([pricing](https://www.marketman.com/pricing), checked 19 Sep 2026).

The mid-market of every sector has the same problem and the same non-solution. **That is one market,
not five** — and it is the reason a platform framing is honest here rather than aspirational.

Full competitive working: [competition.md](competition.md).

## Where physical AI sits — and what it is not

A decision is only worth what it costs to execute, and execution is physical. A Common Operating
Environment that reasons about quantities but not about vans, distances, time windows and spare
capacity is incomplete — it will confidently propose moves that nobody makes.

Three things, ordered by how real they are today:

**1. Execution-aware decisions — now.** A transfer only beats a purchase when the physical leg is
cheap enough. The demo transfer carries $20–41 of value against $5–10 by courier, $22–35 by own
staff, and **~$0 if it rides a trip that already exists**. So the automation lever that matters is
batching and routing, not picking — a constraint-solving problem on data CrossHaul already holds.
Working: [physical-ai.md §4](physical-ai.md).

**2. The execution record — now.** Every decision produces a physical task with an outcome. Logging
dispatch and arrival times, carrier, quantity variance, and whether it rode an existing trip is what
makes the next decision better. This is currently the weakest part of the record and the cheapest to
fix.

**3. Embodied execution — not soon, and not ours to build.** Miso Robotics reports **$514,798 of net
revenue in 2025 against $29M raised, with 10 systems deployed** — four years after announcing 100
White Castle locations. That is the deployment rate of a working kitchen robot into a willing chain.
The same $150k machine costs **$9/hour in a distribution centre and $30/hour in a restaurant** on
utilisation and wage alone, before capability.

The honest position, and a better one than building robots:

> **CrossHaul is a beneficiary of transport and warehouse autonomy, not a producer of it.** When an
> intra-city 10 kg drop costs $2 instead of $7, every marginal transfer turns clearly positive and
> recommendation volume rises materially. All of the upside, none of the capex.

[Project-SCIM](https://github.com/abhijitbetigeri/Project-SCIM) is the proof that the
decision → execution → record loop closes end to end. Its own README is candid that nothing is
learned there and the robot follows a scripted task — and that limit is respected everywhere in
these documents.

**Not claimed:** robots in kitchens, learned behaviour, sim-to-real, digital twins.

## The beachhead: food service

All four conditions hold at their sharpest — shelf life measured in days rather than months, demand
that swings by day of week and site, and transfers across a city rather than a country. It is also
where the product is built and live.

The vertical is **Mise**. Its market, pricing, unit economics and go-to-market are worked in full:

| | |
|---|---|
| [market-research.md](market-research.md) | TAM, SAM, the 3–20 unit beachhead, competitive landscape |
| [financial-model.md](financial-model.md) | 3-year cohort model — $3.24M ARR, 84% GM, 4.0-month CAC payback |
| [go-to-market.md](go-to-market.md) | Channel ranking, the Cross-Branch Waste Audit wedge, seven falsifiers |
| [competition.md](competition.md) | The "don't they already have this?" objection, answered |

**Sequencing discipline:** the platform is the reason this is a large company; the beachhead is the
reason it is a real one. Present the primitive, prove it in food service, and name the next sector
without claiming to serve it.
