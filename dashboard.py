import json
from pathlib import Path

import pandas as pd
import streamlit as st

BASE_DIR = Path("/Users/sugashinikaliappan/nyc-taxi-data-quality-platform")

QUALITY_REPORT = BASE_DIR / "data/reports/quality_report_2024_01.json"
ANOMALY_REPORT = BASE_DIR / "data/reports/anomaly_report_2024_01.json"
PROFILE_REPORT = BASE_DIR / "data/reports/profile_report_2024_01.json"
DRIFT_REPORT = BASE_DIR / "data/reports/drift_report_jan_vs_feb.json"


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


st.set_page_config(
    page_title="NYC Taxi Data Quality Dashboard",
    layout="wide"
)

st.title("NYC Taxi Data Quality & Observability Dashboard")

quality = load_json(QUALITY_REPORT)
anomaly = load_json(ANOMALY_REPORT)
profile = load_json(PROFILE_REPORT)

st.header("Executive Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Dataset", quality["dataset"])
col2.metric("Records", f"{quality['total_records']:,}")
col3.metric("Quality Score", f"{quality['quality_score_percent']}%")
col4.metric("Rules Failed", quality["rules_failed"])

st.header("Data Quality Rule Results")

rule_df = pd.DataFrame(quality["rule_results"])
st.dataframe(rule_df, use_container_width=True)

st.header("Anomaly Detection Summary")

anomaly_df = pd.DataFrame(anomaly["anomaly_results"])
st.dataframe(anomaly_df, use_container_width=True)

st.header("Column Profiling Summary")

profile_rows = []

for col, details in profile["columns"].items():
    row = {"column": col}
    row.update(details)
    profile_rows.append(row)

profile_df = pd.DataFrame(profile_rows)
st.dataframe(profile_df, use_container_width=True)

st.header("Drift Detection")

if DRIFT_REPORT.exists():
    st.success("Drift report generated successfully: Jan 2024 vs Feb 2024")
    st.write(str(DRIFT_REPORT))
else:
    st.warning("Drift report not found.")
