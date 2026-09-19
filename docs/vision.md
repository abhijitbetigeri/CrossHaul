# Mise — Impact & Vision

Working notes for the Impact & Vision beat of the pitch. Impact & Vision is one of eight scored
criteria; the other seven are scoring business viability, so everything here is written to *support*
the business case, not to substitute for it.

---

## 1. The five-year vision

In five years Mise is the decision layer for perishable inventory across multi-site operators. Not
the ledger that records what moved — the system that decides what moves, and moves it before anyone
buys. By then the loop runs unattended across thousands of locations: forecast per menu item,
explode through the bill of materials, clear the shortage against sister-branch surplus first, and
send a supplier only the net that genuinely has to be bought. The company will have built something
no incumbent can copy by shipping a feature — a longitudinal record of what every location actually
consumed, what it actually paid, and which moves actually cleared — and that record is what makes
each subsequent decision better. The same primitive that routes tomatoes between two restaurants
routes insulin between two pharmacies and chilled produce between two grocery stores; restaurants
are the beachhead, not the ceiling. And because every transfer Mise decides is a logged instance of
a physical task — this crate, from here, to there, by this time — the company will hold, as a
byproduct of ordinary operation, the largest labelled corpus of restaurant-logistics decisions in
existence.

---

## 2. Impact, quantified and bounded

### 2.1 The recovery figure, and why it is deliberately small

| Input | Value | Source |
|---|---:|---|
| Locations, end of year 3 | 1,083 | [financial-model.md](financial-model.md) |
| Waste cost per location per year | $72,000 | Industry estimate ([market-research.md](market-research.md)) |
| Total waste exposure under management | **$77.98M / yr** | 1,083 × $72,000 |
| Mise recovery rate assumed | **15%** | Mise's own conservative bound — see below |
| **Food value recovered, year 3** | **$11.70M / yr** | $77.98M × 0.15 |

