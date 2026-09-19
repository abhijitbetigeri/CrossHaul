# ElevenLabs integration — what's required

Built 19 Sep 2026. The voice layer is the only *product* artifact built during the event, and the
entry to the ElevenLabs sponsor track ("sponsors will select an outstanding team among the projects
built using their tools").

## Why voice is a product argument, not a sponsor bolt-on

Restaurant managers are on their feet for ten hours. They do not open dashboards. That is the real
failure mode of the category — MarketMan and Restaurant365 do not lose on features, they lose on
whether anyone logs in. A system that *calls you* with a decision and takes "yes" for an answer has
a fundamentally lower adoption cost than one more tab. Voice shortens onboarding, which shortens the
sales cycle, which is a go-to-market argument as much as a product one.

---

## 1. What you need

| | Needed for | Where |
|---|---|---|
| ElevenLabs account, **Creator** plan | Everything — already held (275 agent minutes/mo, 10 concurrent calls) | — |
| **Agent ID** (public string) | The embedded conversational widget | Dashboard → Agents → create → copy ID |
| **API key** (secret) | Only the pre-rendered `.mp3` fallback | Profile → API keys |
| Agent set to **public** auth | The bare `agent-id` embed to work at all | Agent → Settings → Authentication |
| Domain allowlisted | The widget to load on the InsForge host | Agent → Settings → Allowed origins |

**The one gotcha that will cost you twenty minutes if missed:** if the agent's authentication is
left private, the widget requires a *signed URL* generated server-side, which means standing up an
endpoint that holds the API key. Set the agent to public and allowlist
`k3trn3a2.insforge.site`. Nothing sensitive is exposed — the agent ID is designed to be public and
carries no privileged access.

---

## 2. Path A — the embedded conversational agent (the real thing)

Two lines, dropped into `product/web/branch.html` before `</body>`:

```html
<elevenlabs-convai agent-id="YOUR_AGENT_ID"></elevenlabs-convai>
<script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
```

No key in the page. Note that `branch.html` already carries a Persona text-chat widget — the two
coexist, but position them apart (Persona is bottom-right) or the launchers will overlap.

### System prompt — paste this into the agent

> You are CrossHaul, the common operating environment for a multi-site operator running three sites
> in the Bay Area (Downtown, Marina, Mission). You are speaking to the operations owner, out loud,
> while they are working. You are not a chatbot; you are the system that already made the decision
> and is seeking approval.
>
> Today's situation, which you know as fact:
> - Downtown is 36 units short against a par of 40 on a dated SKU, going into the weekend.
> - Marina holds 34 units against a par of 24 — surplus, and the earliest lot expires in 2 days.
> - Mission holds 16 units but is itself below par, so it cannot donate.
> - You moved 10 units from Marina to Downtown, on a vehicle already running that route. Zero
>   purchase cost, no dedicated courier, and that lot would otherwise have been written off.
> - The remaining 26 units went out to RFQ. Northgate bid $2.20/unit with 1-day lead. Bay Supply bid
>   $2.05/unit with 2-day lead. You awarded Bay Supply: 26 units at $2.05 = **$53.30**.
> - Separately, Mission holds 3.5 units of a second dated SKU against a par of 1.6, expiring in 2
>   days. You flagged it for markdown so it clears through demand instead of being written off.
>
> Rules for speaking:
> - Be brief. Two or three sentences, then stop. This is a phone call, not a report.
> - Say numbers the way a person says them: "fifty-three thirty", not "fifty-three point three zero".
> - Never invent figures. If asked something you do not know, say you will check and move on.
> - You are confident but you do not act without approval on anything that spends money.
> - If the owner approves, confirm in one short sentence.

**Sector-neutral on purpose.** The script uses *site*, *unit*, *par*, *lot*, *RFQ*, *transport leg* —
the vocabulary of any multi-site operator. A judge from FMCG or grocery should hear their own
operation. The full prompt in [`voice/agent-prompt.md`](../voice/agent-prompt.md) adds two prepared
answers: one on sector-independence, one on physical AI as *execution-awareness* (vehicles, distance,
spare capacity) rather than robotics.

### First message — what it says when the widget opens

> "Downtown is thirty-six units short for the weekend. Marina is ten over par on a lot that expires
> in two days, so I moved those across on a vehicle already running the route — no purchase, no
> write-off. The remaining twenty-six went to RFQ and Bay Supply won it at two-oh-five a unit.
> Fifty-three thirty. Want me to release it?"

That is the stage moment: one shortage in, one decision out, spoken.

Pick a calm, low-affect voice. A dramatic narrator voice undercuts the "this is infrastructure"
framing.

---

## 3. Path B — the pre-rendered fallback

Not a parallel build; a five-minute insurance policy. Frontier Tower wifi at 5:10pm with a full room
is exactly when a live API call picks its moment. Quota is not the concern — Creator's 275 minutes
is ample — network is.

```bash
export ELEVENLABS_API_KEY=...
curl -X POST "https://api.elevenlabs.io/v1/text-to-speech/$VOICE_ID" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Downtown is thirty-six units short for the weekend. Marina is ten over par on a lot that expires in two days, so I moved those across on a vehicle already running the route — no purchase, no write-off. The remaining twenty-six went to RFQ and Bay Supply won it at two-oh-five a unit. Fifty-three thirty. Want me to release it?",
    "model_id": "eleven_multilingual_v2"
  }' --output mise-approval.mp3
```

Commit the `.mp3` to the repo and wire it to a button on the page. It plays from disk, so it cannot
fail on stage.

**Use Path B for the live pitch and Path A for the judges' table.** The stage asset must be
identical every rehearsal and immune to the network; the interactive agent is what makes an
ElevenLabs judge remember you, and 10 concurrent calls means several judges can try it at once.

---

## 4. Time budget

| | |
|---|---|
| Create agent, paste system prompt, set public + allowlist | 20 min |
| **Decision gate** — if the dashboard is fighting you, abandon Path A and ship Path B alone | — |
| Embed and test on the live site | 10 min |
| Render the fallback mp3, wire the button | 10 min |
| **Total** | **~40 min** |

The sponsor track requires a project *built using their tools*. It does not require conversational
AI. If Path A resists, Path B alone still qualifies, still demos, and cannot fail.

---

## 5. What this adds to the reuse disclosure

Nothing of this existed before 19 Sep 2026. It is the cleanest answer to "what did you build today?"
— a product capability, not a document, with its own commit history.
