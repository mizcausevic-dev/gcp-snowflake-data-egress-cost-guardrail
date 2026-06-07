from dataclasses import dataclass

@dataclass(frozen=True)
class DataSignal:
    lane: str
    exposure: int
    savings: int
    investment: int
    board_story: str

SIGNALS = [
    DataSignal("GCP data egress pressure", 74, 28, 58, "Move data less often before buying more platform capacity."),
    DataSignal("Snowflake warehouse burn", 69, 34, 52, "Warehouse sizing must follow workload evidence, not dashboard urgency."),
    DataSignal("BigQuery to Snowflake lineage gap", 63, 18, 66, "Board-ready data products need provenance across both cloud and warehouse lanes."),
]

def rank(signals=SIGNALS):
    return sorted(
        ((round(s.exposure * 0.45 + s.savings * 0.25 + s.investment * 0.30), s) for s in signals),
        reverse=True,
        key=lambda item: item[0],
    )

if __name__ == "__main__":
    for priority, signal in rank():
        print(f"gcp-snowflake-data-egress-cost-guardrail | {signal.lane} | {priority} | {signal.board_story}")
