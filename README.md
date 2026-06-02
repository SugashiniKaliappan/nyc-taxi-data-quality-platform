# NYC Taxi Data Quality Platform

End-to-end Data Quality Engineering platform built on the NYC Yellow Taxi dataset.

The platform performs:

- Data Validation
- Data Profiling
- Anomaly Detection
- Data Drift Detection
- Email Alerting
- Interactive Dashboarding
- Automated CI/CD Execution with GitHub Actions

---

# Project Architecture

```text
NYC Taxi Dataset
        │
        ▼
Quality Validation
        │
        ▼
Data Profiling
        │
        ▼
Anomaly Detection
        │
        ▼
Drift Detection
        │
        ▼
Email Alert Evaluation
        │
        ▼
JSON Reports
        │
        ▼
Streamlit Dashboard
```

---

# Features

## Data Quality Validation

Business rules validation:

- Pickup before Dropoff
- Positive Trip Distance
- Non-Negative Fare Amount
- Valid Passenger Count

Outputs:

- Quality Report
- Failed Records Dataset
- Quality Score

---

## Data Profiling

Generates:

- Data Types
- Null Counts
- Null Percentages
- Distinct Counts
- Min Values
- Max Values
- Mean Values
- Median Values

Outputs:

- Profile Report

---

## Anomaly Detection

Uses IQR-based outlier detection.

Monitored columns:

- Trip Distance
- Fare Amount
- Tip Amount
- Tolls Amount
- Total Amount

Outputs:

- Anomaly Report
- Outlier Counts
- Upper and Lower Bounds

---

## Data Drift Detection

Compares:

```text
January Dataset
        vs
February Dataset
```

Monitors:

- Mean Drift
- Median Drift
- Distribution Changes

Outputs:

- Drift Report

---

## Email Alerting

Automatic email alerts are triggered when:

```text
Quality Score < Threshold
OR
Validation Rules Fail
```

Example:

```text
Dataset: yellow_tripdata_2024-01

Quality Score: 98.91%

Failed Rules:
- positive_trip_distance
- non_negative_fare
- valid_passenger_count
```

---

## Dashboard

Interactive Streamlit dashboard provides:

### Quality Monitoring

- Quality Score
- Rules Executed
- Rules Failed

### Profiling Insights

- Null Percentages
- Distinct Counts
- Statistical Summaries

### Anomaly Monitoring

- Outlier Counts
- IQR Boundaries

### Drift Monitoring

- January vs February Comparison
- Distribution Drift

### Alert Monitoring

- Alert Status
- Threshold Breaches

---

# Project Structure

```text
nyc-taxi-data-quality-platform/

├── .github/
│   └── workflows/
│       └── data-quality-pipeline.yml
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── reports/
│
├── src/
│   ├── validation/
│   │   ├── basic_quality_checks.py
│   │   └── rules.py
│   │
│   ├── profiling/
│   │   ├── profile_dataset.py
│   │   └── anomaly_detection.py
│   │
│   ├── drift/
│   │   └── drift_detection.py
│   │
│   └── alerts/
│       └── email_alert.py
│
├── dashboard.py
├── run_pipeline.py
├── requirements.txt
└── README.md
```

---

# Dataset

Source:

NYC Taxi & Limousine Commission (TLC)

Files used:

```text
yellow_tripdata_2024-01.parquet
yellow_tripdata_2024-02.parquet
```

Official Source:

https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

---

# Installation

Clone repository:

```bash
git clone https://github.com/SugashiniKaliappan/nyc-taxi-data-quality-platform.git

cd nyc-taxi-data-quality-platform
```

Create virtual environment:

```bash
python3 -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Pipeline

Execute complete pipeline:

```bash
python3 run_pipeline.py
```

Pipeline execution order:

```text
Quality Validation
        ↓
Data Profiling
        ↓
Anomaly Detection
        ↓
Drift Detection
        ↓
Email Alert Evaluation
```

The pipeline automatically performs:

- Data Validation
- Profiling
- Anomaly Detection
- Drift Detection
- Email Alerts

---

# Generated Reports

Reports are stored in:

```text
data/reports/
```

Generated outputs:

```text
quality_report_2024_01.json

profile_report_2024_01.json

anomaly_report_2024_01.json

drift_report_jan_vs_feb.json
```

Example output:

```text
Running: python3 src/validation/basic_quality_checks.py

Running: python3 src/profiling/profile_dataset.py

Running: python3 src/profiling/anomaly_detection.py

Running: python3 src/drift/drift_detection.py

Running: python3 src/alerts/email_alert.py

Data Quality pipeline completed successfully.
```

---

# Running Dashboard

Launch Streamlit dashboard:

```bash
streamlit run dashboard.py
```

Dashboard URL:

```text
http://localhost:8501
```

---

# Email Alert Configuration

SMTP Configuration:

```env
SMTP_HOST=smtp.gmail.com

SMTP_PORT=587

SMTP_USER=your_email@gmail.com

SMTP_PASSWORD=your_gmail_app_password

ALERT_RECIPIENT=recipient@gmail.com

QUALITY_SCORE_THRESHOLD=99.0
```

---

# GitHub Actions Automation

The project includes automated CI/CD execution using GitHub Actions.

Workflow:

```text
Push to Main Branch
        │
        ▼
Install Dependencies
        │
        ▼
Download Dataset
        │
        ▼
Run Pipeline
        │
        ▼
Generate Reports
        │
        ▼
Send Email Alerts
```

Benefits:

- Automated Execution
- CI/CD Integration
- Reproducible Pipelines
- Continuous Data Quality Monitoring

---

# Sample Quality Results

Dataset:

```text
yellow_tripdata_2024-01
```

Results:

| Metric | Value |
|----------|----------|
| Total Records | 2,964,624 |
| Rules Executed | 4 |
| Rules Failed | 3 |
| Quality Score | 98.91% |

Failed Rules:

- Positive Trip Distance
- Non Negative Fare
- Valid Passenger Count

---

# Technology Stack

### Data Engineering

- Python
- Pandas
- NumPy

### Data Quality

- Custom Validation Framework
- Statistical Profiling

### Monitoring

- Email Alerts
- Streamlit Dashboard

### Automation

- GitHub Actions

### Storage

- Parquet Files
- JSON Reports

---

# Future Enhancements

### Data Engineering

- Great Expectations Integration
- Apache Airflow Orchestration
- GCP Deployment
- Data Catalog Integration

### Monitoring

- Slack Alerts
- Microsoft Teams Alerts
- Grafana Dashboards

### Machine Learning

- ML-based Anomaly Detection
- Predictive Drift Monitoring

### Cloud

- GCS Storage
- Cloud Run Deployment
- Cloud Scheduler Automation

---

# Author

Sugashini Kaliappan

GitHub:

https://github.com/SugashiniKaliappan
