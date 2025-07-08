"""
Pytest configuration and shared fixtures for Evolutionary FSM tests.
"""

from pathlib import Path

import pytest


@pytest.fixture
def project_root():
    """
    Return the project root directory.
    """
    return Path(__file__).parent.parent


@pytest.fixture
def test_data_dir(project_root):
    """
    Return the test data directory.
    """
    return project_root / "tests" / "data"


@pytest.fixture
def sample_fsm_config():
    """
    Sample FSM configuration for testing.
    This will be expanded as you implement the FSM features.
    """
    return {
        "states": ["idle", "active", "error"],
        "transitions": [
            {"from": "idle", "to": "active", "trigger": "start"},
            {"from": "active", "to": "idle", "trigger": "stop"},
            {"from": "active", "to": "error", "trigger": "error"},
            {"from": "error", "to": "idle", "trigger": "reset"},
        ],
        "initial_state": "idle",
    }


@pytest.fixture
def sample_agent_config():
    """
    Sample agent configuration for testing.
    This will be expanded as you implement the agentic features.
    """
    return {
        "reasoning_engine": "rule_based",
        "evolution_triggers": ["performance_threshold", "feedback_loop"],
        "modification_strategies": ["add_state", "add_transition", "modify_behavior"],
    }
