import json
from pathlib import Path

import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

#BASE_DIR = Path("/Users/sugashinikaliappan/nyc-taxi-data-quality-platform")
BASE_DIR = Path(__file__).resolve().parents[2]
JAN_FILE = BASE_DIR / "data/raw/yellow_tripdata_2024-01.parquet"
FEB_FILE = BASE_DIR / "data/raw/yellow_tripdata_2024-02.parquet"

OUTPUT_FILE = BASE_DIR / "data/reports/drift_report_jan_vs_feb.json"

COLUMNS = [
    "passenger_count",
    "trip_distance",
    "fare_amount",
    "tip_amount",
    "total_amount"
]

print("Loading January...")
jan_df = pd.read_parquet(JAN_FILE)[COLUMNS]

print("Loading February...")
feb_df = pd.read_parquet(FEB_FILE)[COLUMNS]

jan_df = jan_df.dropna()
feb_df = feb_df.dropna()

jan_df = jan_df.sample(100000, random_state=42)
feb_df = feb_df.sample(100000, random_state=42)

print("Running drift detection...")

report = Report(
    metrics=[
        DataDriftPreset()
    ]
)

result = report.run(
    reference_data=jan_df,
    current_data=feb_df
)

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

try:
    report_dict = result.dict()
except AttributeError:
    try:
        report_dict = result.as_dict()
    except AttributeError:
        report_dict = json.loads(result.json())

OUTPUT_FILE.write_text(
    json.dumps(report_dict, indent=2, default=str),
    encoding="utf-8"
)

print(f"Drift report saved to: {OUTPUT_FILE}")
