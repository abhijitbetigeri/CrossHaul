# CrossHaul — Q&A defence sheet

For the founder to hold during questions. Dream AI Hackathon, 17:10.

**Three rules before anything else.**

1. Every number spoken must match [`CLAUDE.md` §2](../CLAUDE.md). Nothing gets rounded up under pressure.
2. Name the gap before the judge does. Every honest concession in section 2 buys credibility for the numbers in section 1.
3. If you do not know, say "I don't know, and here is how I'd find out by day 90." That answer scores.

**Four things never to say** (from `CLAUDE.md` §3):

| Never say | Say instead |
|---|---|
| "MarketMan is $199 plus $500 setup" | "MarketMan Starter is $249, free setup. I'm at parity." |
| "Their data model can't produce a per-SKU forecast" | "They can forecast. They have no confidence band, no network object, no above-store workflow." |
| "Nobody does inter-location transfers" | "Everybody records them. Nobody decides them." |
| "42% of restaurants use pen and paper" | "That one floats around unattributed. Here's what I can source." |

---

## 0. The question asked most often: "Where does the data come from?"

Asked more than any other, by practitioners rather than investors. Answer it **before** it is asked —
it is now on the solution slide. If it still comes:

> Four sources, and all four already exist in the business. Sales come from the POS — Toast, Square,
> Lightspeed — item level, per site, per day. Recipes are the bill-of-materials, entered once, which
> is what turns "we sold two hundred and seventy-three of those" into "we consumed forty-one kilos of
> this." Prices, lead times and receipts come off supplier invoices — distributor EDI where it exists,
> invoice OCR where it doesn't. And on-hand comes from the counts they already do, which I carry with
> a confidence band rather than as a fact.
>
> There is no new hardware and no new process. And the audit that opens the sale needs none of it
> live — it runs on a POS export and ninety days of invoices, read-only. That is deliberate: I am not
> asking a nine-site operator to start an IT project to find out whether I am worth $249.

**If pressed on which is hardest:** on-hand, by a distance. Everything else is a clean read; on-hand
is an estimate that drifts between counts. That is why the decision carries a confidence band and why
a proposal only fires when the surplus clears it by a margin — the failure mode is a missed transfer,
never a wrong one. Then hand off to Q3.

**If pressed on integration effort:** POS APIs are the table-stakes build and they are why "cloud,
API-accessible POS" is a disqualifying filter in the beachhead definition. A legacy on-premise POS
turns onboarding into a services project and destroys the gross margin, so those operators are not
the buyer.

**Do not say** the data is clean, that this is solved, or that we replace their inventory system.
Nobody rips out MarketMan — we write the transfer back as their native record so their COGS stays
correct.

---

## 1. The ten most likely questions

Ranked by likelihood × damage if fumbled.

### Q1. "Don't restaurants already have this software? MarketMan, Restaurant365, Crunchtime — this is a mature category."

> Partly yes, and the true part is the part I'd want you to press on. MarketMan, Restaurant365 and Crunchtime all ship inter-location transfers. But read their own words. MarketMan "records items sent between sites." R365 does "transfer tracking." Crunchtime's training catalogue has five transfer courses, and every one starts with "Create a Transfer." A human notices, a human decides, the software books it. That's accounting. CrossHaul does the noticing. And the buyer matters — Crunchtime runs 150,000 locations across 850 brands. That's 176 locations per brand. My buyer has nine.

**Why it lands:** you quote their vocabulary, not your own adjectives. Backed by `docs/competition.md` §8.1 and §4.1.

---

### Q2. "What stops Restaurant365 from shipping this next quarter? They just launched R365 AI."

> Nothing technical. They shipped R365 AI in May — an AI Advisor and AI Scheduling. No supply-chain agent, no cross-location netting. Three things slow them down. Their transfer object is a per-location ledger entry with no group-level requirement vector to optimise against, so it's a data-model change, not a feature ticket. Their large customers already solve redistribution with a commissary, which they model explicitly. And their floor is around $499 a location, so the segment where peer-to-peer rebalancing matters isn't their segment. That's a timing advantage, not a moat. I'd rather say that than claim an impossibility.

