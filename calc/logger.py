import logging
import os
from calc.logger import logger

def test_logger_creates_log_file(tmp_path, monkeypatch):
    # Redirect log file to a temp path using monkeypatch
    test_log_file = tmp_path / "test.log"
    monkeypatch.setenv("LOG_FILE", str(test_log_file))
    monkeypatch.setenv("LOG_LEVEL", "INFO")

    # Force re-import of the logger module to apply monkeypatched env vars
    import importlib
    import calc.logger
    importlib.reload(calc.logger)

    # Log a test message
    calc.logger.logger.info("This is a test log entry.")

    # Assert the log file was created and contains the expected message
    assert test_log_file.exists()
    with open(test_log_file) as f:
        log_content = f.read()
        assert "This is a test log entry." in log_content

