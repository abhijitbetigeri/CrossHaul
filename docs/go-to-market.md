# Mise — go-to-market

Companion to [market-research.md](market-research.md) (TAM, competition, pricing) and
[financial-model.md](financial-model.md) (P&L, unit economics, CAC). Where those two documents
establish *that* the market exists and *what* it is worth, this one is the operating plan for
reaching it from a standing start.

**Starting position, stated plainly.** Zero customers. Zero customer discovery. No operator has
agreed to pay. No pilot, no letter of intent, no design partner. Everything below is a plan to
change that, beginning this month, executed by one person. Numbers are either sourced (linked) or
labelled an **assumption**.

---

## 0. The constraints this plan has to live inside

The financial model already commits to specific numbers. A GTM plan that quietly needs different
ones is not a plan, it is a second model. These are binding:

| Constraint | Value | Source |
|---|---|---|
| Price | $249 / location / month | [financial-model.md](financial-model.md) |
| Average group | 6.0 locations → ~$17,900 ACV | same |
| Year-1 groups signed | 17 | same |
| Year-1 CAC | $2,000 per group → **$34,000 total S&M** | same |
| Years 2–3 CAC | $5,500–6,000, two AEs at ~5 groups/month each | same |
| Gross profit per group | $1,358 / month | same |
| CAC payback | 4.0 months | same |

Three consequences follow immediately, and they shape everything below.

1. **Year-1 sales spend is $34,000 in total — roughly $2,800 a month.** The founder's own time sits
   in the $210K year-1 operating expense line, not in CAC, which is why $2,000 per group is
   arithmetically reachable. But it means no paid acquisition, no exhibition booth, no SDR, and no
   $30K/year data subscription. Every channel in §2 is ranked against that number.
2. **17 groups in twelve months is roughly one signature every three weeks**, founder-led, while
   also building the product. §7 load-tests whether one person can do that.
3. **Mise cannot run a single-location pilot.** The product's value is a transfer between branches;
   one branch has no counterparty. The minimum demonstrable deployment is a *cluster* of two to
   three units. This is not a detail — it removes the standard vertical-SaaS land motion and forces
   the wedge in §3.

---

## 1. Beachhead

### 1.1 The filter, not the adjective

"Mid-market restaurant groups" is not a segment, it is a size band. The segment is defined by six
conditions, and a prospect failing any one of them is disqualified rather than nurtured.

