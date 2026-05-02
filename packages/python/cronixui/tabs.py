"""Tabs component."""


from typing import Union

class Tabs:
    """Tabs component."""

    def __init__(self, element: Union[str, None] = None) -> None:
        """Initialize tabs on element."""
        self._element = element
        self._active_index: int = 0

    def set_active(self, index: int) -> None:
        """Set active tab by index."""
        self._active_index = index

    def active_index(self) -> int:
        """Get active tab index."""
        return self._active_index
