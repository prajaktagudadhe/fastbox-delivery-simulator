import json
from simulator import (
    simulate,
    top_performer,
)

FILE = "base_case.json"

def main():
    with open(FILE) as f:
        data = json.load(f)
    (
        report,
        totals,
        delivered_count
    ) = simulate(data)
    print(
        "\nDELIVERY REPORT"
    )
    for item in report:
        print(item)
    print(
        "\nTOTAL DISTANCE"
    )
    for agent, d in totals.items():
        print(
            f"{agent}: {round(d,2)}"
        )
    best = top_performer(
        totals,
        delivered_count
    )
    print(
        "\nTOP PERFORMER:",
        best
    )
if __name__ == "__main__":
    main()