The 15% is the most important number on this page and it is deliberately low. Restaurant food waste
has four main components: over-portioning, theft, prep loss, and spoilage/stockout. Mise sees only
the last one, because it is the only component that appears in inventory data. It cannot observe a
cook trimming a carrot badly. ReFED's own sector data agrees with the shape of this bound: roughly
70% of foodservice surplus is plate waste — food the customer left — which no inventory system can
touch ([ReFED Foodservice fact sheet](https://refed.org/downloads/by-sector-foodservice-2025.pdf)).

Do not raise this number under pressure. Its smallness is the credibility.

### 2.2 Converting dollars to tonnes and CO2e

The cleanest available conversion comes from a single dataset, so numerator and denominator share a
methodology. ReFED's 2024 foodservice figures:

| ReFED foodservice, 2024 | Value |
|---|---:|
| Surplus food generated | 12.5M tons |
| Value of that surplus | $157B |
| GHG attributed to it | 63.6M metric tons CO2e |

Two derived factors:

- **Value intensity:** $157B ÷ 12.5M tons = **$12,560 per ton of surplus food**
- **Carbon intensity:** 63.6M t CO2e ÷ 12.5M tons = **5.09 t CO2e per ton of surplus food**

Applied to the year-3 recovery:

| Step | Arithmetic | Result |
|---|---|---:|
| Food value recovered | 1,083 × $72,000 × 0.15 | $11,696,400 |
| Food tonnage (US short tons) | $11,696,400 ÷ $12,560 | **931 tons** |
| Food tonnage (metric) | 931 × 0.9072 | **845 tonnes** |
| Emissions avoided | 931 × 5.09 | **≈ 4,740 t CO2e / yr** |
| Cross-check, direct from value | $11.70M × (63.6M ÷ $157,000M) | 4,738 t CO2e ✓ |

Per location that is roughly **0.86 tons of food and 4.4 tonnes of CO2e per year**.

For scale, using EPA's typical passenger vehicle at 4.6 metric tons CO2 per year
([EPA](https://www.epa.gov/greenvehicles/greenhouse-gas-emissions-typical-passenger-vehicle)):
4,740 ÷ 4.6 ≈ **1,030 cars taken off the road for a year**. Use the car comparison only if the room
is visibly not following the tonnage; tonnage is the more honest unit.

### 2.3 Where this estimate is soft

State this before a judge finds it.

- **Valuation basis.** ReFED values surplus food at approximately menu/retail value (its $157B is
  described as 14% of foodservice sales). The $72,000-per-location waste figure is a purchase-cost
  style number. If the two bases differ, the tonnage is understated. A sanity check cuts in our
  favour: the independently sourced $162B US restaurant food-waste figure lands within 3% of ReFED's
  $157B, which is evidence the two are on comparable footing.
- **Upper bound, for reference only.** If the recovered value were priced at wholesale food cost
  rather than menu value (restaurant food cost runs roughly 30% of menu price), the implied tonnage
  would be ~3,100 tons and ~15,800 t CO2e. **Do not quote this on stage.** It is here so the founder
  knows the direction of the error, not so it can be used.
- **Emissions are attributed, not measured.** The 5.09 t CO2e/ton is a lifecycle attribution across
  production, transport, and disposal. Mise does not measure avoided emissions at any customer site
  and should never claim to.
- **Recovery rate is modelled, not observed.** Zero customers have run the loop in production. The
  15% is an assumption with a defensible mechanism behind it, not a measured result.

### 2.4 The line that connects impact to the business model

This is the sentence that makes Impact score on a panel that is really scoring viability:

> At year 3, Mise charges $2,988 per location per year and recovers roughly $10,800 of food per
> location per year. The customer is buying a **3.6× return**, and the carbon is what falls out of
> the transaction.

$11.70M of food recovered against $3.24M of ARR means the system returns about 3.6× its own price in
the year it is bought. That ratio — not the tonnage — is what a return-seeking judge is listening
for. The tonnage is the proof that the ratio is physically real.

---

## 3. Why this compounds — the data moat

Every incumbent can copy a feature. None of them can copy a history. Four assets accrue from the
first day of the first deployment, and each improves the product's core decision rather than sitting
in a warehouse.

| Asset | What accrues | Why it compounds | Why it cannot be bought |
|---|---|---|---|
| **Forecast accuracy** | Per-SKU, per-branch demand actuals against Mise's own predictions | Every closed loop is a labelled training example; error narrows, which shrinks safety stock, which reduces waste | A competitor starting today starts with zero prediction-outcome pairs and cannot backfill them |
| **Supplier bid history** | What each supplier actually quoted, for what volume, at what lead time, and whether they delivered | Turns procurement from a price lookup into a counterparty model; Mise can tell an operator which supplier is cheap and which is *reliably* cheap | Prices are public; the reliability record of a specific supplier to a specific group is not |
| **Cross-branch demand patterns** | Which branches co-vary, which run opposite cycles, which pairs reliably clear each other's shortages | Rebalance suggestions get better per group, and network-wide the system learns the *shape* of multi-site demand | Requires simultaneous multi-location visibility, which is exactly what operators lack today |
| **Embodied demonstration data** | Every transfer as a physical task record: origin, destination, item, crate, quantity, deadline, whether it cleared | The corpus grows linearly with transactions at zero marginal cost and is the substrate for §4 | Nobody is recording it, because nobody else is making the decision in the first place |

The fourth row is the one to say out loud, because it is the least obvious and the most durable:
**every rebalance decision Mise records is simultaneously a labelled example of an embodied logistics
task.** The dataset is a byproduct of the revenue-generating loop, not a separate investment. That is
the structure investors recognise as a moat — it accrues whether or not anyone is paying attention to
it, and a well-funded competitor cannot buy the years back.

---

## 4. The physical-AI arc — correctly bounded

### 4.1 The hard budget

**One slide. Fifteen seconds. At the Vision beat and nowhere else in the pitch.**

This is written as an instruction, not a suggestion. The failure mode is real: the founder has
shipped something genuinely cool in [Project-SCIM](https://github.com/abhijitbetigeri/Project-SCIM),
it demos beautifully, and spending ninety seconds on it would cost points on Business Model,
Financial Projections, and Problem Solution Fit — the criteria where the money actually is. Show it,
land one line, move on.

### 4.2 What Project-SCIM actually is — claim exactly this and no more

A Unity 6 back-of-house simulation, playable in a browser, in which a robot executes a Mise rebalance
transfer physically: it drives to the branch holding the near-expiry surplus, picks that specific
crate, carries it through the service pass, and hands it to the cook — while the world logs every
path, pick, and handoff as demonstration data for a restaurant-logistics robot.

### 4.3 What the project's own README says, which you must not contradict

| The README states | So do not say |
|---|---|
| "Nothing is learned here: the robot follows a scripted task." | "trained", "learned policy", "the robot figures out" |
| "Avoidance is whisker raycasts, not a planner." | "navigation stack", "path planning", "SLAM" |
| "Geometry is primitives — it reads as a diagram of a restaurant, not a photoreal one." | "photoreal", "sim-to-real transfer", "digital twin" |
| "What works end to end is the pipeline from execution to robot-consumable trajectory data." | This is the actual claim. Make it. |

The honest framing is strong on its own: *the data pipeline works end to end; the policy is future
work.* Two of the eight judges are engineers and one is an applied-AI founder. They will read the
README if the claim sounds inflated, and the README is more candid than most pitch decks. Being
consistent with your own documentation is free credibility; being caught ahead of it is fatal.

### 4.4 Why this is a five-year asset and not a roadmap item

If asked why robots are not on the 18-month plan, the answer is three sentences and should be
delivered as a strength, not a concession:

- **The core loop is not a manipulation problem.** A Mise rebalance is 10kg of tomatoes crossing a
  city. That is a van and a courier. Robotics adds nothing to the economics of what the product
  actually does today.
- **Restaurant back-of-house is among the hardest indoor environments for embodied AI** — cluttered,
  wet, hot, and dense with moving humans. Deployed food-service robotics today is confined to far
  easier problems: front-of-house running and fixed-station fry automation. Anyone claiming a
  near-term kitchen manipulator to this panel is telling them they have not checked.
- **Robot capex has no place in an 84%-gross-margin SaaS story.** Introducing it invites deployment
  cost, payback period, and maintenance questions that weaken the model being scored.

The correct sequencing is: **Mise decides what moves. Someone else's robot, years from now, executes
it. The data that trains it is being written today, by the product that already pays for itself.**

---

## 5. The line to deliver, then stop

Three candidates. The Vision beat needs exactly one closer — if the physical-AI slide has already
landed a line, do not follow it with another.

**A — the physical-AI closer (narrow, evidence-backed)**

> "Every transfer Mise decides today is training data for the robot that executes it tomorrow — and
> we've already built the simulation where that happens."

**B — the category closer (broad, expansion-facing)**

> "In five years, Mise is the routing layer for perishable inventory — the system that decides what
> moves, before anyone buys."

**C — the impact-into-business closer (quantified)**

> "At a thousand locations we move eleven million dollars of food that would have been thrown away —
> and the record of every one of those moves is the thing nobody else can buy."

**Recommendation: B as the closer, with A as the fifteen-second caption on the physical-AI slide.**

B answers the Sequoia question the organisers pointed at — *what will you have accomplished in five
years* — in one clause, and it is the line that opens the expansion argument in §6 without
overclaiming it. A is the better line but it is a line about a *sub-asset*; ending the entire pitch
on the robot slide tells the panel that robots are the company, which is precisely the impression
§4 exists to prevent. Deliver A on the Project-SCIM slide, then advance, then deliver B and stop
talking. C is the fallback if the panel has shown more interest in the numbers than the narrative —
it is the strongest of the three with a purely financial audience, and the weakest on Vision.

Whichever is used: stop after it. Do not append "and we think that's really exciting." The silence
is the delivery.

---

## 6. Beyond restaurants

The expansion argument is about a **primitive**, not a product. The primitive is: *forecast demand
per site, net it against what sister sites already hold, and buy only the remainder.* Everything
restaurant-specific in Mise sits above that primitive — the recipe bill-of-materials, the menu
promotion sweep. The primitive itself is indifferent to what is in the crate.

It applies wherever four conditions hold at once: **multiple sites under one owner, perishable or
dated stock, site-level demand that varies independently, and a transfer that is cheaper than a
purchase.**

| Vertical | Why the primitive fits | What would have to be rebuilt | Honest status |
|---|---|---|---|
| **Grocery / convenience** | Dated stock, high SKU count, store-level demand variance, existing inter-store transfer logistics | Category hierarchy replaces recipe BOM; far higher SKU cardinality | Nearest adjacency. Not built. |
| **Pharmacy** | Expiry-dated stock, high unit value, stockout has real consequence, chains already move stock between branches | Regulated chain of custody; controlled-substance handling is a hard compliance surface | Highest value per unit, highest regulatory cost. Not built. |
| **Specialty food retail / bakery chains** | Short shelf life, same-day demand swings, production planning already resembles a BOM | Very little — closest structural match to restaurants | Most natural second vertical. Not built. |
| **Any multi-site perishable inventory** | Same four conditions | Vertical-specific demand model | The general statement of the thesis |

Two disciplines when saying this on stage:

1. **Name it as sequencing, not capability.** "The primitive generalises" is a defensible claim.
   "We can serve pharmacies" is not — nothing is built for any of these.
2. **Do not let it dilute the beachhead.** The scored criteria reward a focused go-to-market. The
   expansion argument exists to answer "how big can this get", asked once, and then to be dropped.
   Mise is a restaurant company that happens to have built something more general.

---

## 7. What not to say

| Do not say | Why it costs you | Say instead |
|---|---|---|
| "Robots in kitchens within X years" | Two engineers and an applied-AI founder are on this panel; they know the state of the art and the claim reads as not having checked | "The manipulation problem is years out. What is not years out is the data that will train it." |
| "The robot learned to..." | Directly contradicts Project-SCIM's own README, which is public and linked from the repo | "The robot follows a scripted task. What works end to end is the pipeline from execution to robot-consumable trajectory data." |
| Leading with sustainability | Three investors, a GTM lead, and an AI-data operator are scoring viability. Opening on carbon signals the economics are weak enough to need a moral supplement | Lead with the 3.6× return per location; let the 4,740 tonnes land as the consequence |
| "We eliminate food waste" | Contradicts Mise's own 15% bound, and the bound is the credibility | "We recover the spoilage-and-stockout component, which is about 15%. We do not touch plate waste, portioning, or theft." |
| "Digital twin" / "sim-to-real" | Geometry is primitives; the README says so | "A simulation of the task, built to prove the data pipeline." |
| "Multi-billion-dollar impact" | Invites arithmetic that will not survive | Give the year-3 number with the arithmetic visible |
| Quoting the 3,100-ton upper bound | It is a sensitivity, not an estimate | 931 tons / 4,740 t CO2e, with the valuation caveat volunteered |
| "No one else is doing this" | MarketMan and Restaurant365 ship transfers as bookkeeping; a judge may know that | "They record the transfer. We make the decision. That is an architecture difference, not a feature gap." |

One more, structural: **do not present Impact as a separate act.** The strongest version of this
section is roughly forty seconds — the recovered dollars per location, the tonnage as its physical
consequence, the data moat as why it compounds, fifteen seconds on the robot, and the closing line.
Impact & Vision is one of eight criteria, and it is the one most easily lost by over-delivering it.

---

## Sources

- [ReFED — Food Waste by Sector: Foodservice fact sheet (2024 data)](https://refed.org/downloads/by-sector-foodservice-2025.pdf) — 12.5M tons foodservice surplus; $157B valuation; 63.6M metric tons CO2e; 78.4% to landfill; ~70% plate waste. All conversion factors in §2.2 derive from this one sheet.
- [ReFED — 2026 U.S. Food Waste Report](https://refed.org/food-waste/refed-us-food-waste-report-2026/) — sector context and methodology.
- [EPA — Greenhouse Gas Emissions from a Typical Passenger Vehicle](https://www.epa.gov/greenvehicles/greenhouse-gas-emissions-typical-passenger-vehicle) — 4.6 metric tons CO2/vehicle/year, used only for the car-equivalence framing.
- [EPA — Quantifying Methane Emissions from Landfilled Food Waste (2023)](https://www.epa.gov/land-research/quantifying-methane-emissions-landfilled-food-waste) — ~0.84 t CO2e per ton of landfilled food from fugitive methane alone. Not used in the headline figure, which uses ReFED's fuller lifecycle attribution; cited here because a judge may ask which basis was used.
- [EPA — From Farm to Kitchen: The Environmental Impacts of U.S. Food Waste (2021)](https://www.epa.gov/system/files/documents/2021-11/from-farm-to-kitchen-the-environmental-impacts-of-u.s.-food-waste_508-tagged.pdf) — 169M MTCO2e embodied in annual U.S. food waste excluding landfill emissions; independent corroboration that a per-ton intensity in the 2.5–5 t CO2e range is the right order of magnitude.
- [Mise financial model](financial-model.md) — 1,083 locations and $3.24M ARR at end of year 3.
- [Mise market research](market-research.md) — $72,000/location waste cost, $162B industry figure, physical-AI feasibility assessment.
- [Project-SCIM](https://github.com/abhijitbetigeri/Project-SCIM) — the embodied simulation and its stated limitations.