**Why it lands:** refusing the impossibility claim is the single strongest credibility move available with this panel. `docs/competition.md` §6.3.

---

### Q3. "Your whole product depends on knowing real stock levels. Their on-hand number is theoretical and drifts between counts. Why is yours any better?"

> It isn't. We read the same POS depletion and we carry the same variance. The difference is what we do with the uncertainty. They report a point estimate to be trued up at period close. We carry a confidence band, and we only propose a move when the surplus clears that band by a margin that makes the move worth it. So the failure mode is a missed transfer, not a wrong one. And every proposal goes to a human before anything leaves a building. Count discipline is my biggest onboarding risk. I'm not going to claim I've solved it.

**Why it lands:** this is the best question in the category and the answer is "not more accurate, better calibrated." `docs/competition.md` §8.2 Q2, §6.1.

---

### Q4. "How do you get your first ten customers?"

> Afternoon walk-ins at the flagship unit, at about four dollars a meeting in parking and coffee. Then restaurant-specialist bookkeepers and CPAs on a fifteen percent referral — highest trust, no cash up front. I'm not buying ads; competing on CPC with Restaurant365 on a $2,800 monthly budget is arithmetic suicide. But I don't lead with the platform. I lead with a paid audit. Three weeks, read-only, five hundred dollars for the first ten operators, credited in full against implementation.

**Why it lands:** specific, cheap, and it names what you deliberately excluded. `docs/go-to-market.md` §2, §3.2.

---

### Q5. "Walk me through the growth. Sixteen groups, then fifty-eight, then one-sixty-seven. That's aggressive."

> Year one is seventeen signatures, founder-led — about three a quarter after a slow start. That's the year I control. The aggressive-looking year is three, and it rests on two account executives at roughly five groups a month each. That's ordinary mid-market productivity at a nineteen-thousand-dollar ACV. If founder-led selling doesn't close year one's sixteen groups, I don't hire the seller. The problem would be the product or the price, and hiring a rep hides that instead of fixing it.

**Why it lands:** you gate your own hire on your own performance. `docs/financial-model.md`, `docs/team.md` Hire 2.

---

### Q6. "How big is this actually?"

> The category is $4.55 billion today, $9.18 billion by 2030. My US serviceable market is about $672 million a year — 225,000 multi-site locations at my price. I'd rather you weigh the beachhead. About 150 qualifying groups in the Bay Area, roughly $2.7 million of ARR. Year one is seventeen of them, which is eleven percent of one metro, which is too aggressive to plan against. That's exactly why geography widens to Sacramento and LA at month six.

**Why it lands:** you volunteer that your own beachhead is too small before anyone computes it. `docs/market-research.md` §1–2, `docs/go-to-market.md` §1.3.

---

### Q7. "Why $249? How do you defend that price?"

> It's exact parity with MarketMan's Starter tier — $249, free setup, checked on their live page this morning. So there's no premium to defend. At their entry price I deliver the inter-location capability they gate to Enterprise, from $449, about 1.8 times up. Restaurant365 is quoted third-party at $499 to $749, and they don't publish a list price. I sit at half their floor. If operators object at parity, the problem is my value claim, not my price — and the answer isn't a discount, it's a narrower transfers-only SKU at $149.

**Why it lands:** you already know your fallback, and it preserves positioning rather than margin. `docs/go-to-market.md` §8 falsifier 5, `docs/financial-model.md`.

---

### Q8. "What does the operator actually get back?"

> Food waste runs about $72,000 per location per year, four to ten percent of food purchased. I recover fifteen percent of that. Not more — I only see the spoilage-and-stockout component, because that's the only part that shows up in inventory data. I can't see a cook trimming a carrot badly, and about seventy percent of foodservice surplus is plate waste I'll never touch. Fifteen percent is $10,800 a location against $2,988 of subscription. That's 3.6 times, and the smallness of the fifteen is the credibility.

**Why it lands:** you cap your own claim out loud. Do not raise 15% under pressure. `docs/vision.md` §2.1.

