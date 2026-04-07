"""Core CronixUI functions."""

from typing import Dict, Optional, List, Any


def init() -> None:
    """Initialize all CronixUI components."""
    pass


def query(selector: str) -> Optional[Any]:
    """Query single element.

    Args:
        selector: CSS selector

    Returns:
        Element or None
    """
    pass


def query_all(selector: str) -> List[Any]:
    """Query all matching elements.

    Args:
        selector: CSS selector

    Returns:
        List of elements
    """
    return []


def create_el(
    tag: str, class_name: Optional[str] = None, attrs: Optional[Dict[str, str]] = None
) -> Any:
    """Create an element.

    Args:
        tag: HTML tag name
        class_name: Optional CSS class name
        attrs: Optional attributes dict

    Returns:
        Created element
    """
    pass
