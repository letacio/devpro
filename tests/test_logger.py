import os
import pytest
from Task1_Logger import log_message

@pytest.fixture
def log_file():
    log_file = "test.log"
    yield log_file
    if os.path.exists(log_file):
        os.remove(log_file)

@pytest.mark.sequential_tests
def test_log_message_creates_file(log_file):
    log_message(log_file, "Test message", "INFO")
    assert os.path.exists(log_file)


def test_log_message_writes_message(log_file):
    log_message(log_file, "Test message", "INFO")
    with open(log_file, 'r') as f:
        lines = f.readlines()
        assert "Test message" in lines[0]


def test_log_message_appends_messages(log_file):
    log_message(log_file, "Test message 1", "INFO")
    log_message(log_file, "Test message 2", "WARNING")
    with open(log_file, 'r') as f:
        lines = f.readlines()
        assert "Test message 1" in lines[0]
        assert "Test message 2" in lines[1]