---

### Q9. "There's physical AI in your title. Are you building robots?"

> No, and I want to be precise about that. Decisions here are execution-aware — vans, distance, spare capacity — because a transfer only beats a purchase if the physical leg is cheap enough. That's a routing and scheduling problem on data I already hold. On robots, I'm a beneficiary of transport and warehouse autonomy, not a producer of it. When an intra-city ten-kilo drop costs two dollars instead of seven, every marginal transfer turns positive and my recommendation volume goes up. All of the upside, none of the capex.

**Why it lands:** fifteen seconds, then stop. This is the Vision beat, not a second act. `docs/platform.md`, `docs/physical-ai.md` §4.3.

---

### Q10. "What's the $1.5 million for?"

> Thirty-four months of runway and a Series Seed milestone. Burn through month twenty-four is $772,000 and ARR at month twenty-four is $1.08 million, which is the number that raises the next round. So the raise is a comfortable buffer, not a knife's edge. The money is two things: a founding engineer on data and forecasting at month three, and the year-one selling I do myself at a $2,000 CAC. Two people in year one at $210,000 of opex. Both salaries are below San Francisco market, visibly and deliberately.

**Why it lands:** you know your own burn to the dollar and you don't pad the ask. `docs/financial-model.md`, `docs/team.md`.

---

## 2. The five hardest questions

These are the ones where the honest answer is a weakness. Concede cleanly in the first sentence, then spend the rest on the plan. A judge who watches you name your own gap stops hunting for it.

### H1. "Has anyone actually agreed to pay you $249?"

> No. Zero customer discovery. Nobody has said yes to that number. The price comes from competitor comparables and the pain comes from industry data — both defensible, neither validated, and I'm not going to dress that up. Here's what closes it. The audit is the discovery, and it's paid rather than a favour. Fifty audits is fifty operators' real data and fifty conversations about price. The immediate step is three Bay Area multi-unit groups, letters of intent, and the price tested against real procurement managers before I treat any of this as fact.

**Backed by:** `docs/financial-model.md` "The honest weakness", `docs/go-to-market.md` §3.3.

---

### H2. "Moving one case of tomatoes across a city — does that actually pay for itself?"

> On its own, no. Ten kilos of tomatoes is twenty to forty-one dollars of value. A courier leg is five to nine. Own staff on a sixty-to-ninety-minute round trip is twenty-two to thirty-five in labour plus vehicle. So a single-item transfer by paid courier is marginal, and by staff in a company vehicle it's often negative. That's the most important operational fact I've found. Which is why the lever isn't the transfer — it's batching, and riding trips that already exist. A manager already driving between branches makes the marginal cost roughly zero. Routing is the product, not picking.

**Backed by:** `docs/physical-ai.md` §4.2, §4.3.

---

### H3. "You say every transfer is training data for a robot. Is it?"

> Half true, and let me split it, because the two readings are different claims. What I hold is task-level: item, origin, destination, deadline, outcome. That's what you need to specify the task and generate the scenario distribution, and nobody holds it today. What I do not hold is trajectory-level — observation-action streams at control frequency. That's what a manipulation policy trains on and I don't claim it. A thousand locations for a year is about 73 megabytes and zero state-action pairs. Project-SCIM is a scripted simulation; its own README says nothing is learned there. What works end to end is the pipeline from a decision to a robot-consumable task record.

**Backed by:** `docs/physical-ai.md` §5.6, §5.1, §5.5. Volunteering this distinction converts the weakest claim in the deck into evidence of judgement.

---

### H4. "You've never hired anyone. Year two goes from two people to six."

> Correct, and nothing offsets it yet. I've never hired and I've never managed. The first hire is the test and I'd rather be judged on it than on a claim. It's a founding engineer on data and forecasting, month three, signed at close of the pre-seed — the thing I'm slowest at alone and to a standard. The other two gaps are the same shape. No restaurant operating experience, so I'm recruiting an operator advisor. No sales experience, so there's an AE at month thirteen. Both are dated, both are in the model, and neither is done.

