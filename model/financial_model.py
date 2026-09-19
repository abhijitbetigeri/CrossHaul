"""Mise — 3-year financial model.

A monthly cohort model, not a spreadsheet of round numbers. Every output below is
computed from the INPUTS block; change an input and the whole model re-derives, which
is the only way an assumption can honestly be argued with.

Run:  python3 model/financial_model.py
"""

from dataclasses import dataclass, field

# ── INPUTS — every assumption in the model lives here ────────────────────────

PRICE_PER_LOCATION_MONTH = 249.0

# Groups (customers) signed each month. Founder-led in year 1; two AEs from month 13.
NEW_GROUPS = (
    [0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]                    # Y1 — 17
    + [3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5]                  # Y2 — 47
    + [8, 8, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12]          # Y3 — 121
)

# Locations per group. Early customers skew to the small end of the 3-20 beachhead;
# larger groups land as references accumulate.
AVG_GROUP_SIZE = [6.0] * 12 + [6.2] * 12 + [6.5] * 12

# Monthly logo churn. Multi-unit operators are more durable than single sites, but
# restaurants do close — this is not a 0.5%/mo enterprise-software number.
MONTHLY_CHURN = [0.015] * 12 + [0.012] * 12 + [0.010] * 12

# Cost of revenue per location per month: LLM inference, hosting, payments, and the
# customer-success load. Falls with scale and cheaper inference, not to zero.
COGS_PER_LOCATION_MONTH = [60.0] * 12 + [48.0] * 12 + [40.0] * 12

# Cash cost to acquire one group. Year 1 is founder-led so it is mostly tooling.
CAC_PER_GROUP = [2000.0] * 12 + [6000.0] * 12 + [5500.0] * 12

# Operating expense excluding COGS and CAC: salaries, tools, infrastructure.
# Y1: founder + 1 engineer. Y2: 6 people. Y3: 12 people.
MONTHLY_OPEX = [17_500.0] * 12 + [71_700.0] * 12 + [154_200.0] * 12

LTV_HORIZON_MONTHS = 36  # LTV capped at 3 years — deliberately conservative.


# ── MODEL ────────────────────────────────────────────────────────────────────

@dataclass
class Month:
    n: int
    groups_start: float
    groups_new: float
    groups_churned: float
    groups_end: float
    locations: float
    revenue: float
    cogs: float
    gross_profit: float
    cac_spend: float
    opex: float
    ebitda: float
    arr: float


def run() -> list[Month]:
    months: list[Month] = []
    groups = 0.0

    for i in range(36):
        start = groups
        churned = start * MONTHLY_CHURN[i]
        new = NEW_GROUPS[i]
        end = start - churned + new

        # Revenue on the average base for the month — a customer signed mid-month
        # does not pay a full month.
        avg_groups = (start + end) / 2
        locations = avg_groups * AVG_GROUP_SIZE[i]

        revenue = locations * PRICE_PER_LOCATION_MONTH
        cogs = locations * COGS_PER_LOCATION_MONTH[i]
        gross_profit = revenue - cogs
        cac_spend = new * CAC_PER_GROUP[i]
        opex = MONTHLY_OPEX[i]

        months.append(Month(
            n=i + 1,
            groups_start=start, groups_new=new, groups_churned=churned, groups_end=end,
            locations=locations, revenue=revenue, cogs=cogs, gross_profit=gross_profit,
            cac_spend=cac_spend, opex=opex,
            ebitda=gross_profit - cac_spend - opex,
            arr=end * AVG_GROUP_SIZE[i] * PRICE_PER_LOCATION_MONTH * 12,
        ))
        groups = end

    return months


def year_slice(months: list[Month], y: int) -> list[Month]:
    return months[y * 12:(y + 1) * 12]


def money(x: float) -> str:
    if abs(x) >= 1_000_000:
        return f"${x/1_000_000:,.2f}M"
    return f"${x:,.0f}"