| # | Filter | Threshold | Why it is load-bearing |
|---|---|---|---|
| 1 | Unit count | 3–20 | Below 3 there is no counterparty. Above 20, Crunchtime and Restaurant365 compete directly and a buying committee appears. [63.5% of multi-concept companies run under 20 units](https://restaurantchains.net/multi-concept-restaurant-operators-emerging-chains/) |
| 2 | **Geographic clustering** | ≥3 units within a 45-minute drive | A transfer only beats a purchase if the van trip costs less than the marginal delivery. This is the binding physical constraint on the product and it is the filter most likely to be underestimated |
| 3 | Concept overlap | 1–3 concepts sharing ≥40% of SKUs by spend | Surplus is only fungible where the bills-of-materials overlap. Two concepts with disjoint ingredient sets are two separate transfer graphs |
| 4 | Menu perishability | Fresh-prep, produce-forward — bowls, salads, Mediterranean, Mexican, poke, pizza, juice | [Food waste runs ~$72,000 per location per year, 4–10% of food purchased](https://oysterlink.com/spotlight/restaurant-food-waste-statistics/), but it is concentrated in short-shelf-life SKUs. Frozen-heavy QSR has low spoilage and little to transfer |
| 5 | POS | Toast, Square, Lightspeed or Revel — cloud, API-accessible | The forecast needs item-level sales history. A legacy on-premise POS turns onboarding into a services project and destroys the 76–84% gross margin |
| 6 | Purchasing autonomy | Independent group, or a franchisee whose franchisor does not mandate a supply-chain stack | A franchisee locked to an approved-vendor list cannot buy, however much they want to |

Filters 2 and 3 are the ones that matter and the ones a generic plan omits. The sector's
[median multi-concept operator runs 3 concepts, 13 units, across 2 states](https://restaurantchains.net/multi-concept-restaurant-operators-emerging-chains/) —
so the *median* operator is a poor fit for Mise, because 13 units across 2 states is two or three
disconnected transfer graphs, not one. The beachhead is the clustered subset, and naming that
honestly up front is cheaper than discovering it in month six.

### 1.2 Geography: the San Francisco Bay Area, then Sacramento and Los Angeles

**The honest reason first: the founder lives here.** At $2,000 all-in CAC and founder-led selling, a
customer you can drive to is the only affordable customer. A single round-trip flight is a sixth of
the annual sales budget. Any GTM document that claims a metro was chosen on market-structure grounds
when the founder happens to live in it is being dishonest about the strongest reason.

The supporting reasons are real but secondary:

- **Density.** [San Francisco alone holds roughly 3,900–4,400 restaurants](https://oysterlink.com/spotlight/restaurants-san-francisco-bay-area/),
  and the wider nine-county area several times that. Walk-in prospecting (§2) only works where 25
  qualified doors fit inside one afternoon's driving.
- **Clustering.** Bay Area fast-casual groups are typically strung along a 40-mile corridor —
  Mission to Downtown to Berkeley to Oakland — which is exactly the geometry filter 2 requires.
- **Cost of goods.** Waste at 4–10% of purchases costs more in absolute dollars in the most
  expensive food market in the country, so the ROI argument is strongest here.
- **A tight, association-mediated operator community**, so a single reference travels.

And the counter-argument, which a judge will raise: [the number of restaurants in San Francisco has been shrinking](https://pos.toasttab.com/blog/on-the-line/number-of-restaurants-in-san-francisco-shrinking).
A beachhead in a contracting market imports churn. Two mitigations: target groups that are
*opening* units — nationally there were
[3,381 planned locations across the 1→2 through 18→19 unit transitions in 2026](https://www.restaurantnews.com/restaurant-growth-in-2026-extends-from-second-locations-to-19-units-080326/) —
and widen to Sacramento and Los Angeles from month 6, both drivable and both structurally cheaper
markets.

### 1.3 How big the beachhead actually is *(constructed — assumption chain shown)*

```
   750,000  US restaurant locations                                [sourced, market-research.md §1]
×      2.0% Bay Area share of US locations                         [assumption: 1.4% of population,
                                                                    uplifted for dining density]
=   15,000  Bay Area locations
×       30% multi-unit share                                       [sourced, market-research.md §2]
=    4,500  multi-unit locations
×       40% locally-owned 3–20 unit groups, not national chains    [assumption]
=    1,800  locations
÷      6.0  average group size                                     [financial model]
=      300  candidate groups
×       50% pass the clustering, perishability and POS filters     [assumption — the one to test]
=     ~150  qualifying Bay Area groups
```

**150 groups × 6 locations × $2,988 = ~$2.7M of beachhead ARR.** The year-1 target of 17 groups is
therefore 11% penetration of a single metro in twelve months, which is too aggressive to plan
against. §4's funnel needs a qualified list of ~430 groups. The Bay Area does not contain that.
**This is why the geography widens by month 6, and it is falsifier #2 in §8.** The week-1 list build
measures the 50% filter rate directly rather than assuming it.

---

## 2. First ten customers: the channels, ranked

Ranked by cost per qualified first meeting and time to the first one, under the $34,000 ceiling.
Yields are assumptions and are re-forecast from real rates in week 4.

| Rank | Channel | Cash cost / meeting | Time to first meeting | Yield in 90 days *(assumption)* | Verdict |
|---|---|---:|---|---:|---|
| 1 | **Afternoon walk-in at the flagship unit** | ~$4 (parking, coffee) | Days | 25 meetings | The core motion |
| 2 | **Restaurant-specialist bookkeepers, CPAs, fractional CFOs** | $0 up front, 15% of Y1 ACV on close | 2–4 weeks | 4 meetings | Highest-trust, lowest-cash |
| 3 | **Individual distributor sales reps (DSRs)** | ~$20 (lunch) | 2–4 weeks | 3 meetings | Underrated; see §6 |
| 4 | **GGRA / CRA associate membership and events** | ~$150 | 3–6 weeks | 4 meetings | Access and credibility, not volume |
| 5 | **Targeted LinkedIn outreach to "Director of Operations"** | ~$15 | Days | 6 meetings | Works, but low reply rate without a reference |
| 6 | **Trade shows — attend, do not exhibit** | ~$400 | Months | 0 in 90 days | 2027 line item |
| 7 | **POS partner marketplaces (Toast)** | n/a | 9–12 months | 0 | Build the integration anyway; ignore as a channel |
| 8 | **Operator communities online (Reddit, Facebook, LinkedIn groups)** | ~$0 | Weeks | 1 | Mostly single-unit operators and job seekers |
| 9 | **Franchise brokers and consultants** | n/a | n/a | 0 | Wrong motion entirely — see §6 |
| 10 | **Paid search / LinkedIn ads** | $300–800 | Days | 0 | Excluded. Competing on CPC with Restaurant365 on a $2,800/month budget is arithmetic suicide |

### 2.1 The walk-in, in detail, because it is the plan

Multi-unit operators are unreachable by email and entirely reachable between 2:00 and 4:00pm, when
the lunch rush has cleared and the dinner prep has not started. The founder is not selling to the
person behind the counter. The objective of a walk-in is one name.

> "I'm building something for groups your size — I saw you've got four locations. Who handles the
> ordering across all of them? And when one runs short mid-service, what actually happens — do they
> call the other branches?"

The second question is the qualification. If the answer is "yes, they call Berkeley", the prospect
has just described the manual version of the product and the meeting is nearly booked. If the answer
is "we just get an emergency drop from Sysco", the operator is paying for the problem in freight and
does not know it. If the answer is a blank look, the units are too far apart and filter 2 has failed
— disqualify on the spot and drive to the next one.

Throughput: 8–10 walk-ins per afternoon, three afternoons a week, is ~25 groups touched per week at
essentially zero cash cost. This is the only channel in the table that produces volume inside the
budget.

### 2.2 The accountant layer, in detail, because it is the leverage

Restaurant-specialist bookkeeping firms and fractional CFOs each serve 10–40 operators, review the
food-cost line every month, and already know which groups have a problem. They are the highest-trust
introduction available to a company with no customers.

There is a public comparable for what this is worth:
[Restaurant365 pays referral partners up to $5,000 for connecting a customer](https://www.restaurant365.com/partner-referral/).
Mise cannot pay $5,000 out of a $2,000 CAC, but it can offer **15% of first-year contract value**
(≈$2,700 on a six-unit group) paid on collection rather than on signature — which costs nothing
until it works and is therefore budget-neutral. Target: 12 firms approached in month 1, 3 producing
by month 6.

### 2.3 What is deliberately excluded, and why

- **Content marketing and SEO.** Twelve-month payback horizon against a twelve-month plan.
- **Paid acquisition.** See rank 10.
- **Exhibiting at trade shows.** A booth at FSTEC or MUFC runs into five figures before travel.
  Attending costs a pass and a flight, and 40 pre-booked coffees convert better than a booth for a
  company nobody has heard of.
- **"Restaurant tech" Slack and Discord communities.** They are populated by vendors selling to each
  other.

---

## 3. The wedge: the Cross-Branch Waste Audit

### 3.1 The problem with selling the platform first

A six-location group is being asked for $17,928 a year, plus an operational change — recipe BOMs
loaded, counts disciplined, vendor catalogues mapped — from a company with no customers. The
rational operator answer is no, and it is the correct answer. Worse, the standard risk-reducer does
not exist here: **a single-location pilot cannot demonstrate a transfer.**

So the first thing Mise sells is not the platform.

### 3.2 The offer

**A fixed-fee, three-week, read-only audit of the last 90 days.** List price $2,500 for up to six
locations. The first ten operators pay **$500** as a founding-operator rate. On signature of a
subscription within 60 days, the fee is credited in full against implementation — which is otherwise
billed at $2,500, and which MarketMan charges
[$500 for](https://restaurantinventorytools.com/restaurant-inventory-software-cost/).

**Why paid rather than free.** A free audit is accepted by people who will never buy, and the
founder's hours are the scarcest resource in the company. A $500–2,500 fee is small enough to clear
without a business case and large enough that the person who signs it has to be in the room — which
is the thing actually being purchased: a qualified meeting with the economic buyer, at a positive
price.

**What the operator hands over** — one page, no installation, no IT involvement:

| Input | Where it comes from | Effort |
|---|---|---|
| 90 days of item-level sales, per location | POS export (Toast, Square, Lightspeed) | 10 minutes |
| 90 days of distributor invoices | Sysco / US Foods / PFG portal download or PDF | 20 minutes |
| Current recipe cards or menu with build sheets | Whatever exists, however messy | 30 minutes |
| Last two physical counts per location | Spreadsheet or inventory system export | 15 minutes |

**What comes back** — a six-page document and a 45-minute readout with the owner present:

1. **Per-SKU, per-location spoilage and stockout exposure in dollars**, ranked. Computed from their
   invoices against their sales, not from an industry average.
2. **The retro-transfer ledger** — the specific transfers that should have happened and did not.
   *"On 14 August, Berkeley held 38 lb of avocado two days from spoil while Mission bought 40 lb
   fresh at $1.85/lb. That is $74. There were 61 more like it in 90 days."* With a dollar total and
   an annualised figure.
3. **Consolidated-PO analysis** — how many separate purchase orders went to how many vendors, how
   many were emergency small drops, and what the same basket costs as one planned order.
4. **A forecast backtest** — Mise's per-SKU accuracy on a held-out final 30 days of their own data.
   A measurement, not a promise.

### 3.3 Why this is the right wedge

- **It converts the sale from faith to arithmetic.** The buyer is not evaluating a forecasting claim.
  They are reading dated, priced events from their own invoices, which they can walk into their own
  walk-in and verify. Mise becomes checkable.
- **It requires no new engineering.** It is the existing pipeline — BOM explosion, forecast,
  rebalance — pointed backwards at history rather than forwards at next week.
- **It is the customer discovery the financial model names as its honest weakness.** Fifty audits is
  fifty operators' real data and fifty conversations about price, delivered as a paid engagement
  rather than as a favour.
- **It survives a "no".** An operator who declines the subscription has still paid, still handed
  over data, and still told the founder why. Nothing else in the plan produces a useful loss.

### 3.4 What it costs and what it must convert at

| | Value | Note |
|---|---:|---|
| Founder time per audit, once tooled | ~7 hours | **Assumption**, load-tested in §7.4 |
| Hard cost per audit (invoice parsing, inference) | ~$175 | Budgeted in §7.5 |
| Audit → paid subscription | **1 in 3** | **Assumption.** Falsifier #4 |
| Audits required for 17 groups | ~51 | ≈1 per week, all year |

**Audit fees are excluded from the financial model's revenue line and treated as a CAC offset.** The
model does not depend on them. If audit cash lands materially above the ~$30,000 assumed, year-1 net
burn comes in below the modelled $162,634 — but services revenue should not be capitalised into a
SaaS model, so it is deliberately not counted.

---

## 4. Sales motion and cycle

### 4.1 Who is in the room

| Role | Title in a 3–20 unit group | What they care about | Behaviour in the deal |
|---|---|---|---|
| **Champion** | Director of Operations, Ops Manager, or simply "the person who does the ordering" | Their Tuesday afternoon. In a six-unit group one person often runs purchasing, scheduling and vendors | Mise deletes their worst recurring task — the 4pm ring-round. They will champion it hard |
| **Economic buyer** | Owner, managing partner, or controller | Food cost as a percentage, and cash | Usually one or two people, frequently the person who founded the group. Signs personally |
| **Technical gatekeeper** | *Usually does not exist* | — | A six-unit group has no IT function. The POS vendor and the bookkeeper are the de facto IT department |
| **Operational blocker** | Chef or GM at the donor branch | Their own food-cost percentage and their own par levels | Loses stock to another branch. If the accounting is wrong they quietly refuse to load the van. See §8, falsifier #3 |
| **Incumbent blocker** | Whoever sold them MarketMan or MarginEdge | Renewal | Real, and handled by not competing with it in year 1 — see §4.4 |

The absence of a technical gatekeeper is the single biggest structural advantage of this segment
over enterprise. In enterprise restaurant tech,
[operations, finance, IT/security, legal and procurement all have to align before consensus, which is precisely what lengthened cycles](https://onegoalconsulting.com/blog/the-enterprise-restaurant-tech-sales-cycle-in-2025-what-worked-what-didnt-and-how-vendors-win-in-2026).
In a six-unit group, the champion and the signer are frequently the same person or sit at adjacent
desks.

### 4.2 The stages

| Stage | Elapsed | Exit criterion | Drop-off risk |
|---|---|---|---|
| Qualify | Week 0 | Passes all six filters in §1.1; name of the person who does the ordering | Low — disqualify aggressively |
| First meeting — 30 min, on site, 2–4pm | Week 1 | Verbal agreement to send 90 days of data | Medium |
| Data handover | Weeks 1–2 | Files actually received | **Highest.** Budget for three chases and a screen-share to do the POS export together |
| Audit delivered + readout | Week 4 | Owner in the room; dollar figure on the retro-transfer ledger | Low |
| Proposal | Week 5 | Cluster pilot: 3 units, 90 days, full price, 30-day termination | Medium |
| Signature | Weeks 6–9 | Annual term, monthly billing, per-location | Medium |

**6–9 weeks** from first meeting to signature for an independently owned group. **10–16 weeks** where
a franchisor's approved-vendor review is involved — which is one reason filter 6 exists.

Commercial terms: annual term, billed monthly, priced per location so adding a unit is a line change
rather than a renegotiation. No setup fee for the first ten customers. Thirty-day termination during
the 90-day cluster pilot, because the operator's real objection is not price, it is being stuck.

### 4.3 The funnel to 17 groups *(all rates are assumptions; re-forecast from real data in week 4)*

| Stage | Count | Rate | Weekly tempo |
|---|---:|---:|---|
| Qualified groups on the list | 430 | — | Built in weeks 1–4, extended from month 6 |
| Contacted | 300 | 70% | ~6 / week |
| First meeting held | 90 | 30% | ~1.7 / week |
| Audit agreed | 65 | 72% | ~1.3 / week |
| Data received and audit delivered | 51 | 79% | ~1 / week |
| **Paid cluster pilot signed** | **17** | **33%** | **~1 per 3 weeks** |

This reconciles exactly to the financial model's 17 groups. It also exposes the plan's two real
dependencies: a qualified list of 430 groups (see §1.3 and falsifier #2), and an audit conversion of
one in three (falsifier #4).

### 4.4 Positioning against the incumbent, and what not to say

If the prospect already runs MarketMan or MarginEdge, do not attempt a rip-and-replace in year 1.
[Most multi-location operators already run between five and ten separate platforms](https://www.marginedge.com/blog/6-best-tech-solutions-for-multi-location-restaurants);
an eleventh that replaces one of them is a project, and a project is a committee.

Mise sits **above** the system of record. The line is:

> "Keep your inventory system. It records what happened. Mise decides what should happen next, and
> writes the transfer back into it."

The differentiation claim must be stated the way [market-research.md §3](market-research.md) states
it, because the overclaim is catchable:
[MarketMan does ship inter-location transfers](https://www.marketman.com/platform/multi-unit-restaurant-commissary-kitchen-inventory-software) —
on the Enterprise tier, as bookkeeping for a decision a human already made. The two true claims are
that **the system decides** rather than records, and that **a six-unit operator cannot buy automated
transfers at mid-market pricing today**. Anything beyond those two is a liability in the room.

---

## 5. Land and expand

### 5.1 The ladder

| Stage | Scope | Monthly price | Duration | Gate to the next stage |
|---|---|---:|---|---|
| 0 — Audit | Whole group, read-only, historical | $500 / $2,500 one-off | 3 weeks | Retro-transfer ledger ≥ ~$8,000 / location / year |
| 1 — **Cluster pilot** | The 3 units closest together | $747 | 90 days, 30-day out | Transfers actually executed, not just proposed; PO count down; the champion says it removed the ring-round |
| 2 — Concept rollout | Every unit of that concept | $1,494 at 6 units | Annual | Forecast accuracy holding at scale; supplier PO consolidated |
| 3 — Second concept | The group's other brands | Same per location | Annual | Shared-SKU map across concepts exists |
| 4 — New openings | Each new unit auto-added | Same | — | — |

**Stage 1 is a cluster, not a location.** Repeating the point from §0 because it inverts the usual
land motion: the smallest thing Mise can sell is three units, so the "land" is already $8,964 of
ARR. That is a higher bar to entry than a typical seat-based product and a materially better
starting ARR when it clears.

### 5.2 The arithmetic of expansion inside one logo

```
3-unit cluster pilot          →  $8,964 ARR
6-unit concept rollout        → $17,928 ARR   (2.0×)
13-unit multi-concept group   → $38,844 ARR   (4.3× the landing position)
```

Thirteen units is the [sector median for a multi-concept operator](https://restaurantchains.net/multi-concept-restaurant-operators-emerging-chains/).
The financial model assumes average group size drifts only from 6.0 to 6.5 locations — which is a
deliberately conservative reading of a 3→13 path, and means **expansion within existing logos is
upside the model does not take credit for.** That is the right way round.

### 5.3 The compounding mechanic, and the one that does not exist

Within an account, density compounds: the moment a group's second concept shares a produce vendor
with the first, the transfer graph roughly doubles in edges without adding a single unit. Value per
location rises with account maturity, which is the argument for negative net revenue churn.

**Across accounts, there is no network effect, and Mise should not claim one.** Two unrelated
operators will not transfer stock to each other — food safety, liability and licensing all forbid
it, and no operator wants their avocados coming from a competitor's walk-in. An inter-company
marketplace is not a roadmap item, it is a regulatory problem wearing a roadmap's clothes. The moat
is the per-SKU forecast substrate and the accumulated transfer history inside each account, not a
network.

---

## 6. Channels and partnerships: what is real, and what is a year-3 fantasy

| Partner | The pitch-deck version | What is actually available pre-seed | Earliest realistic |
|---|---|---|---|
| **Sysco / US Foods / PFG, corporate** | DSRs carry Mise into their accounts nationally | Nothing. See below | Year 3, and via data, not sales |
| **Individual DSRs** | — | One rep at a time, over lunch, for their own book | **Now** |
| **Toast / Square / Lightspeed** | Featured marketplace placement drives inbound | A long certification process you should start anyway, for the data | Leads from month 9–12 |
| **Restaurant accountants and fractional CFOs** | — | Referral agreements, paid on collection | **Now** |
| **Franchise brokers and consultants** | Channel to thousands of franchisees | Wrong motion entirely | Never, as stated |
| **Franchisee advisory councils, multi-unit franchisee associations** | — | Reachable at MUFC | Year 2 |
| **GGRA / CRA** | — | Associate membership | **Now** |
| **MarketMan / MarginEdge as integration partners** | — | Technical integration, not a commercial channel | Year 2 |

### 6.1 The distributor partnership, honestly

The programmes exist. [Sysco runs a Solutions Partners programme in which partner products are promoted, co-marketed and sold to Sysco's customers](https://www.solutions.sysco.com/strategize-operations).
But the reality behind the branding is thinner than it sounds: Restaurant365 — a company at
[~$132M ARR and 40,000 customers](https://getlatka.com/companies/restaurant365) — has a
[public Sysco partner page that describes Sysco purely as a food and beverage vendor and discloses no commercial arrangement at all](https://www.restaurant365.com/partners/sysco/).
If that is what the category leader's distributor relationship looks like in public, a pre-seed
company with zero customers will not get a national distributor's channel team on a call.

There is also a structural conflict that has to be said out loud rather than hidden: **Mise's core
value is that the customer buys less.** A transfer that covers a shortage is an order the
distributor does not receive. Any pitch that presents Sysco as a natural partner without naming that
is not credible.

The honest framing — and it is genuinely true, not a dodge — is that the *composition* of the
distributor's business improves even as gross volume dips slightly: fewer unplanned emergency small
drops, more consolidated planned orders, better margin per delivery, better forecastability. That
argument is winnable with an individual DSR who owns thirty accounts and is measured on them. It is
not winnable with a national channel team before there is data to prove it.

**What to do now instead.** DSRs are described by their own trade body as
[the face of foodservice distribution companies in the marketplace and trusted business partners of restaurant and foodservice operators](https://ifdaonline.org/food-distributor-jobs/foodservice-sales/).
Buy three of them lunch in month 2. Each covers 25–40 Bay Area accounts and can name the ones with
multiple locations and a food-cost problem. And note that distributor *data* — invoices, order
guides, EDI — requires no partnership whatsoever: the customer forwards their own invoices or grants
their own portal access.

### 6.2 The POS marketplace, honestly

Toast operates a closed partner ecosystem — [apply, get vetted for business fit and technical readiness, sign a partner agreement, build against a sandbox, pass certification, and only then receive production credentials](https://www.directorders.com/blog/toast-partner-api-restaurant-guide),
with monetisation that reportedly spans API access fees, per-location fees and revenue share. That
is a multi-month process, a platform tax, and a distraction if treated as a lead source.

But the integration itself is **mandatory regardless**, because the forecast cannot exist without
item-level sales history. So: build the Toast integration in months 1–4 because the product requires
it, submit the partner application in month 4 because it is nearly free once the integration exists,
and forecast zero marketplace leads in year 1. Marketplaces convert well for categories buyers
already search for. Nobody searches for "automated inter-branch stock rebalancing."

### 6.3 Associations and events, honestly

- **[Golden Gate Restaurant Association](https://ggra.org/restaurants/)** — associate membership is
  the category for businesses supplying the industry. Year-round programming, the Industry
  Conference, Eat Drink SF. Buys access and standing, not volume. Join in week 2.
- **[California Restaurant Association](https://www.calrest.org/benefits-membership)** — same logic,
  state-wide, useful when the geography widens to Sacramento and Los Angeles.
- **[FS/TEC](https://informaconnect.com/fstec/event-info/)** — 23–25 September 2026, Gaylord Texan,
  Grapevine, Texas, [drawing 1,000–2,000 attendees](https://www.restaurantdive.com/news/restaurant-industry-shows-conferences-2026/761093/).
  **Skip 2026.** It is four days away, would consume roughly 10% of the annual sales budget, and the
  founder has nothing to show. Attend in 2027 with three references.
- **[Multi-Unit Franchising Conference](https://www.multiunitfranchisingconference.com/)** — 27–30
  April 2027, Caesars Forum, Las Vegas. The highest concentration of multi-unit franchisees in the
  United States in one building. This is the single event on the calendar that matters, and the
  year-2 budget should reflect that.

### 6.4 Why franchise brokers are the wrong answer

Franchise consultants and brokers sell franchise *ownership* to prospective franchisees. Their buyer
is a person who does not yet operate a restaurant. That is the opposite end of the lifecycle from a
group already running six units with a food-cost problem. The adjacent thing that is genuinely
useful — franchisee advisory councils and multi-unit franchisee associations — is reached through
MUFC, not through brokers, and is a year-2 activity.

---

## 7. The first 90 days

Today is 19 September 2026. Week 1 begins Monday 22 September.

### 7.1 Month 1, week by week

**Week 1 (22–28 Sep) — Build the list. Sell nothing.**

- Construct the qualified-group list from public data rather than a paid database. [Brizo, the standard foodservice prospecting tool, prices as an annual subscription starting at five user licences](https://brizodata.com/en/pricing/) —
  out of reach on $2,800 a month, and unnecessary at this scale.
  - County environmental health permit registers (San Francisco, Alameda, San Mateo, Santa Clara)
    publish permitted food facilities with the owning entity.
  - California Secretary of State entity search collapses multiple addresses onto one owning LLC.
    **One legal entity against three or more permit addresses is the multi-unit signal.**
  - Google Places for cuisine and concept; the operator's own site for a locations page; POS
    detection from their online-ordering page.
- Score every candidate against the six filters in §1.1 and record drive-time clustering explicitly.
  **Target: 120 scored groups, and a measured filter pass-rate to replace the 50% assumption in §1.3.**
- Stand up the operating kit: free CRM, booking link, one-page mutual NDA, a one-page data-request
  sheet, and the audit document template.
- Decide and record: skip FS/TEC 2026. Diary FS/TEC 2027 and MUFC 27–30 April 2027.

**Week 2 (29 Sep – 5 Oct) — Thirty conversations.**

- 25 walk-ins across Tuesday, Wednesday and Thursday, 2:00–4:00pm, at the flagship unit of 25 listed
  groups. Objective is one name per group, not a pitch.
- Five follow-up emails or LinkedIn messages per day to the named operations person, referencing the
  walk-in by date and location.
- Join GGRA as an associate member. Register for the next association event.
- Email twelve Bay Area restaurant-specialist bookkeeping and CPA firms with the 15%-of-first-year
  referral offer.
- **Exit: 6 first meetings booked.**

**Week 3 (6–12 Oct) — Sell the first audits.**

- Hold the six meetings. Thirty minutes, on site, 2–4pm. **Do not open with a demo.** Open with
  "when a branch runs short mid-service, what actually happens?" and let them describe the ring-round
  in their own words. Then show the retro-transfer ledger *format* — a sample page — rather than the
  product.
- Ask for the audit: $500, three weeks, read-only, and hand over the one-page data list.
- Deliver the first audit end to end for whichever group returns data fastest, including over the
  weekend. The first audit is a product test as much as a sale, and everything downstream is
  calibrated on how long it really takes.
- **Exit: 4 audits agreed, 2 data sets received, 1 audit substantially built.**

**Week 4 (13–19 Oct) — First readouts, and replace the assumptions.**

- Deliver the first two audits and run the readouts with the owner in the room.
- Write down verbatim what the owner says the ledger number is worth, and what they say is wrong
  with it. This is the customer discovery the financial model names as its honest weakness, and it
  is the highest-value output of the month.
- **Price-test explicitly, in every readout:** *"If this ran forwards instead of backwards, at $249
  per location per month, is that a yes?"* Record the answer, not an impression of it.
- Re-forecast §4.3 from measured rates. Delete the assumptions that survived contact and keep the
  ones that did not, labelled.
- **Exit: one paid cluster pilot signed, or a written, named reason why not.**

### 7.2 Months 2 and 3

| | Month 2 (Oct–Nov) | Month 3 (Nov–Dec) |
|---|---|---|
| Walk-ins | 60 | 60 |
| First meetings | 12 | 13 |
| Audits delivered | 8 | 8 |
| Paid groups signed | 1 | 1 |
| Product | Toast integration build; partner application submitted | Transfer accounting at donor book value (see §8 #3) |
| Channel | First accountant referral in pipeline; three DSR lunches | Audit price to $2,500 once three references exist |
| Geography | Bay Area only | List extended to Sacramento and Los Angeles |
| Evidence | First written case study from pilot 1, anonymised if required | Verdict on the 1-in-3 audit conversion |

### 7.3 Day-90 exit criteria

| Metric | Target | What it proves |
|---|---:|---|
| Qualified groups on list | 250 | The beachhead exists at the assumed density |
| First meetings held | 25 | The walk-in channel produces volume |
| Audits delivered | 18 | One person can deliver the wedge at tempo |
| Audits → paid pilots | 3 | The 1-in-3 conversion assumption survives contact |
| Paid locations live | ~18 | ~$4,500 MRR, against a year-1 target of 96 locations |
| Readouts objecting at $249 | <50% | The price holds |
| Median retro-transfer ledger | ≥$8,000 / location / year | **The product is worth buying at all** |

Three signed groups in the first quarter is consistent with the financial model's own description of
year 1 as "roughly three per quarter after a slow start": 3 + 4 + 5 + 5 = 17.

### 7.4 Can one person actually do this? *(the load test)*

| Activity | Hours / week |
|---|---:|
| Walk-ins and travel (3 afternoons) | 6.0 |
| First meetings (1.7/week, including travel) | 4.0 |
| Audit production (1/week at ~7 hours) | 7.0 |
| Readouts and follow-up | 2.0 |
| Channel work (accountants, DSRs, associations) | 2.0 |
| **GTM total** | **21.0** |
| Product, engineering, everything else | 30–35 |

Roughly 21 hours a week on go-to-market and the remainder on product is a demanding but survivable
solo-founder allocation. It is also the binding constraint on the plan: the audit at seven hours is
what makes it fit. If the first audit in week 3 takes twenty hours and does not fall towards seven
by the fifth, the tempo in §4.3 is unreachable and the wedge has to be narrowed — probably to the
retro-transfer ledger alone, dropping the consolidated-PO analysis and the backtest.

### 7.5 Where the $34,000 goes

| Line | Year 1 | Note |
|---|---:|---|
| Audit delivery — invoice parsing, inference, storage | $9,000 | ~51 audits at ~$175 |
| Conferences — FS/TEC 2027, MUFC 2027, two regional, travel | $11,000 | Attend, do not exhibit |
| Travel, parking, meals for on-site visits | $4,800 | ~120 site visits at $40 |
| Prospecting and enrichment tooling | $3,600 | Public-register scraping, contact enrichment. Not Brizo |
| Association memberships — GGRA, CRA, local chambers | $2,400 | Access and standing |
| CRM, scheduling, e-signature, call recording | $1,800 | Free and near-free tiers |
| Contingency | $1,400 | |
| **Total** | **$34,000** | Reconciles exactly to the financial model's year-1 S&M |

Referral commissions to accountants are excluded because they are paid on collection out of gross
profit, not from the acquisition budget.

---

## 8. What would falsify this

Ordered by severity. Each is stated as a claim that could be false, a test, a date, and a response.

### 1. The transfer is not worth doing *(fatal)*

**The claim.** A material share of a clustered group's shortages can be covered from a sister branch
more cheaply than by purchasing.

**Why it is fatal.** It is upstream of everything. If it is false, the pricing is wrong, the ROI
argument in [market-research.md §4](market-research.md) is wrong, CAC payback is wrong, and the
differentiation against MarketMan is irrelevant because there is nothing worth automating. Mise
costs $2,988 per location per year; if the median retro-transfer ledger comes back under roughly
$8,000 per location per year of recoverable value, operators will not change behaviour for a 2.5×
paper return on a task they consider already solved by a phone call.

**Test.** The first ten audits. **Known by day 90.** Computed from the operators' own invoices, so a
bad answer is unambiguous and cannot be argued with.

**Response if false.** The product is not a transfer engine, it is a consolidated-purchasing and
forecasting engine, which is a weaker and more crowded position — and that should be discovered from
ten operators' invoices for $1,750 of parsing cost, not from a year of building.

**This is the reason the audit is the wedge.** The most dangerous assumption in the company is also
the cheapest to test, and the 90-day plan is arranged to test it first, before another line of
product is written.

### 2. The clustered beachhead is too small

**The claim.** ~150 qualifying groups exist in the Bay Area and ~430 across three drivable metros.

**Why it matters.** The sector's
[median multi-concept operator spans two states](https://restaurantchains.net/multi-concept-restaurant-operators-emerging-chains/).
If dispersion is the norm rather than the exception, the 50% filter pass-rate in §1.3 is optimistic,
the qualified list needs five or six metros, and founder-led selling at $2,000 CAC breaks on travel
alone.

**Test.** The week-1 list build measures it directly. **Known by day 14** — the earliest and
cheapest test in the document.

**Response if false.** Either reprice for the dispersed case, or retarget operators who already run
a commissary — where the hub-and-spoke routing is
[already built and staffed](https://www.restaurant-hospitality.com/restaurant-operations/the-new-fast-casual-model-centralized-kitchens)
and Mise becomes the allocation brain on top of existing logistics rather than the thing that has to
invent them.

### 3. The donor branch refuses

**The claim.** GMs will execute transfers the system proposes.

**Why it matters.** The donor branch loses stock and, if transfers are not accounted for correctly,
takes the food-cost hit for a decision it did not make. Software that proposes transfers nobody
loads into a van has an execution rate of zero, produces no savings, and churns in month four —
which would show up as churn far above the modelled 1.0–1.5% monthly.

**Test.** Transfer execution rate in the first cluster pilot. **Known by day 60 of pilot 1.**

**Response if false.** A product change forced by a GTM failure: cost every transfer at the donor's
book value, credit it to the donor's P&L and debit the receiver's, and reduce the GM's interaction
to a single accept-or-decline tap. Build this in month 3 rather than waiting to be taught it.

### 4. The wedge does not convert

**The claim.** One audit in three becomes a paid subscription.

**Why it matters.** Below about one in five, hard cost alone runs past $2,000 per group before the
founder's time, and year-1 CAC is broken.

**Test.** ~18 audits by **day 120**.

**Response if false.** Diagnose before concluding the market is wrong: either the audit is reaching
the champion but not the signer (a targeting fix), or the audit output is interesting but not
decision-grade (an artefact fix — usually the ledger needs to name people and dates, not
categories). Only if both fail is the segment wrong.

### 5. $249 is the wrong price

**The claim.** A 25% premium over
[MarketMan's $199](https://restaurantinventorytools.com/restaurant-inventory-software-cost/) is
supported because Mise sells decisions rather than records.

**Test.** The explicit price question in every readout from week 4. If more than half object, the
premium is not real.

**Response if false.** Not a discount — a narrower SKU. Transfers-only at $149 per location per
month, sitting alongside whatever inventory system they already run. Lower ARPU, but it preserves
the positioning and it keeps the wedge intact.

### 6. MarketMan ungates transfers

**The claim.** A six-unit operator cannot buy automated transfers at mid-market pricing today.

**Why it matters.** Half the differentiation is a pricing gap, and a pricing gap can be closed with a
pricing page. The other half — that their transaction-and-periodic-count data model does not produce
the continuous per-SKU forecast a *decision* requires — survives, but it is the harder half to sell.

**Test.** Continuous monitoring of MarketMan's tier structure.

**Response if false.** Lead with automation rather than access, and accept that the sales
conversation gets harder. Speed of response matters more than the response itself.

### 7. Churn runs hotter than modelled

Not testable inside 90 days, and named because it cannot be. The model's 1.0–1.5% monthly is an
industry-shaped estimate with no customer evidence behind it, and the chosen beachhead is a metro
where [restaurant counts have been falling](https://pos.toasttab.com/blog/on-the-line/number-of-restaurants-in-san-francisco-shrinking).
The financial model already states that at 2.5% monthly, LTV/CAC falls to ~4× and remains viable.
The GTM mitigation is in §1.2: target groups that are opening units, not holding steady.

---

## 9. Summary

| | |
|---|---|
| **Beachhead** | 3–20 unit, fresh-prep restaurant groups with ≥3 units inside a 45-minute drive, on a cloud POS, with purchasing autonomy — Bay Area first, Sacramento and Los Angeles from month 6 |
| **Wedge** | A paid, three-week, read-only Cross-Branch Waste Audit that produces a dated, priced ledger of the transfers that should have happened |
| **Primary channel** | Afternoon walk-ins, then restaurant-specialist accountants on a 15% referral |
| **Champion** | The person who does the ordering. **Signer:** the owner |
| **Cycle** | 6–9 weeks, first meeting to signature |
| **Land** | A 3-unit cluster at $8,964 ARR — never a single location |
| **Expand** | Cluster → concept → second concept: 4.3× inside one logo |
| **Partnerships** | Accountants and individual DSRs now. Toast integration now, Toast leads never before month 9. Distributors corporately: year 3, and through data rather than sales |
| **Year-1 tempo** | ~6 contacts, ~1.7 meetings and ~1 audit per week; one signature every three weeks; 21 GTM hours a week |
| **The thing that breaks it** | If the median retro-transfer ledger comes back under ~$8,000 per location per year, none of the rest matters — and ten audits will say so by day 90 |
