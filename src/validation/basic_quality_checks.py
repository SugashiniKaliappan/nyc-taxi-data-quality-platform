import json
from pathlib import Path

import pandas as pd
from rules import QUALITY_RULES


# -----------------------------
# Paths
# -----------------------------
#BASE_DIR = Path(
#    "/Users/sugashinikaliappan/nyc-taxi-data-quality-platform"
#)

BASE_DIR = Path(__file__).resolve().parents[2]

INPUT_FILE = (
    BASE_DIR / "data/raw/yellow_tripdata_2024-01.parquet"
)

REPORT_FILE = (
    BASE_DIR / "data/reports/quality_report_2024_01.json"
)

FAILED_DIR = (
    BASE_DIR / "data/processed/failed_records"
)

FAILED_DIR.mkdir(parents=True, exist_ok=True)


# -----------------------------
# Helper Function
# -----------------------------
def create_rule_result(
    rule_name,
    failed_count,
    total_count
):
    rule = QUALITY_RULES[rule_name]

    passed_count = total_count - failed_count

    pass_rate = round(
        (passed_count / total_count) * 100,
        2
    )

    threshold = rule["threshold_percent"]

    return {
        "rule_name": rule_name,
        "description": rule["description"],
        "severity": rule["severity"],
        "owner": rule["owner"],
        "threshold_percent": threshold,
        "total_records": total_count,
        "passed_records": passed_count,
        "failed_records": failed_count,
        "pass_rate_percent": pass_rate,
        "status": (
            "PASS"
            if pass_rate >= threshold
            else "FAIL"
        )
    }


# -----------------------------
# Load Dataset
# -----------------------------
print("Loading data...")

df = pd.read_parquet(INPUT_FILE)

total_count = len(df)

print(f"Total records: {total_count:,}")


# -----------------------------
# Data Quality Checks
# -----------------------------

# Rule 1
invalid_time = df[
    df["tpep_pickup_datetime"]
    > df["tpep_dropoff_datetime"]
]

invalid_time.to_parquet(
    FAILED_DIR / "invalid_timestamp.parquet",
    index=False
)

# Rule 2
invalid_distance = df[
    df["trip_distance"] <= 0
]

invalid_distance.to_parquet(
    FAILED_DIR / "invalid_trip_distance.parquet",
    index=False
)

# Rule 3
invalid_fare = df[
    df["fare_amount"] < 0
]

invalid_fare.to_parquet(
    FAILED_DIR / "invalid_fare.parquet",
    index=False
)

# Rule 4
invalid_passengers = df[
    (df["passenger_count"] < 1)
    | (df["passenger_count"] > 6)
]

invalid_passengers.to_parquet(
    FAILED_DIR / "invalid_passenger_count.parquet",
    index=False
)


# -----------------------------
# Rule Results
# -----------------------------
results = []

results.append(
    create_rule_result(
        "pickup_before_dropoff",
        len(invalid_time),
        total_count
    )
)

results.append(
    create_rule_result(
        "positive_trip_distance",
        len(invalid_distance),
        total_count
    )
)

results.append(
    create_rule_result(
        "non_negative_fare",
        len(invalid_fare),
        total_count
    )
)

results.append(
    create_rule_result(
        "valid_passenger_count",
        len(invalid_passengers),
        total_count
    )
)


# -----------------------------
# Overall Report
# -----------------------------
report = {
    "dataset": "yellow_tripdata_2024-01",
    "total_records": total_count,
    "total_columns": len(df.columns),
    "rules_executed": len(results),
    "rules_failed": sum(
        1
        for r in results
        if r["status"] == "FAIL"
    ),
    "quality_score_percent": round(
        sum(
            r["pass_rate_percent"]
            for r in results
        ) / len(results),
        2
    ),
    "rule_results": results
}


# -----------------------------
# Save Report
# -----------------------------
REPORT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

REPORT_FILE.write_text(
    json.dumps(report, indent=2),
    encoding="utf-8"
)


# -----------------------------
# Console Output
# -----------------------------
print(
    f"\nQuality report saved to: {REPORT_FILE}"
)

print(
    f"Failed records saved to: {FAILED_DIR}"
)

print(
    json.dumps(
        report,
        indent=2
    )
)
