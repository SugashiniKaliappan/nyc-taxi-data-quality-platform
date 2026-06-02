# NYC Taxi Data Quality Platform

## Overview

The NYC Taxi Data Quality Platform is an automated Data Engineering solution designed to profile, validate, monitor, and detect anomalies in large-scale taxi trip datasets.

The platform processes millions of NYC Yellow Taxi records and performs automated quality assessments through rule-based validation, statistical profiling, anomaly detection, and data drift monitoring.

The project demonstrates real-world Data Engineering practices commonly used in modern data platforms to ensure data reliability, trustworthiness, and operational excellence.

---

## Business Problem

Data quality issues directly impact analytics, reporting, machine learning models, and business decision-making.

Common issues observed in transportation datasets include:

* Invalid trip durations
* Negative fare amounts
* Missing passenger information
* Unrealistic trip distances
* Data distribution changes over time
* Outlier records affecting downstream analytics

This platform provides automated controls to identify and monitor these issues before data reaches consumers.

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

* ~2.96 Million records per month
* 19 columns
* Multiple numerical and categorical attributes

Examples:

* VendorID
* Pickup Datetime
* Dropoff Datetime
* Passenger Count
* Trip Distance
* Fare Amount
* Tip Amount
* Total Amount

---

## Architecture

```text
Raw Taxi Dataset
        │
        ▼
Data Profiling
        │
        ▼
Quality Validation Rules
        │
        ▼
Anomaly Detection
        │
        ▼
Drift Detection
        │
        ▼
Reports Generation
        │
        ▼
Dashboard / Monitoring
```

---

## Features

### 1. Data Profiling

Generates statistical summaries for every column.

Metrics include:

* Data type analysis
* Null count
* Null percentage
* Distinct values
* Minimum values
* Maximum values
* Mean
* Median

Example findings:

* Passenger Count null rate: 4.73%
* Trip Distance max value: 312,722.3
* Fare Amount minimum value: -899

---

### 2. Rule-Based Quality Checks

Automated validation rules evaluate business-critical data quality constraints.

Implemented Rules:

#### Pickup Before Dropoff

Ensures pickup timestamp occurs before dropoff timestamp.

Severity: HIGH

---

#### Positive Trip Distance

Ensures trip distance is greater than zero.

Severity: HIGH

---

#### Non-Negative Fare

Ensures fare amounts are not negative.

Severity: HIGH

---

#### Valid Passenger Count

Ensures passenger count remains within acceptable limits.

Severity: MEDIUM

---

### Sample Quality Results

| Metric         | Value     |
| -------------- | --------- |
| Total Records  | 2,964,624 |
| Rules Executed | 4         |
| Rules Failed   | 3         |
| Quality Score  | 98.91%    |

---

## 3. Anomaly Detection

The platform identifies abnormal records using statistical outlier detection.

### Method

Interquartile Range (IQR)

Formula:

Upper Bound = Q3 + 1.5 × IQR

Lower Bound = Q1 - 1.5 × IQR

Analyzed Features:

* Trip Distance
* Fare Amount
* Tip Amount
* Tolls Amount
* Total Amount

### Example Findings

#### Trip Distance

* Upper Threshold: 6.28
* Outliers Detected: 382,745

#### Fare Amount

* Upper Threshold: 38.35
* Outliers Detected: 318,801

---

## 4. Data Drift Detection

Data drift monitoring compares multiple months of taxi data to identify distribution changes.

### Comparison

January 2024 vs February 2024

### Objective

Detect:

* Distribution shifts
* Feature instability
* Upstream ingestion issues
* Seasonal behavior changes

Outputs:

* Drift metrics
* Feature comparison reports
* Monitoring reports

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
│   └── drift/
│       └── drift_detection.py
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

### GitHub Actions

The entire pipeline is automated using GitHub Actions.

Workflow Stages:

1. Install dependencies
2. Execute profiling
3. Run quality checks
4. Detect anomalies
5. Perform drift analysis
6. Generate reports

Benefits:

* Repeatable execution
* CI/CD integration
* Automated monitoring
* Version-controlled workflows

---

## Technology Stack

### Programming

* Python

### Data Processing

* Pandas
* NumPy

### Storage

* Parquet

### Orchestration

* GitHub Actions

### Version Control

* Git
* GitHub

---

## Sample Results

### Quality Score

98.91%

### Failed Quality Records

* Invalid Trip Distance: 60,371
* Negative Fare Amount: 37,448
* Invalid Passenger Count: 31,525

### Anomalies Detected

* Trip Distance Outliers: 382,745
* Fare Amount Outliers: 318,801
* Total Amount Outliers: 363,621

---

## Future Enhancements

* Great Expectations integration
* PyDeequ validation framework
* Airflow orchestration
* Data Quality Dashboard
* Slack Alerts
* Email Notifications
* AWS Deployment
* Real-Time Streaming Validation using Kafka
* Machine Learning based anomaly detection

---

## Key Learnings

* Data profiling at scale
* Data quality rule engineering
* Statistical anomaly detection
* Data drift monitoring
* Workflow automation
* Production-oriented Data Engineering practices

---

## Author

Sugashini Kaliappan

