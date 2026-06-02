import json
from pathlib import Path
import pandas as pd

#BASE_DIR = Path("/Users/sugashinikaliappan/nyc-taxi-data-quality-platform")
BASE_DIR = Path(__file__).resolve().parents[2]
INPUT_FILE = BASE_DIR / "data/raw/yellow_tripdata_2024-01.parquet"
PROFILE_FILE = BASE_DIR / "data/reports/profile_report_2024_01.json"

NUMERIC_COLUMNS = [
    "passenger_count",
    "trip_distance",
    "fare_amount",
    "tip_amount",
    "tolls_amount",
    "total_amount"
]


print("Loading data...")
df = pd.read_parquet(INPUT_FILE)

profile = {
    "dataset": "yellow_tripdata_2024-01",
    "total_records": len(df),
    "total_columns": len(df.columns),
    "columns": {}
}

for col in df.columns:
    column_profile = {
        "dtype": str(df[col].dtype),
        "null_count": int(df[col].isnull().sum()),
        "null_percent": round((df[col].isnull().sum() / len(df)) * 100, 2),
        "distinct_count": int(df[col].nunique(dropna=True))
    }

    if col in NUMERIC_COLUMNS:
        column_profile.update({
            "min": float(df[col].min()),
            "max": float(df[col].max()),
            "mean": round(float(df[col].mean()), 2),
            "median": round(float(df[col].median()), 2)
        })

    profile["columns"][col] = column_profile

PROFILE_FILE.parent.mkdir(parents=True, exist_ok=True)
PROFILE_FILE.write_text(json.dumps(profile, indent=2), encoding="utf-8")

print(f"Profile report saved to: {PROFILE_FILE}")
print(json.dumps(profile, indent=2)[:3000])
