import json
from pathlib import Path

import pandas as pd

#BASE_DIR = Path("/Users/sugashinikaliappan/nyc-taxi-data-quality-platform")
BASE_DIR = Path(__file__).resolve().parents[2]

INPUT_FILE = (
    BASE_DIR / "data/raw/yellow_tripdata_2024-01.parquet"
)

REPORT_FILE = (
    BASE_DIR / "data/reports/anomaly_report_2024_01.json"
)

NUMERIC_COLUMNS = [
    "trip_distance",
    "fare_amount",
    "tip_amount",
    "tolls_amount",
    "total_amount"
]


def detect_outliers_iqr(df, column):

    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)

    iqr = q3 - q1

    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    outliers = df[
        (df[column] < lower_bound)
        | (df[column] > upper_bound)
    ]

    return {
        "column": column,
        "q1": round(float(q1), 2),
        "q3": round(float(q3), 2),
        "iqr": round(float(iqr), 2),
        "lower_bound": round(float(lower_bound), 2),
        "upper_bound": round(float(upper_bound), 2),
        "outlier_count": len(outliers),
        "max_value": round(float(df[column].max()), 2),
        "min_value": round(float(df[column].min()), 2)
    }


print("Loading data...")

df = pd.read_parquet(INPUT_FILE)

report = {
    "dataset": "yellow_tripdata_2024-01",
    "anomaly_results": []
}

for col in NUMERIC_COLUMNS:
    report["anomaly_results"].append(
        detect_outliers_iqr(df, col)
    )

REPORT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

REPORT_FILE.write_text(
    json.dumps(report, indent=2),
    encoding="utf-8"
)

print(
    f"Anomaly report saved to: {REPORT_FILE}"
)

print(
    json.dumps(report, indent=2)
)
