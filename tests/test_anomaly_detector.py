import pandas as pd
import pytest
import sys
sys.path.append("/workspaces/puprime-anomaly-detection")

from src.detection.anomaly_detector import (
    generate_trade_events,
    detect_unusual_volume,
    detect_loss_streak,
    run_all_detectors,
)


def test_generate_trade_events():
    df = generate_trade_events(100)
    assert len(df) == 100
    assert "trader_id" in df.columns
    assert "lot_size" in df.columns


def test_detect_unusual_volume():
    df = generate_trade_events(200)
    alerts = detect_unusual_volume(df, threshold=10.0)
    assert "alert_type" in alerts.columns
    assert all(alerts["lot_size"] > 10.0)


def test_detect_loss_streak():
    df = generate_trade_events(500)
    alerts = detect_loss_streak(df, streak_length=5)
    assert "alert_type" in alerts.columns
    if not alerts.empty:
        assert all(alerts["alert_type"] == "loss_streak")


def test_run_all_detectors_returns_dataframe():
    df = generate_trade_events(200)
    alerts = run_all_detectors(df)
    assert isinstance(alerts, pd.DataFrame)


def test_run_all_detectors_has_alert_columns():
    df = generate_trade_events(200)
    alerts = run_all_detectors(df)
    assert "alert_type" in alerts.columns
    assert "alert_reason" in alerts.columns