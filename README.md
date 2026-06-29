## Known Gaps & Future Improvements

* The anomaly detectors currently operate on simulated trading data. In a production environment, trade events would be ingested from a real-time streaming platform such as Apache Kafka or a database change data capture (CDC) pipeline.
* The `detect_rapid_trading()` function uses an O(n²) sliding-window approach for each trader. While suitable for this project's dataset, a production-scale implementation would require a more efficient algorithm to process millions of trade events with low latency.
* Alerts are persisted in the database, but there is no automated notification layer. A production-ready system could integrate with Slack, Microsoft Teams, email, or PagerDuty to notify compliance teams in real time.
* Detection thresholds (e.g., lot size, trading window, and rapid-trade limits) are currently hardcoded. A production implementation would store these as configurable business rules that can be adjusted per instrument, account type, or risk policy without modifying the codebase.

## Business Value

This project demonstrates how a data engineering pipeline can support automated trading surveillance and risk monitoring within a brokerage environment. By identifying suspicious trading patterns early, the system helps reduce financial risk, improve regulatory compliance, and provide compliance teams with a centralized, queryable alerts repository for investigation, auditing, and reporting.

## Author

**Matthew James**
**Data Engineer | Python | SQL | ETL | Data Pipelines**
GitHub: github.com/matthewoke94
