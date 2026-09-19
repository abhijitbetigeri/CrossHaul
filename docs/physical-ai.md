# Physical AI and Robotics in Restaurant Supply Chain — A Feasibility Analysis

**Status:** internal technical analysis. Not a pitch document.
**Relationship to [`vision.md`](vision.md):** that document sets *pitch policy* — one slide, fifteen
seconds, at the Vision beat and nowhere else. This document is the substance underneath that policy.
Nothing here contradicts it; several sections make the case for it more precisely than a pitch can.
Where this analysis sharpens a claim made in `vision.md`, it is flagged explicitly (§5.6).

**Method and honesty about it.** Deployment figures below come from vendor press releases, SEC
filings, trade press, and academic literature, and are labelled by source type. Vendor-published
throughput and reliability numbers are marked as such and should be discounted; almost none of the
robotics claims in this sector have independent verification. Cost models in §6 are the author's own
arithmetic from published input prices, stated with assumptions visible so a reviewer can disagree
with a specific line rather than the conclusion. Where evidence is thin, the section says so.

---

## 1. The question, stated precisely

Mise is a decision layer. Branch agents forecast per-item demand, explode it through recipe BOMs,
detect shortage, search sister branches for surplus, and move goods laterally before buying. The
physical world enters at exactly one point: something has to actually carry the crate.

The question is not "will robots ever be in restaurants." It is narrower and answerable:

1. Is the physical leg of a Mise transfer a robotics problem, or a logistics problem with a human in
   it that costs less than any robot will for a decade?
2. Does the record Mise accumulates have training value for embodied systems, or is that claim
   an equivocation between two different kinds of data?
3. Is there any action the founder should take in the next 18 months on account of the answer?

The short answers, defended below, are: **no, mostly not, and almost none.** The longer answers
contain the parts worth knowing.

---

## 2. What is actually deployed today

### 2.1 The one place robots unambiguously work: distribution centres

Food distribution centres are the single stage of the chain where embodied automation is not a pilot.
The environment is indoor, climate-controlled, flat-floored, barcoded, palletised, dimensionally
regular, operated 16–24 hours a day, and staffed by workers whose loaded cost is well above
restaurant labour.

