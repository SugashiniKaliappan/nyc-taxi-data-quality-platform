# NYC Taxi Data Quality Platform

## Overview

The NYC Taxi Data Quality Platform is an automated Data Engineering solution designed to profile, validate, monitor, and detect anomalies in large-scale taxi trip datasets.

The platform processes millions of NYC Yellow Taxi records and performs automated quality assessments through rule-based validation, statistical profiling, anomaly detection, data drift monitoring, and threshold-based email alerting.

The project demonstrates real-world Data Engineering practices commonly used in modern data platforms to ensure data reliability, trustworthiness, and operational excellence.

---

## Key Features

* Data profiling
* Rule-based data quality validation
* Failed record isolation
* Quality score calculation
* Statistical anomaly detection
* Data drift detection
* Threshold-based email alerts
* GitHub Actions automation
* Streamlit dashboard

---

## Architecture

```text
Raw Taxi Dataset
        │
        ▼
Data Quality Validation
        │
        ▼
Failed Record Repository
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
Quality Report Generation
        │
        ▼
Threshold Evaluation
        │
        ▼
Email Alert Notification
        │
        ▼
Dashboard / Monitoring
```

---

## Dataset

### Source

NYC Taxi & Limousine Commission (TLC)

### Dataset Used

Yellow Taxi Trip Records

### Sample Period

* January 2024
* February 2024

### Scale

* ~2.96 million records per month
* 19 columns
* Numerical and categorical trip attributes

---

## Data Quality Rules

Implemented validation rules:

| Rule                   | Description                                    | Severity |
| ---------------------- | ---------------------------------------------- | -------- |
| Pickup Before Dropoff  | Pickup time should be before dropoff time      | HIGH     |
| Positive Trip Distance | Trip distance should be greater than zero      | HIGH     |
| Non-Negative Fare      | Fare amount should not be negative             | HIGH     |
| Valid Passenger Count  | Passenger count should be between valid limits | MEDIUM   |

---

## Sample Quality Results

| Metric         |     Value |
| -------------- | --------: |
| Total Records  | 2,964,624 |
| Rules Executed |         4 |
| Rules Failed   |         3 |
| Quality Score  |    98.91% |

Failed records are stored separately under:

```text
data/processed/failed_records/
```

---

## Anomaly Detection

The platform identifies statistical outliers using the Interquartile Range method.

### Method

```text
Upper Bound = Q3 + 1.5 × IQR
Lower Bound = Q1 - 1.5 × IQR
```

Analyzed features:

* Trip Distance
* Fare Amount
* Tip Amount
* Tolls Amount
* Total Amount

### Example Findings

| Feature       | Outliers Detected |
| ------------- | ----------------: |
| Trip Distance |           382,745 |
| Fare Amount   |           318,801 |
| Total Amount  |           363,621 |

---

## Data Drift Detection

The drift module compares January 2024 and February 2024 taxi datasets to detect distribution changes.

Drift monitoring helps identify:

* Feature distribution shifts
* Upstream ingestion changes
* Seasonal behavior changes
* Data instability over time

Output:

```text
data/reports/drift_report_jan_vs_feb.json
```

---

## Email Alerting

The platform includes threshold-based email alerts.

An alert is triggered when:

```text
Quality Score < Configured Threshold
OR
One or more rules fail
```

Example threshold:

```text
QUALITY_SCORE_THRESHOLD=99.0
```

Since the current quality score is 98.91%, the email alert is triggered successfully.

### Alert Contents

The email alert includes:

* Dataset name
* Total records processed
* Quality score
* Threshold value
* Number of failed rules
* Failed rule names
* Severity
* Owner
* Failed record counts

### Environment Variables

Create a `.env` file locally:

```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_gmail_app_password
ALERT_RECIPIENT=recipient_email@gmail.com
QUALITY_SCORE_THRESHOLD=99.0
```

Do not commit `.env` to GitHub.

---

## Project Structure

```text
nyc-taxi-data-quality-platform/

├── .github/
│   └── workflows/
│       └── data-quality-pipeline.yml
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
├── data/
│   ├── raw/
│   ├── processed/
│   └── reports/
│
├── dashboard.py
├── run_pipeline.py
├── requirements.txt
└── README.md
```

---

## Automation

### Local Pipeline

Run the full pipeline locally:

```bash
python3 run_pipeline.py
```

Pipeline stages:

```text
quality_checks
profiling
anomaly_detection
drift_detection
email_alert
```

---

## GitHub Actions

The project includes GitHub Actions workflow automation.

Workflow stages:

1. Checkout repository
2. Set up Python
3. Install dependencies
4. Download NYC Taxi datasets
5. Run data quality pipeline

---

## Technology Stack

### Programming

* Python

### Data Processing

* Pandas
* NumPy
* PyArrow

### Data Quality & Monitoring

* Rule-based validation
* IQR anomaly detection
* Evidently AI for drift detection

### Alerting

* SMTP
* Gmail App Password
* python-dotenv

### Dashboard

* Streamlit

### Automation

* GitHub Actions

### Version Control

* Git
* GitHub

---

## Sample Results

### Quality Score

```text
98.91%
```

### Failed Quality Records

* Invalid Trip Distance: 60,371
* Negative Fare Amount: 37,448
* Invalid Passenger Count: 31,525

### Anomalies Detected

* Trip Distance Outliers: 382,745
* Fare Amount Outliers: 318,801
* Total Amount Outliers: 363,621

### Email Alert

```text
Email alert sent successfully when quality threshold was breached.
```

---

## Future Enhancements

* Add JSON report attachment to alert email
* Add Slack alert integration
* Add Great Expectations validation
* Add PyDeequ validation framework
* Add Airflow or Dagster orchestration
* Add cloud deployment on GCP or AWS
* Add real-time streaming validation with Kafka
* Add ML-based anomaly detection
* Add historical trend dashboard

---

## Author

Sugashini Kaliappan

Senior Data Engineer | Data Science Graduate | Data Quality Engineering Enthusiast
