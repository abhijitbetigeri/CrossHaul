# Mise — the competition question

**"Don't restaurants and franchises already have this software?"**

Compiled 19 Sep 2026. Every factual claim below is linked. Where a claim could not be verified from
primary documentation, it is marked **[unverified]** rather than asserted — the founder may repeat
this on stage, and an unsourced number that gets challenged costs more than an admitted gap.

---

## 1. The honest answer, in one paragraph

Yes — restaurant inventory software exists, it is mature, and the category leaders are large,
well-funded businesses. Crunchtime alone runs in **150,000+ locations across 850+ restaurant
brands** ([Crunchtime](https://www.crunchtime.com/)). Restaurant365 crossed a **$1B valuation on
$135M co-led by KKR and L Catterton**, with products in **40,000+ restaurants**
([Restaurant365](https://www.restaurant365.com/in-the-news/restaurant365-announces-135m-funding-round-co-led-by-kkr-and-l-catterton/),
[Orange County Business Journal](https://www.ocbj.com/oc-homepage/restaurant365-hits-1b-valuation-135m-raised/)).
Three things are nevertheless true. **First**, inter-location transfers in every incumbent we could
document are a *recording* function, not a *deciding* function: a human notices the imbalance,
a human creates the transfer, and the software keeps the books straight. **Second**, the one
capability that is genuinely automated — forecast-driven suggested ordering — is computed
*per store, against that store's own on-hand*, and its output is always a purchase order, never a
transfer. **Third**, the operator Mise sells to, the 3–20 unit group, mostly is not running any of
this: the median US multi-concept operator has **13 units**
([RestaurantData via Restaurant Magazine](https://www.restaurantmagazine.com/restaurantdata-multi-concept-restaurant-operators-local-regional/)),
while Crunchtime's installed base averages ~176 locations per brand.

Where the objection is **right**: transfers exist, forecasting exists, consolidated purchasing
exists. Mise is not inventing any of these primitives.

Where the objection is **wrong**: no documented product closes the loop — *forecast → shortage →
search sister branches → propose the move → net what remains → one PO*. Every incumbent breaks
the chain at the same link, and it is the same link for all of them.

---

## 2. What a 3–20 unit group actually runs today

| Layer | Who owns it | Typical mid-market choice | Notes |
|---|---|---|---|
| POS / transaction | Toast, Square, Lightspeed, SpotOn | Toast or Square | Toast POS holds an estimated ~11.8% global share of the integrated-restaurant-tech category ([Technology Evaluation](https://www3.technologyevaluation.com/solutions/53909/toast-pos)) |
| Invoice capture / AP | xtraCHEF (Toast), MarginEdge, Ottimate | xtraCHEF if on Toast | xtraCHEF is invoice/cost-management first; it explicitly does not link locations' inventory ([Toast xtraCHEF](https://pos.toasttab.com/products/xtrachef), [analysis](https://restaurantinventorymanagementsoftware.com/blog/toast-inventory-management-complete-guide-2025)) |
| Inventory / back-office | MarketMan, Restaurant365, Crunchtime, Supy, Apicbase, MarginEdge | MarketMan or nothing | See §4 |
| Accounting / GL | QuickBooks Online, Sage Intacct, R365's own GL | QuickBooks Online | R365's differentiator is that accounting and inventory are one system ([Restaurant365](https://www.restaurant365.com/restaurant-management-system/)) |
| Labor / scheduling | 7shifts, R365 Labor, Crunchtime Teamworx | 7shifts | Adjacent to Mise; not contested |

Two structural facts about that stack matter for the pitch:

1. **The POS owns the demand signal and refuses to own the supply decision.** Toast's inventory
   product is per-location; operators asking to move items between units find no built-in function
   ([Toast Community thread](https://community.toasttab.com/t5/restaurant-operations/item-transfers-between-units/m-p/11417),
   summarised [here](https://restaurantinventorymanagementsoftware.com/blog/toast-inventory-management-complete-guide-2025)).
2. **The back-office layer is a ledger that happens to have a forecast bolted on**, not a planner.
   This is the crux of §5.

---

## 3. Adoption — the part of the answer that actually wins the argument

### 3.1 What we can source

| Claim | Number | Source | Strength |
|---|---|---|---|
| Restaurants using inventory management software | **45%** (vs. 84% POS, 52% accounting, 50% payroll) | [Toast 2019 Restaurant Success Report, via Restaurant Dive](https://www.restaurantdive.com/news/69-of-restaurants-use-multiple-technologies-but-many-want-all-in-one-syst/559006/) | Attributable but **2019** — treat as a floor, not a current figure |
| Operators planning to *increase* inventory-tech investment in 2024 | **52%** | [NRA Restaurant Technology Landscape Report 2024](https://restaurant.org/education-and-resources/resource-library/new-report-examines-the-technology-landscape-in-todays-restaurants/) | Strong. A category half the market still plans to buy into is not a saturated category |
| Operators describing their own tech use as "mainstream" rather than leading-edge | Majority | [NRA 2024](https://restaurant.org/education-and-resources/resource-library/new-report-examines-the-technology-landscape-in-todays-restaurants/) | Directional |
| Restaurant *executives* reporting daily AI use in inventory management | **55%**; another 25% testing | [Deloitte, Q4 2024, n=375 global restaurant executives](https://www.deloitte.com/us/en/about/press-room/deloitte-how-ai-is-revolutionizing-restaurants.html) | **Cuts against us — read §3.3** |
| US restaurants that are single-unit operations | **~70%** | NRA, cited widely incl. [Orbital](https://www.withorbital.com/data/how-many-restaurants-in-the-us/) | Strong, and defines who is *not* the buyer |
| Median US multi-concept operator | **3 concepts, 13 units, 2 states** | [RestaurantData study, n=1,339 companies / 288,239 units](https://www.restaurantmagazine.com/restaurantdata-multi-concept-restaurant-operators-local-regional/) | Strong — the median multi-unit operator sits inside Mise's 3–20 band |
| Multi-concept organisations operating fewer than 20 locations | **Nearly two-thirds** | [same](https://www.restaurantmagazine.com/restaurantdata-multi-concept-restaurant-operators-local-regional/) | Strong |
| Emerging-brand growth transitions, 2-to-4 units vs 5-to-19 units | **66.4% / 33.6%** of 3,381 tracked expansions | [RestaurantData 2026](https://www.restaurantnews.com/restaurant-growth-in-2026-extends-from-second-locations-to-19-units-080326/) | Strong |
| Crunchtime installed base | 850+ brands, 150,000+ locations → **~176 locations/brand average** | [Crunchtime](https://www.crunchtime.com/) (ratio is our arithmetic) | Strong, and the single best adoption-concentration datapoint available |

### 3.2 The number we could *not* verify — say so

A widely repeated figure, **"42% of operators still rely on pen-and-paper or spreadsheets for
scheduling, inventory, or sales tracking"**, appears on
[Barmetrix](https://www.barmetrix.com/blog/restaurant-industry-trends) **with no attribution to any
named study**. We traced it and found no primary source. **Do not use this number on stage.** If a
judge cites it back, the correct response is "that one floats around unattributed; here is what I
can actually source" — and then give the Toast 45% and the Crunchtime concentration ratio.

Likewise, no current, segment-specific survey of "what share of 3–20 unit operators run dedicated
inventory software" appears to exist publicly. **[unverified]** That is a real gap in the evidence
base and the honest framing is: the hypothesis is supported by structural evidence (§3.4), not by a
direct measurement.

### 3.3 The evidence that cuts against the hypothesis — handle it first

Deloitte reports **55% of restaurant executives using AI in inventory management daily**
([Deloitte](https://www.deloitte.com/us/en/about/press-room/deloitte-how-ai-is-revolutionizing-restaurants.html)).
Taken at face value that would demolish the "nobody has this" argument. It does not, for a reason
worth stating explicitly because a Rain Capital partner will spot it before you do:

- The sample is **375 global restaurant *executives* across 11 countries**. A company large enough
  to employ a surveyed executive is not a 6-unit taqueria group. The instrument is enterprise-skewed
  by construction.
- Deloitte's own finding is that **fewer than half of respondents say their organisation is ready
  for AI adoption** — 39% on technology infrastructure, 34% on operations. Daily *use* and
  operational *readiness* are being reported by the same population at very different levels.

The correct reading: **AI-driven inventory is real and concentrated at the top of the market.** That
is the same shape as the Crunchtime ratio. It is evidence *for* the mid-market gap, not against it.

### 3.4 The structural argument, which is stronger than any survey

Rather than resting on a contested percentage, rest on three verifiable structural facts:

1. **Vendor self-selection.** Crunchtime is described by third-party analysts as built for
   multi-unit brands with **more than 10 locations**, with customers including Chipotle, Five Guys,
   Dunkin', Wingstop, Texas Roadhouse and Burger King
   ([Crunchtime](https://www.crunchtime.com/), [ITQlick](https://www.itqlick.com/crunchtime/pricing)).
   Implementation is quoted third-party at **$5,000 for small businesses rising past $50,000 for
   full enterprise rollouts** ([ITQlick](https://www.itqlick.com/crunchtime/pricing)) — **[unverified
   by Crunchtime; third-party estimate only]**.
2. **Price gating.** Restaurant365 is quoted by third parties at **$499/location/month (Essential)
   and $749/location/month (Professional)**, with onboarding billed separately and one reviewer
   reporting **$14K** ([pricing aggregators](https://pricingnow.com/question/restaurant365-pricing/),
   [Capterra](https://www.capterra.com/p/139768/Restaurant365/pricing/)). R365 publishes no list
   price. **[unverified by R365 — they quote custom only]**.
3. **Feature gating within the affordable tier.** See §4.3.

A 9-unit group cannot buy Crunchtime economics and does not want R365's GL. That is the buyer.

---

## 4. What incumbents genuinely do and do not do

Assessed against documentation and help-centre material, not landing pages. The four capabilities
are those in the brief:

- **(a)** forecast demand per menu item per location
- **(b)** automatically *detect* that branch A's shortage is coverable by branch B's surplus
- **(c)** *propose or execute* a transfer without a human initiating it
- **(d)** *net the franchise-wide position* before purchasing

### 4.1 Capability matrix

| Capability | MarketMan | Restaurant365 | Crunchtime | Supy | Apicbase | Spreadsheets | **Mise** |
|---|---|---|---|---|---|---|---|
| **(a) Per-item demand forecast, per location** | **Partial** — dynamic par per item from 1–5 weeks of consumption, but their own documentation says the feature "doesn't apply any forecasting logic independently, it uses your current prediction logic", integrating Deputy/Tenzo instead ([MarketMan](https://www.marketman.com/blog/suggestive-ordering)) | **Not documented** on the inventory page; forecasting is documented for **labor**, not inventory ([R365 Inventory](https://www.restaurant365.com/inventory/inventory-management/), [R365 AI launch](https://www.prnewswire.com/news-releases/restaurant365-introduces-r365-ai-the-only-intelligence-engine-built-on-the-full-restaurant-pl-302768635.html)) | **Yes** — predicts sales/traffic/checks, derives dynamic par, subtracts on-hand, compares delivery dates ([Crunchtime](https://www.crunchtime.com/blog/benefits-of-recommended-orders)) | **Partial** — par-threshold triggered PO suggestions ([Supy](https://supy.io/blog/multi-location-restaurant-inventory-management/)) | **Yes** — "proposes orders per site and per supplier based on recent sales and lead times" ([Apicbase](https://get.apicbase.com/demand-forecasting-software-restaurant/)) | No | Yes |
| **(b) Auto-detect cross-branch surplus covering a shortage** | **No evidence** — multi-unit page claims "predictive analytics to forecast demand" but never surplus-to-shortage matching ([MarketMan](https://www.marketman.com/platform/multi-unit-restaurant-commissary-kitchen-inventory-software)) | **No** — commissary flow is order-driven end to end ([R365 docs](https://docs.restaurant365.com/docs/commissary)) | **No evidence** in product pages, help centre or the full course catalogue ([Crunchtime training guide, PDF](https://assets.crunchtime.com/image/upload/v1/docs/RG_-_Platform_Training_Reference_Guide.pdf)) | **No** — human creates the request ([Supy](https://supy.io/product-features/inventory-transfers)) | **No** — forecast output is a supplier PO, not a redistribution ([Apicbase](https://get.apicbase.com/demand-forecasting-software-restaurant/)) | No | Yes |
| **(c) Propose/execute a transfer with no human initiating** | **No** — "lets you **record** items sent … between restaurant sites" ([MarketMan](https://www.marketman.com/platform/multi-unit-restaurant-commissary-kitchen-inventory-software)) | **No** — "Control inventory with accurate transfer **tracking**" ([R365](https://www.restaurant365.com/inventory/inventory-management/)) | **No** — the training catalogue is entirely human verbs: *Create a Transfer to Send Goods to Another Location*, *Create a Transfer to Request Goods From Another Location*, *Process a Request to Transfer Goods*, *Reconcile a Transfer of Goods Sent to Your Location* ([PDF](https://assets.crunchtime.com/image/upload/v1/docs/RG_-_Platform_Training_Reference_Guide.pdf)) | **No** — "Create transfer requests from one branch to another in seconds"; receiving branch must accept ([Supy](https://supy.io/product-features/inventory-transfers)) | **No** — transfers update stock and cost automatically *once made* ([Apicbase](https://get.apicbase.com/restaurant-inventory-management-software/)) | No | Yes |
| **(d) Net the franchise-wide position before purchasing** | **Partial** — HQ centralises pricing, approved vendors and consolidated reporting; no documented netting against sister-branch stock ([MarketMan](https://www.marketman.com/platform/multi-unit-restaurant-commissary-kitchen-inventory-software)) | **Partial** — commissary prints a *consolidated production list* across submitted store orders ([R365 docs](https://docs.restaurant365.com/docs/commissary)) | **[unverified]** — bid management and distribution exist; no documentation found confirming cross-location net requirement | **Partial — closest incumbent.** Aggregates pending demand from all outlets into one consolidated supplier order ([Supy](https://supy.io/blog/learn-standing-orders-recurring-supplier-orders-restaurants)). But it consolidates **gross** demand for buying power; no evidence it nets against surplus held elsewhere | **No evidence** of cross-site netting | No | Yes |
| **(e) Record a transfer once a human decides** | **Yes**, gated to Enterprise | **Yes** | **Yes** | **Yes**, with full request→approve→dispatch→receive audit trail | **Yes** | Manual | Yes |
| **(f) Auto-convert near-expiry surplus into a menu promotion** | No | No | No | No | No | No | Yes |

### Where incumbents win outright — state this before you are asked

| Capability | Who wins | Why it matters |
|---|---|---|
| General ledger, AP, multi-entity accounting, period close | **Restaurant365** — accounting and inventory in one system ([R365](https://www.restaurant365.com/restaurant-management-system/)) | Mise has none of this and should not claim to |
| Labor, scheduling, time & attendance, AI schedule generation | **R365** ([R365 AI, May 2026](https://www.prnewswire.com/news-releases/restaurant365-introduces-r365-ai-the-only-intelligence-engine-built-on-the-full-restaurant-pl-302768635.html)), **Crunchtime** (Teamworx) | Adjacent; not contested |
| Food safety, task management, e-learning, operations execution | **Crunchtime** ([suite](https://www.crunchtime.com/)) | 2.4M+ training courses completed since 2015 ([PDF](https://assets.crunchtime.com/image/upload/v1/docs/RG_-_Platform_Training_Reference_Guide.pdf)) |
| Vendor EDI breadth | **MarketMan Enterprise** (unlimited EDI integrations) ([pricing](https://www.marketman.com/pricing-for-restaurant-inventory-management-system)) | Table stakes Mise must buy or partner for |
| Invoice OCR at volume | MarketMan (unlimited scans on Growth+), xtraCHEF, MarginEdge | Mature, commoditised |
| Enterprise deployment, support, references at 100+ units | Crunchtime, R365 | Mise has none of this |

### 4.2 The Crunchtime open item — resolved

**Question:** does Crunchtime automate rebalancing, or merely record it?

**Answer: it records it. Transfers are human-initiated on both ends.** The strongest available
evidence is Crunchtime's own **Platform Training Reference Guide (v11.00, Aug 2024)**, which lists
the complete Net-Chef course catalogue. The transfer module is five courses, and every verb is a
human one:

| Course | Title | Length |
|---|---|---|
| NCI 102a | *Create a Transfer to Send Goods to Another Location* | 4 min |
| NCI 102b | *Create a Transfer to Move Product to a New Storage Location* | 2 min |
| NCI 102c | *Create a Transfer to Request Goods From Another Location* | 3 min |
| NCI 102d | *Process a Request to Transfer Goods to Another Location* | 2 min |
| NCI 102e | *Reconcile a Transfer of Goods Sent to Your Location* | 3 min |

Source: [Crunchtime Platform Training Reference Guide, PDF](https://assets.crunchtime.com/image/upload/v1/docs/RG_-_Platform_Training_Reference_Guide.pdf).

There is no course — and no help-centre article we could locate — for *reviewing a suggested
transfer* or *approving a system-proposed rebalance*. Crunchtime's help centre reinforces the manual
frame: its transfer troubleshooting article is titled *"Why are Products not available when
**creating** a Location Transfer?"* and enumerates the setup prerequisites a human must satisfy
before the form will accept the line
([Crunchtime Support](https://crunchtime.zendesk.com/hc/en-us/articles/360013043694-Why-are-Products-not-available-when-creating-a-Location-Transfer)).

Meanwhile Crunchtime **does** automate ordering — and this is the honest concession. Its
recommendation engine predicts sales, traffic and check counts, derives a dynamic par from
consumption and forecast, subtracts on-hand, and compares against delivery dates to output an order
quantity ([Crunchtime](https://www.crunchtime.com/blog/benefits-of-recommended-orders)). It is a
genuine forecast-to-purchase loop. **It is also single-store-scoped and its only output is a
purchase order.** The Crunchtime inventory product page never mentions inter-location transfers at
all ([Crunchtime](https://www.crunchtime.com/inventory-management)).

**So the answer to "does Crunchtime already do this?" is: it does the forecasting half at
enterprise scale and price, and does not do the rebalancing half at any price we could document.**

### 4.3 The pricing gate — verify before the pitch

| Product | Price | Source | Note |
|---|---|---|---|
| MarketMan Starter | $199/location/month | [BackofHouse review](https://backofhouse.io/vendors/marketman) | Third-party; matches the previously verified figure |
| MarketMan Growth | $249/location/month | [BackofHouse](https://backofhouse.io/vendors/marketman) | |
| MarketMan Enterprise | Custom, "restaurants with 5 or more locations" | [BackofHouse](https://backofhouse.io/vendors/marketman) | |
| MarketMan list price **as of this research** | Starter **$249**, Growth **$299**, Enterprise **from $449**, per location, free setup ("$1,500 value") | [MarketMan pricing page](https://www.marketman.com/pricing-for-restaurant-inventory-management-system) | **MarketMan's live page is now higher than the third-party figures and setup is free, not $500** |
| MarketMan Commissary add-on | $499/mo standalone, $749/mo external | [MarketMan](https://www.marketman.com/pricing-for-restaurant-inventory-management-system) | On top of the per-location plan |
| Square Restaurant Inventory by MarketMan | **$99/location/month**, requires Square Plus ($49) or Premium ($149) | [Square](https://squareup.com/us/en/inventory-management/restaurants), [Businesswire, Apr 2026](https://www.businesswire.com/news/home/20260402238712/en/Square-and-MarketMan-Launch-Advanced-Inventory-Management-Integration-for-Restaurants) | Effective floor **$148–$248/location/month** |
| Restaurant365 | $499 / $749 per location/month **[third-party only]** | [aggregator](https://pricingnow.com/question/restaurant365-pricing/) | R365 publishes no list price |
| Crunchtime | Custom; third-party estimates thousands/month + $5K–$50K implementation **[unverified]** | [ITQlick](https://www.itqlick.com/crunchtime/pricing) | |
| **Mise** | **$249/location/month** | — | Sits at MarketMan Starter list, below MarketMan Growth, **at half R365's floor** |

**Action item before the pitch:** MarketMan's published pricing has moved since it was last
verified. Re-check [the live page](https://www.marketman.com/pricing-for-restaurant-inventory-management-system)
the morning of, and quote the live number. Getting caught on a stale competitor price is a
self-inflicted wound.

The *feature-gating* claim — that inter-location transfers sit in MarketMan's Enterprise tier —
is corroborated by third-party reviews describing Enterprise as the multi-unit/franchise plan
including centralised reporting and inter-location transfers
([The Restaurant HQ](https://www.therestauranthq.com/technology/marketman-review/)). **MarketMan's
own published tier list does not name transfers in any tier [unverified against MarketMan's own
documentation]**, so phrase it as "transfers land in their multi-unit tier" rather than quoting a
tier name you cannot source.

---

## 5. The precise differentiation

State it in this order. It is built to survive someone who has actually used MarketMan.

### 5.1 Deciding versus recording

Every incumbent transfer feature is a **bookkeeping primitive**. The vocabulary is unanimous and
it is theirs, not ours:

- MarketMan: *"lets you **record** items sent … between restaurant sites"* ([MarketMan](https://www.marketman.com/platform/multi-unit-restaurant-commissary-kitchen-inventory-software))
- Restaurant365: *"Control inventory with accurate transfer **tracking**"* ([R365](https://www.restaurant365.com/inventory/inventory-management/))
- Supy: *"**Create** transfer requests from one branch to another"* ([Supy](https://supy.io/product-features/inventory-transfers))
- Crunchtime: *"**Create** a Transfer to **Request** Goods From Another Location"* ([PDF](https://assets.crunchtime.com/image/upload/v1/docs/RG_-_Platform_Training_Reference_Guide.pdf))

In every case the sequence is: **a human notices → a human decides → the software books it.** The
expensive step — noticing, across branches, before the shortage bites — is left to a GM who can see
one store.

Mise inverts the sequence: **the system notices → the system proposes → a human approves.**

### 5.2 The chain, and where each incumbent breaks it

```
forecast per menu item, per branch
        ↓
explode through recipe BOM → ingredient requirement
        ↓
compare to on-hand → per-branch shortage / surplus
        ↓
match shortage against sister-branch surplus        ← EVERY INCUMBENT BREAKS HERE
        ↓
propose the transfer
        ↓
net the residual across the whole group
        ↓
one PO, one approval
```

Crunchtime and Apicbase execute steps 1–3 well, then jump straight to a purchase order. Supy is the
only product we found that touches step 6 — consolidating outlet demand into one supplier order
([Supy](https://supy.io/blog/learn-standing-orders-recurring-supplier-orders-restaurants)) — but it
consolidates **gross** demand for buying leverage, with no documented check against stock already
sitting in the group. **Nobody executes step 4.**

### 5.3 The mid-market cannot buy the automated half at mid-market price

Even the human-initiated transfer is tiered above the entry product. Square's MarketMan entry SKU
at $99/location/month plus a $49–$149 Square plan is where a small group actually lands, and
multi-unit transfer functionality is not there. The automated forecasting that does exist
(Crunchtime) sits behind custom enterprise pricing and five-figure implementations. **Mise's claim
is not "we invented transfers." It is "the decision layer has never been sold at $249."**

### 5.4 The secondary capability nobody has

Auto-converting near-expiry surplus into a menu promotion does not appear in any incumbent's
documented feature set. What exists in the category is **expiry alerting** — flagging items
approaching shelf-life so staff can act. Generating the promotion itself is, as far as our search
found, unclaimed. **[Absence of evidence — we could not exhaustively search every vendor's release
notes; phrase as "I haven't found anyone shipping this" rather than "nobody does this."]**

---

## 6. Why incumbents have not built it

Three candidate explanations. Be honest that the third is live.

### 6.1 Architecture — real, but do not overstate it

The naive version of this argument ("their data model can't produce a per-SKU forecast") is
**false and a judge will know it.** Incumbents already deplete theoretical on-hand continuously by
mapping POS sales through recipes — Compeat pulls Toast sales to automatically deplete stock as
items sell, and actual-vs-theoretical variance reporting is a standard feature across MarketMan,
R365 and Crunchtime ([MarginEdge on AvT](https://www.marginedge.com/blog/a-restaurant-operators-guide-to-actual-vs-theoretical-food-costs-and-usage)).

The **defensible** version has three parts:

1. **Confidence, not capability.** Theoretical on-hand is reconciled against a physical count that
   is typically **weekly for most items, monthly for slow-moving dry goods**
   ([MarketMan](https://www.marketman.com/blog/how-often-should-a-restaurant-take-inventory)).
   Between counts the number drifts by exactly the amount of the unmeasured variance — waste, theft,
   over-portioning, unrecorded comps. A ledger built to be *trued up at period close* is accurate
   enough to cost a P&L and too uncertain, unqualified, to auto-dispatch a van. Making a transfer
   decision requires a **confidence interval on on-hand**, which the AvT model does not produce.
2. **The optimisation object does not exist.** These are per-location ledgers rolled up for
   reporting. R365's HQ view "tracks item pricing across locations"; MarketMan's HQ "centralises
   inventory, purchasing, and reporting across all locations from one dashboard." Both are
   **read-side aggregation**. There is no write-side network object — no group-level requirement
   vector to solve a min-cost-flow against. Adding one is not a feature; it is a second data model.
3. **The workflow surface is wrong.** Incumbent inventory UX is built for a store manager doing a
   count. A rebalancing proposal has no owner in that UI: it is above-store, needs a cross-branch
   approver, and needs logistics the software does not model (who drives, when, does the cold chain
   hold). Crunchtime's answer to this is five training courses teaching humans the manual workflow.

### 6.2 Incentive and segment

Crunchtime's economics are set by 850 brands averaging ~176 locations. At that size groups run
**commissaries and distribution centres** — the redistribution problem is already solved by a hub,
which R365 models explicitly as commissary order forms, fulfilment and consolidated production
lists ([R365 docs](https://docs.restaurant365.com/docs/commissary)). **Peer-to-peer rebalancing is
a problem shape that belongs specifically to groups too big to wing it and too small for a
commissary — 3 to 20 units.** That is precisely the segment the enterprise vendors price past and
the entry vendors feature-gate below.

### 6.3 "They could, and might" — the honest answer

They could. R365 shipped **R365 AI on 12 May 2026** with an AI Advisor and one-click AI Scheduling
([PR Newswire](https://www.prnewswire.com/news-releases/restaurant365-introduces-r365-ai-the-only-intelligence-engine-built-on-the-full-restaurant-pl-302768635.html)).
Crunchtime already owns the forecast. Supy already owns cross-outlet demand aggregation. None of
them has shipped step 4, but no law of physics prevents it — and the first-order barrier is product
priority, not technology. **The defensible claim is a timing and focus claim, not an impossibility
claim.** Say that out loud; it is more credible than the alternative and a CS PhD will respect it.

---

## 7. Where Mise sits — alongside, not instead of

**Answer to "do I have to rip out MarketMan?": no.** Mise is a decision layer that reads
inventory and sales state and writes back transfers and one PO. Replacing the ledger, the invoice
OCR, the EDI catalogue and the accounting export is a multi-year build with no differentiation in
it, and the rip-out is the single biggest reason mid-market back-office deals die.

| Integration | Priority | Why |
|---|---|---|
| **Toast** | Table stakes | Owns the demand signal for most of the target segment; large published partner directory ([Toast](https://pos.toasttab.com/blog/on-the-line/toast-pos-integrations)) |
| **Square** | Table stakes | The entry-tier segment lives here; MarketMan already ships a Square SKU ([Businesswire](https://www.businesswire.com/news/home/20260402238712/en/Square-and-MarketMan-Launch-Advanced-Inventory-Management-Integration-for-Restaurants)) |
| **MarketMan / R365 read + write** | Table stakes for "sit alongside" | Read on-hand and recipes, write the transfer back as their native transfer record so their books stay correct. **The transfer must land in their ledger — otherwise Mise breaks the customer's COGS** |
| **Distributor EDI (Sysco, US Foods, PFG)** | Phase 2 | MarketMan Enterprise offers unlimited EDI; matching that is expensive. Ship PO-by-email/CSV first |
| **QuickBooks Online** | Phase 2 | The mid-market GL. Not Sage Intacct — that is the R365/enterprise end |

**Sales motion consequence:** Mise is an *add-on* to an existing back office, or a *first* system
for a group on spreadsheets. It is not a displacement sale. Positioning it as a replacement forces
a comparison Mise loses (no GL, no AP, no labor, no food safety) instead of the comparison it wins
(nobody rebalances).

**The honest caveat to say before a judge says it:** for a group with **no** inventory system at
all, Mise must produce its own on-hand — which means counts, recipe BOMs and supplier catalogues.
That is the real onboarding cost and it is the same cost that makes incumbent implementations
expensive. There is no free lunch in this layer.

---

## 8. The rebuttal script

### 8.1 The 30-second spoken answer

> Partly, yes — and the part that is true is the part I'd want you to press on.
>
> MarketMan, Restaurant365 and Crunchtime all ship inter-location transfers. But read their own
> words: MarketMan "records items sent between restaurant sites." Restaurant365 does "accurate
> transfer tracking." Crunchtime's training catalogue has five courses, and every one starts with
> "Create a Transfer." A human notices the imbalance, a human decides, and the software books it
> correctly. That is accounting.
>
> Mise does the noticing. We forecast per menu item per branch, explode it through the recipe
> bill-of-materials, and when branch four is short, we check branches one through seven before we
> check a supplier. Only what the group genuinely doesn't have becomes a purchase order.
>
> And the buyer matters. Crunchtime runs 150,000 locations across 850 brands — that's 176 locations
> per brand. My buyer has nine. They're on a clipboard, or on MarketMan's entry tier where transfers
> aren't included. Nobody is selling them the decision at $249 a location.

### 8.2 Follow-ups a knowledgeable judge asks next

**Q1. "Crunchtime already forecasts demand and auto-generates orders. Why isn't that the same
thing?"**

Because forecasting and rebalancing are different products and Crunchtime only built one. Their
recommendation engine predicts sales, derives a dynamic par, subtracts **that store's** on-hand and
outputs a **purchase order**. It never looks sideways and it never outputs a transfer — their
inventory product page does not mention inter-location transfers at all. Their transfer module is
five training courses teaching a human to fill in a form. They own the forecast and they stop one
step before the decision that saves the money. And they sell it at custom enterprise pricing with a
five-figure implementation, to brands averaging 176 locations.

**Q2. "Your rebalancing depends on knowing real stock levels. Their on-hand number is theoretical
and drifts between weekly counts. Why is yours any better?"**

*(This is the best question available and the answer is not "ours is more accurate.")* It isn't —
we read the same POS depletion and we carry the same variance. The difference is what we do with the
uncertainty. Incumbents report a point estimate to be trued up at period close. We carry a
confidence band and only propose a move when the surplus exceeds the band by a margin that makes the
move worth it — so the failure mode is a missed transfer, not a wrong one. And every proposal goes
to a human before anything leaves a building. The count-discipline problem is real and it is our
biggest onboarding risk, not something I'll claim we've solved.

**Q3. "What stops Restaurant365 from shipping this next quarter? They just launched R365 AI."**

Nothing technical. They shipped R365 AI in May with an AI Advisor and AI Scheduling — no supply-chain
agent, no cross-location netting. Three things slow them: their transfer object is a per-location
ledger entry with no group-level requirement vector to optimise against, so it's a data-model change
not a feature; their large customers already solve redistribution with a commissary, which they
model explicitly; and their pricing floor is around $499 a location, which means the segment where
peer-to-peer rebalancing matters most isn't their segment. That's a timing advantage, not a moat. My
moat has to be the transfer-outcome data — which moves worked, which spoiled, which the GM
overrode — and that only accrues by shipping first.

**Q4. "Do I have to rip out MarketMan?"**

No, and I'd argue against it. We read your on-hand and recipes and write the transfer back as a
native MarketMan transfer so your COGS stays correct. You keep your invoice scanning, your EDI, your
accounting export. We're the layer that decides; they stay the layer that records. If you're on
spreadsheets, we're your first system — but then you're paying the onboarding cost of building
recipe BOMs, and I'd rather tell you that now than in week six.

**Q5. "Why won't Toast just build it? They own the sales data."**

They might, but their inventory product is deliberately per-location — operators asking in Toast's
own community forum how to move items between units are told there's no built-in function. Toast's
strategic centre is the transaction and the payment; the multi-location supply decision is an
above-store workflow with a different buyer inside the same company. That's the same reason POS
vendors ceded invoice OCR to xtraCHEF and then bought it. The realistic outcome here is acquisition,
not organic displacement.

---

## 9. What would genuinely threaten Mise

Ranked by how much it should actually worry the founder.

| # | Threat | Why it is serious | Early warning signal |
|---|---|---|---|
| 1 | **Crunchtime adds cross-location netting to its recommendation engine and moves downmarket** | They already have the hardest half — the forecast — running in 150,000 locations, plus transfer rails and the distribution relationships ([Crunchtime](https://www.crunchtime.com/)) | A Crunchtime release note for a "suggested transfer" or "network par"; a sub-10-unit SKU |
| 2 | **Supy closes the loop** | Structurally closest: already aggregates outlet demand into one consolidated supplier order ([Supy](https://supy.io/blog/learn-standing-orders-recurring-supplier-orders-restaurants)) and already has request→approve→dispatch→receive transfer rails ([Supy](https://supy.io/product-features/inventory-transfers)). They need one join, not one product | Any Supy copy that says *suggested* or *recommended* transfer |
| 3 | **Count discipline in the target segment is too poor for automated decisions to be trustworthy** | Not a competitor — the market risk. If a 9-unit group counts monthly, a rebalancing proposal is built on a number weeks stale. This kills the product regardless of what anyone else ships | Pilot data: proposal acceptance rate, and how often accepted transfers are found not to exist |
| 4 | **AI-native full-stack entrants with real capital** | Nory ships ingredient-level forecasting and an Ordering Assistant today and frames cross-site transfers as the operator's job ([Nory](https://www.nory.ai/blog/multi-site-restaurant-inventory-management)) — one product decision from competing directly. Owner raised $240M for an AI-native restaurant platform ([Restaurant Business](https://www.restaurantbusinessonline.com/technology/owner-raises-240m-ai-native-restaurant-tech)) | A competitor's landing page using the word "rebalance" |
| 5 | **The supply side agentifies first** | YC-backed entrants are attacking this from the distributor end — Kaso aggregating restaurant demand to negotiate chain-level pricing, Burnt/Ozai replacing order management inside distributors ([YC Supply Chain](https://www.ycombinator.com/companies/industry/supply-chain)). If the distributor's agent optimises the group's order, it captures the same value from the other side | Distributor-side AI ordering announcements from Sysco / US Foods / PFG |
| 6 | **Transfers turn out to be operationally cheap to ignore** | The unspoken assumption is that moving a case between branches beats buying one. If drive time, labour and cold-chain risk exceed the ingredient's margin, the whole thesis is a rounding error for anything but high-value proteins and seafood | Pilot: measured saving per executed transfer vs. fully-loaded cost of the move |
| 7 | **R365 or Toast acquires the capability** | Both have the balance sheet; R365 raised $135M at $1B ([R365](https://www.restaurant365.com/in-the-news/restaurant365-announces-135m-funding-round-co-led-by-kkr-and-l-catterton/)); Toast has repeatedly bought rather than built in this layer | An acquisition in the multi-location inventory space |

**The one that should keep the founder up at night is #3**, not #1. Competitive threats are visible
and slow. A product whose core decision rests on an on-hand number the customer does not maintain
fails quietly, at pilot, and looks like a sales problem.

---

## 10. Claims audit — what to say and what not to say

| Say this | Don't say this |
|---|---|
| "MarketMan records transfers — that's their word" (linked) | "MarketMan doesn't have transfers" — **false, they do** |
| "Crunchtime's transfer training is five courses, all starting with 'Create'" (linked PDF) | "Crunchtime can't forecast" — **false, they forecast well** |
| "Crunchtime averages 176 locations per brand" (arithmetic from their own figures) | "Nobody uses inventory software" — **false and easily refuted** |
| "45% of restaurants used inventory software in Toast's 2019 survey" (dated, say so) | "42% still use pen and paper" — **unattributed, do not use** |
| "R365's published floor is around $499/location third-party; they don't publish list" | "R365 costs $499" as fact — **they publish nothing** |
| "I haven't found anyone shipping auto-promotion of near-expiry stock" | "Nobody does auto-promotion" — **absence of evidence** |
| "They could build this; my advantage is focus and timing" | "They architecturally cannot build this" — **overclaim** |
