"""CrossHaul — inference routing by reasoning complexity.

Built 19 Sep 2026, Dream AI Hackathon. NEW.

The financial model commits to cost of revenue falling from $60 to $40 per location per month,
carrying gross margin from 76% to 84%. This file is the part of that which is an engineering
decision rather than a scale effect.

The argument: CrossHaul makes calls of very different reasoning complexity, and routing them all to
a frontier model is the same mistake as running every query on your largest database instance.
Matching the ingredient in the crate is not the same problem as clearing a multi-constraint
rebalance across seven sites against supplier minimums and expiry windows.

    High volume, low reasoning   -> open-weights models on Nebius Token Factory
    Low volume, high reasoning   -> Claude Opus 5

Run:
    python3 inference/router.py              # the cost model
    python3 inference/router.py --live       # also proves the Nebius call works (needs a key)
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass

# ── Prices, $ per million tokens ─────────────────────────────────────────────
# Anthropic first-party rates. Nebius Token Factory publishes "from $0.06 per 1M input"; the
# figures below are a conservative mid-size open-weights estimate and are LABELLED AS ESTIMATES
# because they are the one input here not taken from a published rate card.
PRICES = {
    "claude-opus-5":   (5.00, 25.00),   # multi-constraint decisions
    "claude-sonnet-5": (2.00, 10.00),   # operator dialogue
    "claude-haiku-4-5": (1.00, 5.00),   # simple structured transforms
    "nebius-open":     (0.10, 0.30),    # ESTIMATE — Nebius Token Factory, open-weights
}


@dataclass
class Workload:
    """One call class in the CrossHaul loop, sized per location per month."""
    name: str
    why: str
    input_tokens: int          # per location per month
    output_tokens: int
    routed_to: str             # the model this class should run on
    reasoning: str             # low | medium | high


# Sized for a real site: ~200 tracked SKUs, a weekly cycle (4.3/month), batched calls.
WORKLOADS = [
    Workload(
        "Demand forecast", "Per SKU per site. Structured in, structured out, no judgement.",
        input_tokens=258_000, output_tokens=69_000,
        routed_to="nebius-open", reasoning="low",
    ),
    Workload(
        "Market intelligence", "Bulk extraction from scraped pages. High volume, mechanical.",
        input_tokens=60_000, output_tokens=12_000,
        routed_to="nebius-open", reasoning="low",
    ),
    Workload(
        "Promotion sweep", "Turn near-expiry surplus into a menu action. Narrow, templated.",
        input_tokens=8_600, output_tokens=2_600,
        routed_to="claude-haiku-4-5", reasoning="low",
    ),
    Workload(
        "Operator dialogue", "Voice and chat. Needs fluency and refusal to invent numbers.",
        input_tokens=90_000, output_tokens=24_000,
        routed_to="claude-sonnet-5", reasoning="medium",
    ),
    Workload(
        "Rebalance + procurement",
        "Match surplus to shortage across sites under expiry, distance, supplier minimums and "
        "landed cost, then justify it to a human who will approve a spend. The product IS this call.",
        input_tokens=34_000, output_tokens=8_600,
        routed_to="claude-opus-5", reasoning="high",
    ),
]

BASELINE_MODEL = "claude-opus-5"   # the naive architecture: everything on the best model


def cost(model: str, tokens_in: int, tokens_out: int) -> float:
    pin, pout = PRICES[model]
    return tokens_in / 1e6 * pin + tokens_out / 1e6 * pout


def main() -> None:
    print("### Inference cost per location per month\n")
    print("| Call class | Reasoning | Routed to | All-Opus | Routed | Saved |")
    print("|---|---|---|---:|---:|---:|")

    base_total = routed_total = 0.0
    for w in WORKLOADS:
        b = cost(BASELINE_MODEL, w.input_tokens, w.output_tokens)
        r = cost(w.routed_to, w.input_tokens, w.output_tokens)
        base_total += b
        routed_total += r
        print(f"| {w.name} | {w.reasoning} | `{w.routed_to}` | "
              f"${b:.3f} | ${r:.3f} | ${b - r:.3f} |")

    saved = base_total - routed_total
    print(f"| **Total** | | | **${base_total:.2f}** | **${routed_total:.2f}** "
          f"| **${saved:.2f}** |")
    print(f"\nRouting removes **{100 * saved / base_total:.0f}%** of inference cost — and the one "
          f"call that decides how money is spent stays on the frontier model.\n")

    # ── Honesty about what this does and does not do to gross margin ─────────
    COGS_Y1, COGS_Y3, PRICE = 60.0, 40.0, 249.0
    print("### What that is worth against the model\n")
    print("| | |")
    print("|---|---:|")
    print(f"| Price per location per month | ${PRICE:.0f} |")
    print(f"| Modelled cost of revenue, year 1 | ${COGS_Y1:.0f} |")
    print(f"| Modelled cost of revenue, year 3 | ${COGS_Y3:.0f} |")
    print(f"| Inference, unrouted | ${base_total:.2f} |")
    print(f"| Inference, routed | ${routed_total:.2f} |")
    print(f"| Saving as a share of the $20 COGS reduction | "
          f"{100 * saved / (COGS_Y1 - COGS_Y3):.0f}% |")

    print("\n**Stated honestly: inference is not the dominant line in cost of revenue — customer "
          "success is.** Routing contributes roughly a fifth of the modelled $60 → $40 reduction. "
          "The rest comes from support cost per location falling with scale. Both are required, "
          "and claiming inference alone carries the margin story would not survive a question.\n")

    if "--live" in sys.argv:
        live_check()


def live_check() -> None:
    """Prove the Nebius path actually works. Optional — the cost model stands without it."""
    key = os.environ.get("NEBIUS_API_KEY")
    if not key:
        print("### Live check\n\nSkipped — set NEBIUS_API_KEY to run it "
              "(hackathon participants get $50 of credit).")
        return

    # Nebius Token Factory is OpenAI-compatible, so this is a plain POST. Deliberately stdlib
    # only — a demo a judge might run should not need a pip install first.
    import json
    import urllib.error
    import urllib.request

    prompt = (
        "Site: Downtown. Ingredient: Roma tomatoes. On hand 4.0 kg, par 40 kg. "
        "Forecast burn 14.4 kg/day. Reply with ONLY the number of days of cover, one decimal."
    )
    req = urllib.request.Request(
        "https://api.tokenfactory.nebius.com/v1/chat/completions",
        data=json.dumps({
            "model": "openai/gpt-oss-120b",
            "messages": [{"role": "user", "content": prompt}],
            # gpt-oss reasons before answering and the reasoning is billed as completion
            # tokens, so a tight cap returns a null content rather than a short answer.
            "max_tokens": 300,
            "temperature": 0,
        }).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = json.load(resp)
        answer = (body["choices"][0]["message"].get("content") or "").strip() or "(empty)"
        u = body["usage"]
        tin, tout = u["prompt_tokens"], u["completion_tokens"]
        print(f"### Live check — Nebius Token Factory\n")
        print(f"Model `openai/gpt-oss-120b` returned days-of-cover: **{answer}** (expected ~0.3)\n")
        print(f"{tin} in / {tout} out — **${cost('nebius-open', tin, tout):.6f}**. "
              f"The same call on Opus 5: **${cost('claude-opus-5', tin, tout):.6f}**.")
    except urllib.error.HTTPError as exc:
        print(f"### Live check\n\nHTTP {exc.code}: {exc.read().decode()[:300]}")
    except Exception as exc:  # noqa: BLE001 — a demo script should report, not raise
        print(f"### Live check\n\nFailed: {exc}")


if __name__ == "__main__":
    main()