| System | Scale evidence | Source type |
|---|---|---|
| Symbotic AS/RS + SymBot case handling | >2 billion cases processed cumulatively; 84% of SymBots averaged >40 miles/day in 2025; deployed by Walmart, [UNFI](https://www.supplychaindive.com/news/united-natural-foods-launches-symbotics-ai-tech-distribution-centers/632854/), Associated Food Stores | [Vendor milestone release](https://www.symbotic.com/news/symbotic-announces-2025-milestones-processing-over-2-billion-cases-as-demand-for-physical-ai-accelerates/) — throughput and accuracy claims unverified |
| Locus Robotics AMRs (goods-to-person assist) | >350 sites worldwide as of April 2026; cold-chain hardware variant took HelloFresh from 100 to 500 temperature-controlled SKUs, with 26 additional robots added within three months | [Vendor/wire release](https://www.businesswire.com/news/home/20260623042232/en/Locus-Robotics-Helps-HelloFresh-Expand-Temperature-Controlled-SKU-Capacity-5X-Across-Growing-Brand-Portfolio) |
| Boston Dynamics Stretch (container unload, case pick) | Lidl deploying 22 units across NL/BE/AT/ES import warehouses by mid-2026; DHL fleet deal | [Trade press](https://www.mmh.com/article/after_pilot_program_grocery_company_lidl_rolling_out_fleet_of_22_robots_from_boston_dynamics_to_automate_container_unloading) |
| Amazon Robotics (Proteus AMR, Sparrow/Vulcan picking) | >1 million robots deployed network-wide, crossed mid-2025 | Company statements via [trade press](https://www.freightwaves.com/news/robots-drive-10b-amazon-investment-for-european-fulfillment-centers) |

The most informative number in that table is not a throughput figure. It is this: **Amazon's Sparrow
picking arm handles roughly 65% of the company's catalogue.** That is the state of the art in
general-purpose grasping, achieved by the best-resourced robotics organisation in the world, after a
decade, on rigid retail packaging, in a purpose-built environment with controlled lighting and
known item dimensions. The remaining 35% is deformable, irregular, or fragile — which is a
description of most food.

This is the correct anchor for any claim about manipulation in a kitchen. If 35% of *shrink-wrapped
retail goods* remains out of reach in the easiest environment that exists, a mobile manipulator
picking loose produce off a wet walk-in shelf is not a near-term engineering problem.

### 2.2 Transport: real, early, and not yet about food

Driverless long-haul is genuinely happening and is no longer a demo.

| Operator | Status (2026) | Source |
|---|---|---|
| Aurora | ~440,000 cumulative driverless miles as of end-June 2026; 10 driverless routes in the US Sun Belt; second-generation trucks launched | [Aurora IR](https://ir.aurora.tech/news-events/press-releases/detail/144/aurora-launches-second-generation-driverless-trucks-in-u-s-to-meet-customer-demand), [trade press](https://www.truckinginfo.com/news/aurora-heads-into-2026-with-big-plans-on-tap) |
| Kodiak | Driverless safety case 93% complete; 35 trucks running with no human in cab in the Permian Basin as of Q2 2026; long-haul commercial launch targeted year-end 2026 | [Trade press](https://www.truckinginfo.com/news/kodiak-says-driverless-long-haul-launch-on-track-for-2026) |

Note the scale. 440,000 driverless miles is roughly what **fifty** human long-haul drivers cover in a
year. The technology is past the demo stage and nowhere near the volume stage. And for food
specifically, the highway leg is the easy part: foodservice distribution is multi-stop, refrigerated,
requires liftgate unloading into a restaurant's back door, and often requires the driver to check the
delivery in with a manager. **The unsolved part of food freight is the last hundred feet, not the
highway** — and no autonomous trucking programme is working on it.

### 2.3 Last mile: deployed, but on a different problem

Sidewalk robots (Serve, Starship, Coco, Kiwibot) are in genuine commercial operation in a handful of
dense cities. Reported unit costs run [$18,000–$25,000 for LiDAR-equipped Serve
units](https://www.insidedeeptech.com/the-top-delivery-robot-companies-of-2026-compared/), with
vendor-side operating cost framed at $7–11 per robot-hour against $25–45/hr for a human courier.
Treat that comparison sceptically: it typically excludes remote-assist labour, field recovery,
vandalism, and the cost of the human who reloads the robot.

More importantly, this is not the Mise problem. A sidewalk robot carries one hot bag a few hundred
metres to a consumer. A Mise transfer carries a 10 kg crate — and realistically a batch of several —
across a city between commercial premises. Different payload, different range, different regulatory
class.

### 2.4 Kitchen automation: fixed stations only, and the revenue tells the story

This is where the evidence is most useful, because there is a financial filing.

**Miso Robotics (Flippy)** is the most visible kitchen robotics company in the US. Its audited
filings report **net revenue of $514,798 in 2025**, up from $384,676 in 2024, with **two customers
generating 100% of revenue**, and **10 third-generation Flippy systems deployed as of 31 March
2026** across White Castle, Insert Coin and Levy. Against that, 2025 financing produced $24.6M gross
and the current campaign had raised $29.3M by August 2026
([Kingscrowd analysis of DealMaker/SEC filings](https://kingscrowd.com/miso-robotics-on-dealmaker-securities-2025-2/);
[White Castle 100-location expansion announcement, 2022](https://info.misorobotics.com/newsroom/white-castle-expands-partnership-with-miso-robotics-to-install-flippy-2-in-100-new-locations)).

The gap between "100 new locations" announced in 2022 and 10 systems deployed in 2026 is the single
most instructive data point in restaurant robotics. It is not that Flippy does not work — by all
accounts the fry station works. It is that **the deployment rate of a working kitchen robot into a
willing, publicly committed, highly standardised QSR chain is on the order of a few units per year.**
Any timeline claim that outruns that number is not credible.

The systems that *are* scaling in kitchens all share one property: they are not robots operating in a
kitchen, they are **redesigned stations that happen to contain actuators**.

| System | What it actually is | Status |
|---|---|---|
| Sweetgreen Infinite Kitchen | Automated makeline — dispensing, not manipulation. ~700 bps labour savings, ~100 bps COGS improvement vs. traditional stores (company-reported) | Scaling; technology [sold to Wonder for $186M](https://www.restaurantdive.com/news/wonder-deploys-infinite-makeline-manhattan/830315/), redeployed as Infinite Makeline |
| Hyphen Makeline | Under-counter automated assembly, ~350 bowls/hour early version | Tested at Chipotle's Cultivate Center and in stores; [not system-deployed](https://www.restaurantdive.com/news/cava-chipotle-invest-hyphen-automated-makeline/757450/) after several years and $10M+ from Chipotle and Cava |
| Chef Robotics | Fixed-station ingredient dispensing into trays in **food manufacturing**, not restaurants | >100 million servings cumulative; [$43.1M Series A](https://www.therobotreport.com/chef-robotics-brings-in-43m-to-deploy-more-food-assembly-robots/) ($20.6M equity, $22.5M equipment debt) |

Chef Robotics deserves specific note because it is the strongest company in the category and its
positioning proves the thesis. It succeeded by going **upstream into food manufacturing** —
high-volume, fixed-layout, repetitive, single-product-run — and states that restaurants are the
*eventual* goal, reached by working through "stadiums to cruises to prisons and ghost kitchens"
first. The most capable food-manipulation company in the world has ordered its market by descending
structure, and restaurants are last.

### 2.5 Front of house: deployed at scale, ROI contested

Bear Robotics reports [>16,000 robots deployed
globally](https://embodyvc.com/companies/bear-robotics/); Pudu reports
[>56,000](https://www.roboticscenter.ai/blog/restaurant-robot-guide). LG [acquired a controlling 51%
of Bear](https://www.lg.com/global/newsroom/news/corporate/lg-acquires-majority-stake-in-bear-robotics-to-bolster-robotics-capabilities/)
in January 2025. These are real numbers and a real business.

They are also a robot that does not manipulate anything. A Servi or BellaBot is a wheeled tray with
obstacle avoidance. Humans load it and humans unload it. That is precisely why it scaled: it removed
the two hardest problems (grasping and food contact) from the requirements.

Even so, the ROI is contested. [Chili's paused its 61-store server-robot
pilot](https://www.restaurantbusinessonline.com/technology/chilis-pausing-its-test-server-robots) —
the units moved too slowly and congested aisles, and 58% of surveyed guests said the robot did not
improve their experience. Managers at Haidilao outlets have reported reliability and cost-
effectiveness falling short of human servers.

**Read that carefully.** The easiest possible embodied task in a restaurant — wheeled transport, no
manipulation, no food contact, flat floor, fixed route, in a chain willing to run a 61-store pilot —
failed its ROI test on *congestion and speed*. Restaurant floors are the constraint, not the
autonomy stack.

### 2.6 The failure record

| Company | What it tried | Outcome |
|---|---|---|
| Zume Pizza | Robot-assembled pizza cooked in ovens inside moving delivery vans | Burned [~$445M](https://www.fastcompany.com/90979001/zume-pizza-silicon-valley-445-million-robot-revolution-that-wasnt); could not stop cheese sliding during transit cooking; pivoted to packaging 2020; folded 2023 |
| Karakuri | Robotic kiosk assembling hot and cold meal components | [Shut down](https://thespoon.tech/karakuri-joins-the-growing-list-of-food-robot-startups-that-have-shut-down/); cited long development cycles and capital intensity |
| Creator | Robotic burger restaurant | Ceased operations |
| Dishcraft Robotics | Automated commercial dishwashing | Ceased operations |

Four failure modes recur and all four apply to any kitchen manipulation proposal:

1. **Development cycles outrun funding cycles.** Food robotics takes 5–8 years to a shippable unit;
   venture funds are structured for shorter.
2. **Physics of food is harder than assumed.** Zume's failure was literally a materials problem —
   molten cheese under vehicle acceleration. Deformable, thermally active, variable-geometry
   material is the adversary.
3. **Capital intensity per revenue dollar is brutal.** Miso: $29M raised against $515k of revenue.
   Chef Robotics had to raise $22.5M of *equipment* debt separately from equity, because the robots
   are inventory.
4. **The customer has a cheaper substitute that already works.** Restaurant labour is the lowest-cost
   flexible manipulator available, and it reconfigures for free.

---

## 3. Mapping the chain: where robots genuinely pay

### 3.1 A five-factor screen

Embodied automation pays where five conditions coincide. Scoring each stage 1–5 on each factor makes
the pattern legible. **These scores are the author's judgement, not measurements** — they are an
argument structure, not evidence, and a reviewer should feel free to move any individual cell.

| Factor | Why it governs |
|---|---|
| **Structure** | How predictable the geometry, lighting, and object set are. Determines whether perception is solvable. |
| **Repetition density** | Task instances per square metre per day. Determines whether a fixed installation amortises. |
| **Utilisation hours** | Hours/day the machine can be productive. Capex is fixed; hours are the denominator. |
| **Labour displaced** | Fully loaded hourly cost of the human doing the job today. Sets the ceiling on robot cost. |
| **Failure tolerance** | Cost of a failed task. A dropped case in a DC is waste; a dropped pan during service is a ruined ticket and a safety incident. |

| Stage | Struct. | Repet. | Hours | Labour $ | Fail. tol. | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Distributor DC (case handling, AS/RS, AMR) | 5 | 5 | 5 | 4 | 4 | **23** | Deployed at scale now |
| Primary processing / food manufacturing | 5 | 5 | 5 | 3 | 4 | **22** | Mature (fixed industrial robots) |
| Middle-mile highway transport | 4 | 4 | 5 | 5 | 1 | **19** | Early commercial; safety case is the gate |
| Last-mile sidewalk delivery | 2 | 3 | 4 | 3 | 3 | **15** | Deployed in narrow geographies |
| Front-of-house running | 2 | 4 | 3 | 2 | 4 | **15** | Deployed; ROI contested |
| Prep — **fixed station** (fryer, makeline) | 4 | 4 | 2 | 2 | 2 | **14** | Works only where the station is redesigned |
| Farm harvest | 1 | 4 | 1 | 4 | 3 | **13** | Narrow crops only; seasonality kills amortisation |
| Restaurant receiving / BOH storage | 1 | 2 | 1 | 2 | 3 | **9** | Nothing deployed. Decade+ |
| Prep — **general** (mise en place, plating) | 1 | 2 | 2 | 2 | 1 | **8** | Not on any credible roadmap |

### 3.2 What the screen shows

The stages where robots work are the stages where somebody spent capital making the world legible to
a machine — pallets, totes, barcodes, flat floors, fixed racking, known SKU dimensions. **A pallet is
not a shipping convenience; it is a machine-readable abstraction over goods, and it took the
twentieth century to standardise.** The restaurant back of house has no equivalent. Every walk-in is
laid out differently, stock is in whatever container it arrived in, floors are wet, aisles are
600 mm wide, and four humans are moving through the same volume at speed during service.

Two rows deserve emphasis:

**"Prep — fixed station" scores 14, not 8, because the station was redesigned.** Sweetgreen's Infinite
Kitchen does not solve kitchen manipulation; it *deletes* it by replacing an assembly task with a
dispensing task in purpose-built hardware. That is the only kitchen automation pattern with evidence
behind it, and it is a capital-equipment business, not a robotics business.

**"Restaurant receiving / BOH storage" — the stage Mise touches — scores lowest but one.** It has the
worst structure, the lowest repetition density (a branch receives goods a handful of times per day),
the worst utilisation (the machine idles 20 hours), and it displaces the cheapest labour in the
chain. Every one of the five factors points the same way.

### 3.3 The honest version of "economics are better upstream"

The commonly stated version — upstream environments are more structured — is true but incomplete. The
quantitative version is sharper and is developed in §6: **the same machine costs roughly $9/hour in a
DC and roughly $30/hour in a restaurant, purely because of utilisation hours, while the labour it
displaces is worth roughly $30/hour in the DC and roughly $22/hour in the restaurant.** The ratio
flips from about 3× favourable to about 1.4× unfavourable before any capability difference is
considered. Structure determines whether the robot *can* do the job; utilisation and wage determine
whether anyone should buy it. Restaurants lose on both.

---

## 4. The specific Mise question: is a transfer a robotics problem?

### 4.1 Decompose the actual task

Take Project-SCIM's own scenario, which uses real Mise numbers: Downtown holds 4.0 kg against a par of
40 (36 short); Marina holds 34.0 against a par of 24 (10 kg surplus, 2 days to expiry); transfer 10
kg, buy the net 26 at $2.05/kg. Here is what physically happens.

| Sub-task | Duration | Who does it today | Is it a robotics problem? |
|---|---|---|---|
| Decide the transfer should happen | — | **Mise** | No — this is the product, and it is software |
| Locate the specific crate in Marina's walk-in | 30–90 s | Whoever is on shift | Perception problem; unsolved in clutter; low value |
| Pick and carry crate to the vehicle | 60 s | Same person | Trivially easy for a human; hard and expensive for a robot |
| Drive across the city | 20–45 min each way | Manager, shared driver, or courier | **This is the entire cost.** Autonomy-relevant, but it is the autonomous-vehicle problem, not a Mise problem |
| Carry crate into Downtown, put on shelf | 60 s | Receiving staff | As above |
| Reconcile the received quantity against the ticket | 30 s | Staff, in the app | **Software. And currently the weakest link.** |

Roughly 95% of the elapsed time and essentially all of the marginal cost is the drive. The
manipulation portion — two picks and two places of a rigid, handled, standardised crate — is about
three minutes of human effort spread across an hour.

### 4.2 The uncomfortable arithmetic

The physical leg costs, today:

| Execution mode | Cost per transfer | Basis |
|---|---|---|
| Third-party white-label courier (Uber Direct) | $5–9 | [Published merchant pricing](https://www.wpslash.com/how-to-integrate-doordash-drive-and-uber-direct-with-your-woocommerce-restaurant-for-local-delivery/) |
| DoorDash Drive | $6–10 | Same |
| Roadie, local ≤20 miles | $15–35 | [Published ranges](https://new.risingsunartscentre.org/news/roadie-cost-typical-price-ranges-for-us-deliveries-2026.html) |
| Own staff, 60–90 min round trip | $22–35 labour + $6–12 vehicle | BLS median cook $17.62/hr (May 2025) × ~1.3 burden, plus IRS-rate mileage |
| **Marginal cost if it rides an existing trip** (manager already driving between branches; commissary run) | **~$0** | — |

Now the value side. Ten kilos of tomatoes at $2.05/kg is **$20.50 of purchase avoided**, plus up to
another $20.50 of spoilage avoided at Marina. Call the economic value $20–41.

**A single-item transfer executed by a paid courier is marginal, and executed by staff in a company
vehicle is often negative.** This is not a criticism of Mise; it is the reason real multi-site
operators batch transfers onto one van run, and it is the most important operational fact in this
document.

### 4.3 What that implies

Three consequences follow, and they all point away from robotics.

1. **The automation lever that matters is batching and routing, not picking.** If the marginal
   courier leg is $5–9 and the per-line value is $20, then the variable that determines whether Mise's
   recommendations clear in practice is *how many lines share a van*. That is a vehicle-routing and
   scheduling problem — software Mise can build, running on data Mise already has. A manipulator
   improves none of it.

2. **The cheapest execution is the trip that already exists.** The highest-leverage physical-AI-
   adjacent feature Mise could ship is not a robot; it is knowing the existing movement pattern
   between branches — who drives where, when, in what vehicle, with what spare capacity — and
   scheduling transfers onto it. This is a logging and constraint-solving feature.

3. **Where automation genuinely changes these unit economics, it does so from outside Mise.** If
   autonomous urban freight makes an intra-city 10 kg drop cost $2 instead of $7, every marginal
   transfer becomes clearly positive and Mise's recommendation volume goes up materially. **Mise is a
   beneficiary of transport autonomy, not a producer of it** — and that is a genuinely good position:
   all of the upside, none of the capex. This is the strongest honest physical-AI statement available
   and it is worth more than any manipulation claim.

### 4.4 A note on what the sensible robot would actually be

If one insisted on automating the crate handling, the correct design is *not* a humanoid and *not* a
food robot. It is a materials-handling robot that touches **only the sealed crate, never the food** —
which sidesteps the entire food-contact regulatory regime (§6.3). The task is closer to a small AMR
with a lift than to anything in the VLA literature. That makes it an easier engineering problem and
an even worse business problem, because it saves three minutes of a $22/hour worker's day.

---

## 5. The data argument, examined

This is the section most likely to be probed by an engineering-literate reviewer, and the one where
the loose version of the claim does not survive contact.

### 5.1 Four distinct kinds of data get conflated

| Tier | Content | Sample rate | Who needs it |
|---|---|---|---|
| **(a) Decision-level** | *That* a task was chosen: item, quantity, origin, destination, deadline, outcome | ~1 row per task | Planners, schedulers, forecasters, benchmark authors |
| **(b) Task-level demonstration** | *How* a task decomposed: subgoals, ordering, durations, who did what, where handoffs occurred | ~10–50 rows per task | Task-and-motion planning, high-level policy, LLM agents |
| **(c) Trajectory-level** | Synchronised observation–action streams: RGB from 2–3 cameras, proprioception, commanded actions | **30–50 Hz, continuous** | Imitation learning, VLA fine-tuning |
| **(d) Contact-level** | Force/torque, tactile, slip, deformation | 100–1000 Hz | Contact-rich manipulation, grasping of deformables |

**Mise records tier (a). Exclusively.** A transfer record — origin, destination, item, quantity,
deadline, cleared or not — is perhaps 200 bytes, one row per event. There is no observation in it, no
action, no geometry, no force. It is not a low-resolution version of tier (c); it is a different
object.

The magnitude gap is worth making concrete. π₀-class fine-tuning to a new task takes on the order of
[100–1,000 demonstrations, or 1–20 hours of teleoperated
data](https://www.therobotreport.com/physical-intelligence-open-sources-pi0-robotics-foundation-model/),
each demonstration being a multi-camera stream at control frequency. One hour of one robot's data is
tens of gigabytes. A thousand Mise locations doing one transfer per location per day for a year
produce roughly **73 MB** of tier-(a) records — and **zero** state–action pairs.

### 5.2 What the imitation-learning literature actually says you need

The relevant result is [*Data Scaling Laws in Imitation Learning for Robotic
Manipulation*](https://arxiv.org/abs/2410.18647), which finds that generalisation follows an
approximate power law in the number of **environments and objects**, and that **diversity of
environments and objects dominates the raw number of demonstrations** — beyond a threshold of roughly
50 demonstrations per environment–object pair, additional demonstrations in the same setting add
little. Policies trained on ~32 distinct environment–object pairs generalised to unseen environments
and objects at roughly 90% success.

Two implications for Mise:

- The binding constraint on a restaurant-logistics policy is **how many distinct kitchens and how
  many distinct crates and objects it has seen**, not how many transfer events are in a ledger. Mise
  does accumulate environment diversity in principle — many branches — but it records nothing about
  those environments.
- "We have more transfer records than anyone" is a claim about volume in a tier where volume is the
  least valuable axis, in a modality that is not the one policies train on.

### 5.3 Where the Mise record is genuinely, defensibly valuable

Rigour cuts both ways. Tier (a) is not worthless — it is valuable for things that are not policy
learning, and those things are real:

1. **Task distribution.** No robotics company knows the true empirical frequency distribution of
   restaurant-logistics tasks: which items move, in what quantities, between what site types, under
   what deadlines, how often, with what failure rate. That distribution is exactly what you need to
   *specify* a benchmark, *generate* simulation scenarios, and *weight* a curriculum. It is the
   answer to "what should the robot be good at," which is logically prior to "how does the robot do
   it" and is answered by nobody today.
2. **Scheduling and TAMP priors.** Deadlines, durations, and clearance rates are directly usable by a
   high-level planner and by an agentic system deciding sequencing. This is a real use and it is one
   Mise itself should exploit before anyone else does.
3. **Outcome labels.** "Did it clear" is a supervised label on a decision. That is the scarce thing
   in operations data and it is the foundation of the forecasting moat — which is a *software* moat
   and the strongest one Mise has.

### 5.4 Two defects in the record as currently kept

Both are cheap to fix and both are the kind of thing a reviewer will spot.

**Selection bias.** Mise logs the transfers Mise *decided to make*. A model trained on that log
inherits Mise's own policy — the classic logged-bandit / off-policy evaluation problem. You cannot
learn "which transfers would have cleared" from a dataset containing only transfers you chose to
attempt. **Fix: log rejected candidates too**, with the reason for rejection (distance, deadline,
quantity below threshold, no vehicle). That converts a biased log into a counterfactual dataset and
costs a database column. It is the single highest-value schema change available.

**No execution metadata.** The record captures the decision and the outcome, but not the execution:
dispatch time, arrival time, vehicle, carrier, whether the quantity that arrived matched the quantity
sent, condition on arrival, whether it rode an existing trip. This is the *only* part of the record
with any bearing on physical execution, it is the input to the routing work in §4.3, and it is
currently missing. **Fix: capture it.** It costs a form field and it is the concrete, unglamorous
version of the "embodied data" claim.

### 5.5 Project-SCIM: right modality, and the README explains why the content is limited

Project-SCIM generates tier (b) and nominally tier (c) — paths, pick/place events, handoff timing,
congestion. That is the correct modality. Its own [README](https://github.com/abhijitbetigeri/Project-SCIM)
states the limits, verbatim, and they should be read as technical statements rather than as modesty:

> **Honest limits.** Nothing is learned here: the robot follows a scripted task. What works end to end
> is the pipeline from execution to robot-consumable trajectory data. Avoidance is whisker raycasts,
> not a planner. Geometry is primitives — it reads as a diagram of a restaurant, not a photoreal one.

Each limit has a precise consequence for training value:

| README statement | Consequence for the data |
|---|---|
| "Nothing is learned here: the robot follows a scripted task" | The logged trajectories are the **script's** trajectories. Behaviour-cloning a scripted controller recovers the script, which you already possess in closed form. Information gain over the source code is zero. |
| "Avoidance is whisker raycasts, not a planner" | The avoidance behaviour is a reactive heuristic, not competent navigation. It is not a behaviour worth cloning, and the collision statistics do not describe a real navigation stack's failure distribution. |
| "Geometry is primitives — it reads as a diagram of a restaurant, not a photoreal one" | No usable visual distribution for a perception model. Domain randomisation over primitives does not cover the appearance manifold of a real walk-in. |
| "What works end to end is the pipeline from execution to robot-consumable trajectory data" | **This is the true and defensible claim.** It is a claim about *instrumentation and schema*, not about a dataset or a policy. |

The one channel with independent research interest is the human side: **human–robot handoff timing
and congestion measured rather than assumed**, in an environment where a human player controls one
side. That is a genuine quantity. At primitive-geometry fidelity and ~45-second sessions it is a
demonstration that the measurement exists, not a dataset anyone can train on — but it is the part
worth developing if the artifact is ever extended.

On sim-to-real generally: the reality gap for contact-rich and deformable manipulation remains open
even for purpose-built high-fidelity simulators. Recent work finds that simulated **contact force
magnitudes are unreliable** and that transfer succeeds only through carefully chosen
dynamics-invariant representations such as force *direction*
([arXiv:2602.14174](https://arxiv.org/pdf/2602.14174)); the survey literature
([*The Reality Gap in Robotics*, Annual Reviews](https://www.annualreviews.org/content/journals/10.1146/annurev-control-031924-100130))
treats domain randomisation, real-to-sim reconstruction and sim-real co-training as necessary rather
than sufficient. A Unity scene built from primitives, without a calibrated contact model and without
randomisation, is several categories removed from that frontier. This is the correct reason to never
use the phrase "digital twin" or "sim-to-real" about Project-SCIM — not because it sounds
overreaching, but because it is a specific technical claim that the artifact does not support.

### 5.6 The sharpened version of the moat claim

[`vision.md` §3](vision.md) lists "Embodied demonstration data" as the fourth row of the data moat and
states that *"every rebalance decision Mise records is simultaneously a labelled example of an
embodied logistics task."*

**That sentence is true under one reading and false under another, and the two readings are exactly
what an engineering judge will separate:**

- **True reading:** a labelled example of an embodied logistics *task specification* — the what, not
  the how. Tier (a). Genuinely unheld by anyone else, genuinely useful for benchmark design,
  scenario generation, and planning. This is the claim to make.
- **False reading:** a labelled example of embodied *behaviour*, usable to train a manipulation
  policy. Tier (c). Mise holds none of this, and Project-SCIM holds only scripted simulated versions
  of it.

The pitch line — *"Every transfer Mise decides today is training data for the robot that executes it
tomorrow"* — sits on the boundary. It is defensible, and it is the single claim in the deck most
likely to be probed. The prepared twenty-second answer is:

> "Task-level, not trajectory-level. We hold the decision record — item, origin, destination,
> deadline, outcome — which is what you need to *specify* the task and to generate the scenario
> distribution. The sensorimotor data is a separate problem and we don't claim it. Project-SCIM is a
> scripted simulation; its README says nothing is learned there. What works end to end is the
> pipeline from a decision to a robot-consumable task record."

Volunteering that distinction before being asked converts the weakest claim in the deck into
evidence of judgement. This does not contradict the fifteen-second policy — it is the answer held in
reserve for the question the fifteen seconds invites.

---

## 6. What would have to become true

### 6.1 The cost model

The relevant comparison is cost per productive hour, not sticker price. Assumptions are shown so each
can be argued with independently.

**Machine:** a warehouse-grade mobile manipulator capable of locating, grasping and transporting a
standard crate. Sticker prices for reference: [Unitree G1 at
$13,500](https://theresarobotforthat.com/blog/unitree-g1-price/) (research platform, not a work
machine — no payload, no washdown, no service contract); [Agility Digit at ~$250,000 purchase or
~$30/hour RaaS](https://robotpriceindex.com/guides/how-much-does-a-humanoid-robot-cost); Figure 03
unpublished, third-party estimates ~$250,000. Take $150,000 as an optimistic mid-decade price for a
purpose-built, non-humanoid crate-handling machine.

| Line | Annual | Note |
|---|---|---|
| Capex amortisation | $30,000 | $150,000 over 5 years, zero salvage |
| Maintenance, spares, service contract | $18,000 | 12% of capex — conventional for mobile robotics |
| Remote supervision | $10,000 | 1 teleoperator per 5 robots, $25/hr loaded, 2,000 hr/yr |
| Connectivity, insurance, integration amortisation | $5,000 | |
| **Total cost of ownership** | **$63,000/yr** | |

| Deployment | Productive hours/yr | **Cost/hour** | Loaded labour displaced | Verdict |
|---|---|---|---|---|
| **Distribution centre** — 20 h/day × 350 days | 7,000 | **$9.00** | $28–38/hr (Sysco selector [$20/hr start rising to $27.25/hr](https://careers.sysco.com/en/Sysco-Detroit) × ~1.3 burden, plus night differential) | ~3× favourable. This is why DCs buy |
| **Restaurant back of house** — 6 h/day × 350 days | 2,100 | **$30.00** | $22–23/hr (BLS median cook [$17.62/hr, May 2025](https://www.bls.gov/ooh/food-preparation-and-serving/cooks.htm) × ~1.3 burden) | ~1.4× unfavourable. This is why restaurants don't |

**The same machine, the same capability, the same year — and the answer inverts on utilisation and
wage alone.** Capability is not the binding constraint in this comparison; it is the *second*
constraint, and it also points the same way.

### 6.2 What would have to change

| Variable | Today | Threshold for restaurant BOH to pencil | Realistic? |
|---|---|---|---|
| Machine cost | ~$150k (optimistic) | **≤$35k** at restaurant utilisation, holding opex ratios | Possible late-decade if humanoid supply chains commoditise; no evidence yet at work-machine grade |
| Productive hours/day | ~6 (one delivery window, one prep block) | **≥16** — requires the robot to do several *unrelated* jobs | The real blocker. Single-task machines cannot reach it; multi-task capability is precisely what does not exist |
| Loaded restaurant wage | $22–23/hr | **≥$35/hr** | Would require a large real-wage shock; possible in specific high-minimum jurisdictions, not nationally |
| Remote intervention rate | n/a — no deployed baseline | **<1 per 500 tasks** (see §6.4) | Unknown. No published data for cluttered indoor manipulation |
| Grasp generality on food-adjacent items | ~65% of rigid retail packaging (Amazon Sparrow) | **>99%** on crates; >95% on loose produce | Crates are plausible within 3–5 years. Loose produce is not, on current evidence |

The row that decides it is **productive hours**. A restaurant cannot keep a robot busy. The only
architecture that fixes this is a machine that does several unrelated jobs across the day — which is
the humanoid pitch, and which is exactly the capability that does not exist and is not close.

### 6.3 Regulatory constraints

| Constraint | Effect |
|---|---|
| [FDA Food Code](https://www.fda.gov/food/retail-food-protection/fda-food-code): food-contact surfaces cleaned at least every 4 hours | Any end-effector contacting food or food-contact surfaces enters a sanitation regime requiring washdown-rated hardware |
| Washdown ratings: IP66–IP69K, [DIN 40050-9](https://teyconn.com/engineering/ip69k-food-grade-connector-guide/) (100 bar, 80 °C jet); 316L stainless; NSF H1 lubricants per [21 CFR 178.3570](https://teyconn.com/engineering/ip69k-food-grade-connector-guide/) | **Rules out essentially every general-purpose mobile manipulator and humanoid currently shipping.** Their hands, cable runs, and joint seals are not washdown-rated and cannot be made so without a redesign |
| Temperature control in transit for TCS foods | Tomatoes are not time/temperature-control-for-safety foods, so the canonical Mise example is the easy case. **Anything chilled requires an actively refrigerated, temperature-logged vehicle** — which is a much harder autonomy target than a sidewalk robot |
| State personal-delivery-device statutes | Typically cap weight and speed. A single 10 kg crate is usually within limits; a batched multi-line transfer — which §4.2 shows is the only version with viable economics — generally is not |

The useful conclusion: **the regulatory picture favours the crate-only design.** A robot that touches
only sealed containers avoids the Food Code entirely. That is a design constraint the Mise task
naturally satisfies, and it is worth knowing — even though §4 concludes the machine should not be
built.

### 6.4 The reliability threshold, derived

Suppose a robot performs 40 transfer-related task instances per site per day and each failure requires
5 minutes of a $23/hr worker's attention — roughly $1.92 per intervention, before the cost of a
service disruption. The robot's entire claimed saving is about three minutes of that worker's time per
transfer, or roughly $1.15.

**At a 99% per-task success rate, the robot fails 0.4 times per day and consumes $0.77/day of human
attention against $46/day of claimed saving — fine. At 95%, it fails twice a day and the operator
starts scheduling around it. The real threshold is not the arithmetic; it is the point at which a
manager stops trusting the machine during service, which happens well above the break-even rate.**

The Chili's outcome is the empirical version of this. Its robots did not fail at manipulation — they
did not manipulate. They were abandoned for being slow and congesting aisles. **The operative
reliability constraint in a restaurant is not task success; it is not being in the way**, and no
published metric measures it.

---

## 7. Timeline

Reasoning is given per row because the dates are less useful than the arguments.

| Stage | Meaningful automation | Reasoning |
|---|---|---|
| Food manufacturing / processing | **Now** | Mature. Chef Robotics at 100M+ servings; fixed industrial robots standard. Structure was engineered in decades ago |
| Distributor DC — case handling, AS/RS, AMR | **Now, deepening through 2030** | Symbotic, Locus, Stretch all shipping. Constraint is capital and integration time, not capability |
| Distributor DC — each-pick of loose/irregular food items | **3–6 years** | Amazon's 65% catalogue coverage is the ceiling indicator. Food is the hard tail of that distribution |
| Middle-mile highway freight | **3–7 years to material volume** | Technology works (Aurora 440k driverless miles); volume is ~50 human drivers' worth. Refrigerated multi-stop foodservice routes are a later cohort than dry van |
| Last hundred feet of food delivery — liftgate, back door, check-in | **7–12 years** | Nobody is working on it. It is the actual bottleneck in food freight and it has no programme behind it |
| Urban light freight autonomy (would change §4.3 economics) | **5–10 years** | Depends on regulatory expansion of autonomous commercial vehicles beyond current geofences |
| Restaurant fixed-station automation (fryer, makeline) | **Now, but scaling at single-digit units per chain per year** | Miso: 10 systems deployed in 2026 after a 100-location announcement in 2022. Sweetgreen/Wonder is the pattern that works, and it is capital equipment |
| Front-of-house running | **Deployed; will remain contested** | 16k + 56k units shipped, and Chili's still walked away. The category is real and the ROI is site-specific |
| Restaurant BOH mobile crate handling (the Mise task) | **10+ years, and likely never as a standalone purchase** | Fails all five screen factors. Utilisation is the structural blocker. Only arrives bundled into a general-purpose machine that does many jobs |
| General kitchen manipulation — prep, plating, mise en place | **Not forecastable** | Requires deformable-object manipulation under time pressure in clutter with food-safety hardware. No credible path is visible |

The single most defensible sentence in this table: **the deployment rate of a working, publicly
committed kitchen robot into a willing QSR chain is on the order of a few units per year.** Any
timeline that outruns that is asserting a change in the rate, and needs to say what causes it.

---

## 8. What the founder should do in the next 18 months

**Almost nothing.** That is the correct answer, and it should be stated as a decision rather than an
omission. What follows is the complete list, and it is short by design.

### 8.1 Do

1. **Add the two schema fields from §5.4.** Log *rejected* transfer candidates with rejection reason,
   and log execution metadata (dispatch/arrival time, carrier, vehicle, quantity variance, whether it
   rode an existing trip). Cost: a migration and two form fields. This is the only item on this list
   with compounding value, and its value is primarily to Mise's own routing and forecasting — the
   embodied-data story is a secondary benefit, not the justification.

2. **Build the batching/routing feature, and understand it as the real physical-AI work.** §4.2 shows
   single-line transfers are economically marginal and §4.3 shows batching is the lever. This is the
   feature that makes Mise's recommendations actually clear in the field. It is software, it needs no
   capex, and it is the honest answer to "what are you doing about execution."

3. **Keep Project-SCIM alive as a research artifact and do not extend it.** Its value is that it
   exists, it is public, and its README is more candid than most pitch decks. Extending it costs
   engineering time for no commercial return. If it is ever extended, the one channel worth
   developing is human–robot handoff timing, which is the only measurement in it with independent
   research interest.

4. **Keep the robotics credential visible and separate from the product claim.** See §8.3 — it is a
   credibility asset and it is being under-used.

5. **Track two external variables, quarterly, at fifteen minutes each.** (i) Urban autonomous light
   freight cost per drop — the only exogenous change that materially improves Mise's transfer
   economics; (ii) deployment counts, not announcements, in kitchen automation. Both are cheap to
   watch and neither requires action until they move.

### 8.2 Do not

| Do not | Why |
|---|---|
| Buy, lease, or pilot any robot | There is no task in Mise with positive unit economics for a machine, and the capex would contaminate an 84%-gross-margin model |
| Build a robotics roadmap slide with dates | §7 shows the dates would be wrong, and a wrong date is worse than no date in front of engineering judges |
| Collect sensorimotor data speculatively | Tier-(c) data is only valuable against a specific embodiment and task. Collected without one, it is unusable — and Mise has no embodiment |
| Describe Project-SCIM as a digital twin, sim-to-real, or a trained policy | Contradicted by its own public README, which is linked from the repo and which a judge can read in ninety seconds |
| Position Mise as a robotics company | The screen in §3 says the whole category is a decade out at the stage Mise occupies. The software business is the business |

### 8.3 The most under-used asset

The founder's strongest robotics credential is not Project-SCIM. It is a **verifiable defect found in
upstream Isaac Lab**, which this analysis independently confirmed in current `main`:

`source/isaaclab_tasks/isaaclab_tasks/manager_based/locomotion/velocity/velocity_env_cfg.py`
sets the startup material-randomisation event to

```python
"static_friction_range": (0.8, 0.8),
"dynamic_friction_range": (0.6, 0.6),
```

Both ranges are **degenerate** — minimum equals maximum — so the randomisation term is a no-op and
every environment in the batch trains on one surface. The G1 configurations
(`.../config/g1/rough_env_cfg.py` and its flat variant) inherit this without override. Meanwhile
Spot, in the same tree, overrides it properly in
`.../config/spot/flat_env_cfg.py`:

```python
"static_friction_range": (0.3, 1.0),
"dynamic_friction_range": (0.3, 0.8),
```

The quadruped gets real friction randomisation; the humanoid, in the default pipeline most people
start from, does not. That is a genuine finding about the most widely used humanoid training stack,
it is checkable in thirty seconds by anyone on the panel, and it demonstrates the exact skill this
analysis says is scarce: **reading a simulator sceptically instead of trusting it.**

It is also the tightest possible illustration of §5.5's argument. The reason simulated data must be
distrusted by default is not abstract — it is that a widely used, well-maintained public repository
silently trains humanoid locomotion on a single friction coefficient. Somebody who found that is
qualified to say what simulated demonstration data is and is not worth, and that is the credential
worth carrying into the room.

---

## 9. Conclusions

1. **Embodied automation in food supply chain works upstream and fails downstream, for quantifiable
   reasons.** The same machine costs ~$9/hour in a distribution centre and ~$30/hour in a restaurant
   on utilisation alone, against labour worth ~$30/hour and ~$22/hour respectively. The ratio inverts
   before capability is even considered.

2. **A Mise transfer is not a robotics problem.** 95% of its cost is a van crossing a city. The
   manipulation content is three minutes of a $22/hour worker's day. Automating it would save about
   $1.15 per transfer with a machine costing $63,000 a year.

3. **Single-line transfers are economically marginal at courier prices** — $20–41 of value against
   $5–35 of execution cost. The lever is batching and routing, which is software Mise can build on
   data it already has. This is the most actionable finding in the document and it has nothing to do
   with robots.

4. **Mise is a beneficiary of transport autonomy, not a producer of it.** If urban light freight
   drops the cost of a 10 kg intra-city move, Mise's recommendation volume rises with zero capex
   exposure. This is the strongest honest physical-AI position available and it is better than any
   manipulation claim.

5. **The data argument is weaker than the loose version and stronger than nothing.** Mise holds
   decision-level task specifications — genuinely unheld by anyone, genuinely useful for benchmark
   design, scenario generation and planning. It holds zero sensorimotor data. Project-SCIM produces
   the right modality from a scripted controller over primitive geometry, which its README states
   plainly and which means its information gain for policy learning is approximately zero. The
   working claim — a pipeline from a decision to a robot-consumable task record — is true, is the
   README's own claim, and is the one to make.

6. **The correct 18-month robotics plan is two database fields, a routing feature, and leaving
   Project-SCIM alone.** Writing a longer plan would be writing fiction, and the panel contains people
   who would recognise it.

---

## Sources

**Deployed systems**
- [Symbotic — 2025 milestones, 2 billion cases](https://www.symbotic.com/news/symbotic-announces-2025-milestones-processing-over-2-billion-cases-as-demand-for-physical-ai-accelerates/) (vendor)
- [UNFI launches Symbotic AI tech in distribution centres — Supply Chain Dive](https://www.supplychaindive.com/news/united-natural-foods-launches-symbotics-ai-tech-distribution-centers/632854/)
- [Locus Robotics / HelloFresh cold-chain AMR deployment](https://www.businesswire.com/news/home/20260623042232/en/Locus-Robotics-Helps-HelloFresh-Expand-Temperature-Controlled-SKU-Capacity-5X-Across-Growing-Brand-Portfolio) (vendor/wire)
- [Lidl deploying 22 Boston Dynamics Stretch robots — Modern Materials Handling](https://www.mmh.com/article/after_pilot_program_grocery_company_lidl_rolling_out_fleet_of_22_robots_from_boston_dynamics_to_automate_container_unloading)
- [Boston Dynamics — mobile case handling beyond the container](https://bostondynamics.com/blog/taking-mobile-case-handling-beyond-the-container/) (vendor)
- [Amazon robotics investment and Proteus/Sparrow/Vulcan — FreightWaves](https://www.freightwaves.com/news/robots-drive-10b-amazon-investment-for-european-fulfillment-centers)

**Transport autonomy**
- [Aurora — second-generation driverless trucks](https://ir.aurora.tech/news-events/press-releases/detail/144/aurora-launches-second-generation-driverless-trucks-in-u-s-to-meet-customer-demand)
- [Aurora 2026 outlook — Heavy Duty Trucking](https://www.truckinginfo.com/news/aurora-heads-into-2026-with-big-plans-on-tap)
- [Kodiak driverless long-haul on track for 2026 — Heavy Duty Trucking](https://www.truckinginfo.com/news/kodiak-says-driverless-long-haul-launch-on-track-for-2026)
- [Delivery robot comparison 2026 — Inside Deep Tech](https://www.insidedeeptech.com/the-top-delivery-robot-companies-of-2026-compared/)

**Kitchen and restaurant automation**
- [Miso Robotics financials and deployment count — Kingscrowd analysis of SEC/DealMaker filings](https://kingscrowd.com/miso-robotics-on-dealmaker-securities-2025-2/)
- [White Castle / Miso 100-location expansion announcement (2022)](https://info.misorobotics.com/newsroom/white-castle-expands-partnership-with-miso-robotics-to-install-flippy-2-in-100-new-locations)
- [Miso develops smaller, faster Flippy — Restaurant Dive](https://www.restaurantdive.com/news/miso-robotics-develops-smaller-faster-flippy-white-castle-jack-in-the-box/738567/)
- [Sweetgreen automated kitchen margins and retention — Restaurant Dive](https://www.restaurantdive.com/news/sweetgreen-automated-kitchen-higher-margins-sales-labor-retention/723863/)
- [Wonder deploys Infinite Makeline — Restaurant Dive](https://www.restaurantdive.com/news/wonder-deploys-infinite-makeline-manhattan/830315/)
- [Cava and Chipotle back Hyphen with $10M — Restaurant Dive](https://www.restaurantdive.com/news/cava-chipotle-invest-hyphen-automated-makeline/757450/)
- [Chef Robotics $43M Series A — The Robot Report](https://www.therobotreport.com/chef-robotics-brings-in-43m-to-deploy-more-food-assembly-robots/)
- [Chef Robotics 100M servings — The Robot Report](https://www.therobotreport.com/chef-robotics-completes-100-million-product-servings-milestone/)
- [LG acquires majority stake in Bear Robotics](https://www.lg.com/global/newsroom/news/corporate/lg-acquires-majority-stake-in-bear-robotics-to-bolster-robotics-capabilities/)
- [Chili's pauses server-robot test — Restaurant Business](https://www.restaurantbusinessonline.com/technology/chilis-pausing-its-test-server-robots)
- [What's actually deployed vs hype in restaurant robots — SVRC](https://www.roboticscenter.ai/blog/restaurant-robot-guide)

**Failures**
- [Zume Pizza, $445M — Fast Company](https://www.fastcompany.com/90979001/zume-pizza-silicon-valley-445-million-robot-revolution-that-wasnt)
- [Zume case study, four lessons — The Spoon](https://thespoon.tech/a-food-tech-case-study-four-lessons-from-the-demise-of-zume/)
- [Karakuri joins the list of food robot shutdowns — The Spoon](https://thespoon.tech/karakuri-joins-the-growing-list-of-food-robot-startups-that-have-shut-down/)

**Cost inputs**
- [BLS — Cooks, median $17.62/hr May 2025](https://www.bls.gov/ooh/food-preparation-and-serving/cooks.htm)
- [BLS — Food preparation workers, median $16.98/hr May 2025](https://www.bls.gov/ooh/food-preparation-and-serving/food-preparation-workers.htm)
- [Sysco Detroit warehouse order selector pay](https://careers.sysco.com/en/Sysco-Detroit)
- [US Foods warehouse turnover and automation response — Supply Chain Dive](https://www.supplychaindive.com/news/US-Foods-turns-tech-increase-efficiency/548571/)
- [Humanoid robot pricing 2026 — Robot Price Index](https://robotpriceindex.com/guides/how-much-does-a-humanoid-robot-cost)
- [Unitree G1 pricing 2026](https://theresarobotforthat.com/blog/unitree-g1-price/)
- [DoorDash Drive and Uber Direct merchant pricing](https://www.wpslash.com/how-to-integrate-doordash-drive-and-uber-direct-with-your-woocommerce-restaurant-for-local-delivery/)
- [Roadie local delivery cost ranges 2026](https://new.risingsunartscentre.org/news/roadie-cost-typical-price-ranges-for-us-deliveries-2026.html)

**Robot learning and simulation**
- [*Data Scaling Laws in Imitation Learning for Robotic Manipulation* — arXiv:2410.18647](https://arxiv.org/abs/2410.18647)
- [Physical Intelligence open-sources π₀ — The Robot Report](https://www.therobotreport.com/physical-intelligence-open-sources-pi0-robotics-foundation-model/)
- [*Direction Matters: Learning Force Direction Enables Sim-to-Real Contact-Rich Manipulation* — arXiv:2602.14174](https://arxiv.org/pdf/2602.14174)
- [*The Reality Gap in Robotics: Challenges, Solutions, and Best Practices* — Annual Review of Control, Robotics, and Autonomous Systems](https://www.annualreviews.org/content/journals/10.1146/annurev-control-031924-100130)
- [Isaac Lab — `velocity_env_cfg.py` (degenerate friction ranges inherited by G1)](https://github.com/isaac-sim/IsaacLab/blob/main/source/isaaclab_tasks/isaaclab_tasks/manager_based/locomotion/velocity/velocity_env_cfg.py)
- [Isaac Lab — Spot `flat_env_cfg.py` (real friction randomisation)](https://github.com/isaac-sim/IsaacLab/blob/main/source/isaaclab_tasks/isaaclab_tasks/manager_based/locomotion/velocity/config/spot/flat_env_cfg.py)

**Regulatory**
- [FDA Food Code](https://www.fda.gov/food/retail-food-protection/fda-food-code)
- [IP69K food-grade hardware, DIN 40050-9, NSF H1, 21 CFR 178.3570 — engineering guide](https://teyconn.com/engineering/ip69k-food-grade-connector-guide/)
- [Robotic solutions for the food industry — hygienic design requirements](https://blog.unchainedrobotics.de/en/what-robotic-solutions-are-suitable-for-the-food-industry)

**Internal**
- [Project-SCIM README](https://github.com/abhijitbetigeri/Project-SCIM) — source of the four verbatim limits quoted in §5.5
- [`vision.md`](vision.md) — pitch policy, which this document supports and does not amend