**Backed by:** `docs/team.md` "The honest gaps", Hire 1.

---

### H5. "Where does churn really land?"

> Honestly, unknown, because there are no customers. One to one-and-a-half percent monthly is an industry-shaped estimate with no evidence behind it, and it's the one assumption I can't test inside ninety days — which is why I named it rather than buried it. The sensitivity is in the model. At two and a half percent monthly, LTV to CAC falls to about four times, and that's still viable. And my beachhead is a metro where restaurant counts are falling, which imports churn. The mitigation is targeting groups that are opening units, not holding steady.

**Backed by:** `docs/go-to-market.md` §8 falsifier 7, `docs/financial-model.md`.

---

## 3. Per-judge anticipation

### Chenxi Wang — Managing General Partner, Rain Capital. CS PhD, ex-CMU faculty, ex-VP Research, Forrester.

The one judge who can read the engineering. She will go at one of the two claims the docs have already had to correct. Have both loaded.

**1A. "You're claiming incumbents architecturally can't do this. They deplete theoretical on-hand from POS sales through recipe cards — that's standard actual-versus-theoretical reporting. So why can't they?"**

> You're right, and the naive version of my argument is false. They can and do produce a per-SKU theoretical on-hand. I'd be wrong to say otherwise. The defensible version has three parts. One, confidence, not capability — theoretical on-hand is trued up against a physical count that's weekly for most items and monthly for slow movers, and between counts it drifts by exactly the unmeasured variance. That's accurate enough to cost a P&L and too uncertain, unqualified, to dispatch a van. A transfer decision needs a confidence interval, and actual-versus-theoretical doesn't produce one. Two, the optimisation object doesn't exist — these are per-location ledgers rolled up for reporting, read-side aggregation. There's no group-level requirement vector to solve a min-cost-flow against, and adding one is a second data model, not a feature. Three, the workflow surface is wrong — a rebalance proposal is above-store and has no owner in a UI built for a store manager doing a count. So: they could build it. My advantage is focus and timing, not physics.

**1B. "Every rebalance decision is a labelled embodied-logistics example. Unpack that for me."**

> Task-level, not trajectory-level. Use the H3 answer verbatim.

**Why these land:** conceding the false half in your first sentence, unprompted, is what separates you from every other pitch she hears today. `docs/competition.md` §6.1 and `docs/physical-ai.md` §5.6.

---

### Kaushal Patel — Member of Technical Staff, OpenAI

**"Where does the model actually do work, and what does inference cost you at scale?"**

> The multi-constraint rebalance decision stays on a frontier model. High-volume, low-reasoning calls — forecasting, bulk extraction off invoices — go to open-weights models on Nebius Token Factory. That's $5.16 down to $0.88 per location per month, eighty-three percent removed, verified live today. But I'll state the limit: inference is not my dominant cost-of-revenue line. Customer success is. Routing contributes about twenty-one percent of the modelled sixty-to-forty-dollar reduction. Claiming it carries the margin story wouldn't survive your next question.

`CLAUDE.md` §9.

---

### Amit Panda — Staff Software Engineer, LinkedIn

**"What breaks first when you go from ten locations to a thousand?"**

> Ingestion. Not the solver — dirty POS exports, invoice OCR, and recipe bills-of-materials that exist as a photo of a laminated card. That's why the first hire owns the forecast and the ingestion layer beneath it, at month three. The second thing that breaks is support: at 1,083 locations, customer success is a staffing line, not a footnote, which is why year three weights toward two CS hires and why gross margin is modelled at eighty-four percent rather than a pure-API number.

`docs/team.md`, `docs/financial-model.md`.

---

### Jessica Li — MTS, micro1 (post-training data); former YC founder

**"What's the data asset here, and is it actually defensible?"**

> The defensible asset is outcome labels — did this proposed transfer clear, did it spoil, did the GM override it. That's a supervised label on a decision, and it's the scarce thing in operations data. Two honest defects. It's a logged-bandit problem: I only record transfers I chose to propose, so a model trained on it inherits my own policy. The fix is logging rejected candidates with the reason, which costs a database column and is the highest-value schema change available. And I currently capture the decision and the outcome but not the execution — dispatch time, carrier, quantity variance, whether it rode an existing trip. That's a form field, and it's the unglamorous version of the embodied-data claim.