def main() -> None:
    m = run()

    # ── P&L summary ──────────────────────────────────────────────────────────
    print("### Three-year P&L\n")
    print("| | Year 1 | Year 2 | Year 3 |")
    print("|---|---:|---:|---:|")

    rows: list[tuple[str, list[str]]] = []
    agg = [year_slice(m, y) for y in range(3)]

    rows.append(("Groups (end of year)", [f"{a[-1].groups_end:,.0f}" for a in agg]))
    rows.append(("Locations (end of year)",
                 [f"{a[-1].groups_end * AVG_GROUP_SIZE[a[-1].n - 1]:,.0f}" for a in agg]))
    rows.append(("**Ending ARR**", [f"**{money(a[-1].arr)}**" for a in agg]))
    rows.append(("Revenue (recognised)", [money(sum(x.revenue for x in a)) for a in agg]))
    rows.append(("Cost of revenue", [money(-sum(x.cogs for x in a)) for a in agg]))
    rows.append(("**Gross profit**", [f"**{money(sum(x.gross_profit for x in a))}**" for a in agg]))
    rows.append(("Gross margin",
                 [f"{100*sum(x.gross_profit for x in a)/sum(x.revenue for x in a):.0f}%" for a in agg]))
    rows.append(("Sales & marketing (CAC)", [money(-sum(x.cac_spend for x in a)) for a in agg]))
    rows.append(("Operating expense", [money(-sum(x.opex for x in a)) for a in agg]))
    rows.append(("**EBITDA**", [f"**{money(sum(x.ebitda for x in a))}**" for a in agg]))
    # The installed base excluding growth spend. CAC is discretionary and pays back in
    # ~4 months, so this line is the one that says whether the business works.
    rows.append(("*EBITDA before growth spend*",
                 [f"*{money(sum(x.gross_profit - x.opex for x in a))}*" for a in agg]))

    for label, vals in rows:
        print(f"| {label} | " + " | ".join(vals) + " |")

    # ── Unit economics ───────────────────────────────────────────────────────
    y3 = agg[2]
    gs = AVG_GROUP_SIZE[-1]
    churn = MONTHLY_CHURN[-1]
    arpu_group_month = gs * PRICE_PER_LOCATION_MONTH
    gm = sum(x.gross_profit for x in y3) / sum(x.revenue for x in y3)
    gp_group_month = arpu_group_month * gm

    # LTV capped at 36 months, survival-weighted.
    ltv = sum(gp_group_month * ((1 - churn) ** t) for t in range(LTV_HORIZON_MONTHS))
    cac = CAC_PER_GROUP[-1]

    print("\n### Unit economics (steady state, year 3)\n")
    print("| | |")
    print("|---|---:|")
    print(f"| ARPU per group / month | ${arpu_group_month:,.0f} |")
    print(f"| ARPU per group / year | ${arpu_group_month*12:,.0f} |")
    print(f"| Gross margin | {gm*100:.0f}% |")
    print(f"| Gross profit per group / month | ${gp_group_month:,.0f} |")
    print(f"| CAC per group | ${cac:,.0f} |")
    print(f"| **CAC payback** | **{cac/gp_group_month:.1f} months** |")
    print(f"| LTV (36-month cap, churn-weighted) | ${ltv:,.0f} |")
    print(f"| **LTV / CAC** | **{ltv/cac:.1f}×** |")
    print(f"| Monthly logo churn | {churn*100:.1f}% |")
    print(f"| Annual logo churn | {(1-(1-churn)**12)*100:.1f}% |")

    # ── Cash ─────────────────────────────────────────────────────────────────
    cum, trough, trough_m = 0.0, 0.0, 0
    for x in m:
        cum += x.ebitda
        if cum < trough:
            trough, trough_m = cum, x.n

    RAISE = 1_500_000.0

    print("\n### Cash\n")
    print("| | |")
    print("|---|---:|")
    for y in range(3):
        print(f"| Year {y+1} net burn | {money(-sum(x.ebitda for x in agg[y]))} |")

    # Runway on the raise: the month the cumulative burn exhausts it.
    cum = 0.0
    runway_m = 36
    for x in m:
        cum += x.ebitda
        if -cum > RAISE:
            runway_m = x.n - 1
            break
    cum_24 = -sum(x.ebitda for x in m[:24])

    print(f"| Cumulative burn through month 24 | {money(cum_24)} |")
    print(f"| **Pre-seed raise** | **{money(RAISE)}** |")
    print(f"| Runway on that raise | ~{runway_m} months |")
    print(f"| ARR at month 24 (Series Seed milestone) | {money(m[23].arr)} |")
    print(f"| Gross profit vs opex, year 3 | "
          f"{money(sum(x.gross_profit for x in agg[2]))} vs "
          f"{money(sum(x.opex for x in agg[2]))} |")


if __name__ == "__main__":
    main()
