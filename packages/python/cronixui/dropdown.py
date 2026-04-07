"""Dropdown menu component."""


class Dropdown:
    """Dropdown menu component."""

    def __init__(self, element=None):
        """Initialize dropdown on element."""
        self._element = element
        self._open: bool = False

    def open(self) -> None:
        """Open the dropdown."""
        self._open = True

    def close(self) -> None:
        """Close the dropdown."""
        self._open = False

    def toggle(self) -> None:
        """Toggle the dropdown."""
        self._open = not self._open

    def is_open(self) -> bool:
        """Check if dropdown is open."""
        return self._open
