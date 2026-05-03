"""Modal dialog component."""

from typing import Union


class Modal:
    """Modal dialog component."""

    def __init__(self, element: Union[str, None] = None) -> None:
        """Initialize modal on element."""
        self._element = element
        self._open: bool = False

    def open(self) -> None:
        """Open the modal."""
        self._open = True

    def close(self) -> None:
        """Close the modal."""
        self._open = False

    def is_open(self) -> bool:
        """Check if modal is open."""
        return self._open
