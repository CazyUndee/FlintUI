"""Shared pytest fixtures for CronixUI tests."""

import sys
from pathlib import Path

import pytest

# Add the python package to the path so we can import cronixui
PYTHON_PACKAGE_PATH = Path(__file__).parent.parent / "packages" / "python"
sys.path.insert(0, str(PYTHON_PACKAGE_PATH))


@pytest.fixture
def sample_html_content():
    """Provide sample HTML content for testing."""
    return "<div class='container'><p>Hello World</p></div>"


@pytest.fixture
def sample_component_data():
    """Provide sample component data for testing."""
    return {
        "title": "Test Component",
        "body": "Test content",
        "variant": "primary",
        "size": "md",
    }