`docs/physical-ai.md` §5.3, §5.4.

---

### Pranjal Saxena — Strategy & Operations, Google (AI GTM)

**"Walk-ins are a founder motion. How does this become repeatable?"**

> It doesn't stay walk-ins. The leverage is the accountant layer — restaurant-specialist bookkeepers and fractional CFOs on fifteen percent of first-year ACV. They already have the trust and they see the food-cost line. Toast integration gets built now, but I don't count Toast as a channel before month nine because marketplace leads take nine to twelve months. Distributors are a year-three conversation and through data, not through their sales force. And there's a structural constraint that shapes all of it: I cannot run a single-location pilot, because one site has no counterparty. Minimum deployment is a two-to-three site cluster, so the land is $8,964, never one seat.

`docs/go-to-market.md` §2, §6, `CLAUDE.md` §5.

---

### Arjun Rai — EIR, Open Tech Ventures; founded HelloWoofy

**"SMBs don't change behaviour. Does the GM actually load the van?"**

> That's the risk that would kill it quietly, and it's falsifier three in my plan. The donor branch loses stock and, if it's accounted for wrong, eats the food-cost hit for a decision it didn't make. So two things. Cost every transfer at the donor's book value, credit the donor's P&L, debit the receiver's. And reduce the GM's interaction to one accept-or-decline tap. I measure transfer execution rate in the first cluster pilot and I know by day sixty. If it's low, the product changes in month three rather than waiting to be taught it. And no — nobody rips out MarketMan. I write the transfer back as their native record so their COGS stays correct.

`docs/go-to-market.md` §8 falsifier 3, `docs/competition.md` §7.

---

### Serephina Ha — Managing Director, Founder Institute LA & Boston; GP, Axci Capital

**"You're solo. Why you, and what do you do about the bus factor?"**

> I've shipped sixteen products in four months, and I won a hackathon in July with this one. I'm not a restaurant person. I'm a distributed systems person, and a group whose twelve branches can't see each other's inventory has a coordination problem, not a cooking problem. I know what I'm missing — an operator and a seller. Both are hires, both are dated, both are in the model. The bus factor is real and it's partly why the founding engineer is hire one and starts at month three. And I'm recruiting two advisors with actual terms — a five-to-twenty-unit operator and a food distribution executive, quarter to half a point each, monthly call and one intro a quarter. A logo on an advisor slide is worth nothing.

`docs/team.md` "Why me", Advisors.

---

### Kwangrog Kim — Co-founder & Partner, Sazze Partners

**"What's defensible in three years, and what's the path to the next round?"**

> The next round is arithmetic: $1.08 million ARR at month twenty-four on a $1.5 million pre-seed with thirty-four months of runway. On defensibility, I won't claim a technology moat — R365 or Crunchtime could build this. What compounds is transfer-outcome data: which moves worked, which spoiled, which the GM overrode. That only accrues by shipping first, into a segment the enterprise vendors price past and the entry vendors feature-gate below. And the same primitive is why this isn't a restaurant company forever — the coordination layer exists at enterprise scale and doesn't exist at mid-market price in every sector that holds dated stock. SAP has run inter-plant transfers for decades. A six-plant manufacturer doesn't run SAP.

`docs/financial-model.md`, `docs/platform.md`.

---

## 4. The traps

Things that sound like a question and are actually an invitation to overclaim. The discipline is the same every time: answer the primitive, refuse the capability.

