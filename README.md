# PuPrime Anomaly Detection Pipeline

An automated anomaly detection system that monitors trading activity and flags 
suspicious behaviour for risk and compliance teams at online forex brokers.

## Project Overview

This pipeline simulates the kind of real-time risk monitoring system used by 
trading platforms like PuPrime to detect unusual trader behaviour before it 
becomes a financial or compliance risk.

## Anomaly Types Detected

- **Unusual Volume** — trades with lot sizes exceeding normal thresholds
- **Rapid Trading** — traders executing too many trades in a short time window
- **Loss Streak** — traders experiencing consecutive losing trades (risk indicator)

## Features

- Generates realistic trade event data with injected anomalies
- Three independent anomaly detectors running in parallel
- Alerts saved to PostgreSQL database with full audit trail
- 78 alerts detected from 1000 trade events in testing
- Unit tested with pytest

## Tech Stack

- **Language:** Python 3.12
- **Database:** PostgreSQL (Neon cloud)
- **Libraries:** pandas, numpy, psycopg2, faker, python-dotenv
- **Testing:** pytest
- **Version Control:** Git/GitHub

## Project Structure
## Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Add your `.env` file:
4. Run the pipeline:
```bash
python src/pipeline/alerts_pipeline.py
```

## Sample Output
## Author

Matthew James — Data Engineer
GitHub: github.com/matthewoke94