<<<<<<< HEAD
## Known Gaps & Future Improvements

* The anomaly detectors currently operate on simulated trading data. In a production environment, trade events would be ingested from a real-time streaming platform such as Apache Kafka or a database change data capture (CDC) pipeline.
* The `detect_rapid_trading()` function uses an O(n²) sliding-window approach for each trader. While suitable for this project's dataset, a production-scale implementation would require a more efficient algorithm to process millions of trade events with low latency.
* Alerts are persisted in the database, but there is no automated notification layer. A production-ready system could integrate with Slack, Microsoft Teams, email, or PagerDuty to notify compliance teams in real time.
* Detection thresholds (e.g., lot size, trading window, and rapid-trade limits) are currently hardcoded. A production implementation would store these as configurable business rules that can be adjusted per instrument, account type, or risk policy without modifying the codebase.

## Business Value

This project demonstrates how a data engineering pipeline can support automated trading surveillance and risk monitoring within a brokerage environment. By identifying suspicious trading patterns early, the system helps reduce financial risk, improve regulatory compliance, and provide compliance teams with a centralized, queryable alerts repository for investigation, auditing, and reporting.
=======
# PuPrime Anomaly Detection Pipeline

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Pytest](https://img.shields.io/badge/Pytest-Tested-yellow)
![Pipeline](https://img.shields.io/badge/Anomaly-Detection-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

# Overview

The **PuPrime Anomaly Detection Pipeline** is a Python-based fraud and risk monitoring system that simulates trading activity, detects suspicious behaviour using configurable business rules, and stores generated alerts for investigation.

The project demonstrates how anomaly detection can be integrated into a trading platform to support compliance teams, risk analysts, and operational monitoring.

---

# Business Problem

Financial trading platforms process thousands of transactions every day.

Without automated monitoring, suspicious trading behaviour can go unnoticed, increasing financial risk and regulatory exposure.

Examples include:

- Abnormally large trade sizes
- Rapid consecutive trading
- Suspicious trading patterns
- High-risk trading behaviour

Manual monitoring is slow, inconsistent, and difficult to scale.

---

# Solution

This project builds an anomaly detection pipeline that:

- Simulates realistic trading activity
- Applies anomaly detection rules
- Flags suspicious events
- Stores alerts for investigation
- Produces structured data suitable for reporting dashboards

The detection logic is separated from the data source, allowing simulated data to be replaced with production trading data without changing the detection algorithms.

---

# Architecture

```text
Trading Data
      │
      ▼
Validation
      │
      ▼
Anomaly Detection Rules
      │
      ▼
Alert Generation
      │
      ▼
Alerts Database
```

---

# Detection Workflow

## Step 1 — Data Generation

Generate simulated trading activity including:

- Traders
- Orders
- Positions
- Trade Events

---

## Step 2 — Validation

Verify the generated dataset before processing.

Checks include:

- Valid trader references
- Valid timestamps
- Positive trade sizes
- Complete records

---

## Step 3 — Anomaly Detection

The detection engine evaluates trading behaviour against predefined business rules.

Example detections include:

- Large trade sizes
- Rapid trading activity
- Consecutive abnormal behaviour
- Suspicious trading sequences

Each detected event produces a structured alert.

---

## Step 4 — Alert Pipeline

Detected anomalies are stored for later investigation.

The alert pipeline enables compliance teams to:

- Review suspicious activity
- Filter alerts
- Investigate individual traders
- Generate audit reports

---

# Features

- Trading activity simulation
- Automated anomaly detection
- Business rule validation
- Alert generation
- Modular detection engine
- Automated testing
- GitHub Actions CI

---

# Reliability Features

| Feature | Description |
|----------|-------------|
| Validation | Rejects invalid records before detection |
| Modular Detection | Rules separated from pipeline |
| Automated Tests | Detection logic verified with Pytest |
| CI Pipeline | GitHub Actions validates every push |
| Reproducibility | Deterministic simulated datasets |

---

# Technology Stack

## Language

- Python 3.12

## Libraries

- Pandas
- Faker
- Pytest

## Development

- Git
- GitHub
- GitHub Actions

---

# Project Structure

```text
puprime-anomaly-detection/

├── src/
│   ├── detection/
│   └── pipeline/
│
├── tests/
│   └── test_anomaly_detector.py
│
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/matthewoke94/puprime-anomaly-detection.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the anomaly detection pipeline

```bash
python src/pipeline/alerts_pipeline.py
```

---

# Testing

Run the automated tests

```bash
pytest
```
>>>>>>> 72fd3dc (Improve project documentation)

---

<<<<<<< HEAD
**Matthew James**
**Data Engineer | Python | SQL | ETL | Data Pipelines**
GitHub: github.com/matthewoke94
=======
# Future Improvements

- Kafka event streaming
- PostgreSQL backend
- Apache Airflow scheduling
- Docker deployment
- Email and Slack alert notifications
- Cloud deployment (AWS/Azure)

---

# Business Value

This project demonstrates how automated anomaly detection can improve operational monitoring within financial institutions.

The solution helps organizations:

- Detect suspicious trading behaviour
- Improve compliance processes
- Reduce operational risk
- Support regulatory reporting
- Enable faster investigations

---

# Author

**Matthew James**

**Data Engineer**

GitHub:

https://github.com/matthewoke94

---

# License

This project is released under the MIT License.
>>>>>>> 72fd3dc (Improve project documentation)
