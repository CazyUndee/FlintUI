"""Toggle switch component."""

from typing import Union


class Toggle:
    """Toggle switch component."""

    def __init__(self, element: Union[str, None] = None) -> None:
        """Initialize toggle on element."""
        self._element = element
        self._on: bool = False

    def toggle(self) -> None:
        """Toggle the state."""
        self._on = not self._on

    def is_on(self) -> bool:
        """Check if toggle is on."""
        return self._on

    def set_on(self, value: bool) -> None:
        """Set toggle state."""
        self._on = value