| The trap | What it's fishing for | The disciplined answer |
|---|---|---|
| **"So could this work for pharma?"** | You claiming a vertical you haven't built | "As a primitive, yes — expiry-dated stock, high unit value, chains that already move stock between branches. As a capability, no. Nothing is built for it, and regulated chain of custody is a hard compliance surface. Food service is the beachhead. Pharma is the highest-value row of a table I'd be lying to say I serve." |
| **"Could robots do the transfers?"** | A robotics claim your own public README contradicts | "Not soon, and not mine to build. Ninety-five percent of the cost is the drive, not the picking — two picks and two places of a handled crate is about three minutes of human effort. If you automated it, the right machine is a materials-handling robot that touches only the sealed crate, and it would save three minutes of a $22-an-hour worker's day. I'm a beneficiary of transport autonomy, not a producer of it." |
| **"How much could you save a big chain? Chipotle has 3,500 stores."** | Extrapolation past your own bound | "I won't run that number, because my fifteen percent bound was derived for clustered groups where a sister branch is a forty-five-minute drive. A 3,500-unit chain solves redistribution with a commissary — that's a different problem and the enterprise vendors already own it. My arithmetic is $10,800 per location, and it only holds inside my filter." |
| **"So nobody else is doing this at all?"** | The one sentence that can be refuted from a phone | "No — everybody ships transfers. MarketMan, R365, Crunchtime all have them. They record. Nobody decides. And on the near-expiry auto-promotion piece, the honest phrasing is that I haven't found anyone shipping it, not that nobody does." |
| **"Isn't it something like 42% of restaurants still on pen and paper?"** | You repeating an unsourced number back | "That one floats around unattributed — I traced it and there's no study behind it. What I can source is Toast's 2019 figure, forty-five percent using inventory software, which is dated, and Crunchtime's own numbers: 176 locations per brand. The structural argument is stronger than any survey." |
| **"You're leaving money on the table at $249 — you could charge triple."** | Abandoning the pricing logic mid-pitch | "Maybe, and I'd rather find that out from operators than assert it here. $249 is parity with MarketMan Starter, which is a position I can defend in a room. Zero people have agreed to pay it yet. Until they have, raising it is a guess dressed as confidence." |
| **"Would Toast or Restaurant365 just acquire you?"** | An exit story instead of a company | "It's the realistic outcome in this layer — Toast ceded invoice OCR to xtraCHEF and then bought it. But that's their decision, not my plan. My plan is $1.08 million ARR at month twenty-four." |
| **"Is this an autonomous agent making the calls?"** | An autonomy claim the product doesn't make | "The system notices and proposes. A human approves before anything leaves a building. That's deliberate — the failure mode I want is a missed transfer, not a wrong one." |

---

## 5. The cheat card

Glance at this ten seconds before walking on.

### Six numbers, cold

| | |
|---|---|
| **1** | **$249 / location / month.** Exact parity with MarketMan Starter. They gate transfers to Enterprise, from $449. |
| **2** | **$72,000** waste per location per year. I recover **15%** = **$10,800** against $2,988. **3.6×.** Never raise the 15%. |
| **3** | **CAC payback 4.0 months. LTV/CAC 7.5×**, capped at 36 months on purpose. |
| **4** | **Year 3: 167 groups, 1,083 locations, $3.24M ARR, 84% gross margin.** |
| **5** | **$1.5M pre-seed. ~34 months runway. $1.08M ARR at month 24.** |
| **6** | **176 locations per Crunchtime brand. My buyer has nine.** |

Backups if pressed: TAM $4.55B → $9.18B by 2030. US SAM ~$672M across 225,000 locations. Impact year 3: 931 tons of food, ~4,740 t CO2e.

### The three sentences that are the spine

> **1.** A group with nine branches runs nine separate inventory ledgers — so branch four buys what branch seven is three days from throwing away.

> **2.** Everyone in this category records transfers. Nobody decides them. We forecast per menu item per branch, check branches one through seven before we check a supplier, and only what the group genuinely doesn't have becomes a purchase order.

> **3.** I sell a paid audit of their own invoices before I sell the platform — so the buyer reads dated, priced events from their own data instead of believing my forecast. And if that ledger comes back under $8,000 a location, my thesis is wrong and ten audits tell me by day 90 for $1,750.

### If you blank

Go to the primitive: *forecast demand per site, net it against what sister sites already hold, buy only the remainder.* Then name the buyer. Then name the gap. That sequence works on any question in the room.
