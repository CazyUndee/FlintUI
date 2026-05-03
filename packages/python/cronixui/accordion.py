"""Accordion component."""

from typing import List, Union


class Accordion:
    """Accordion component."""

    def __init__(self, element: Union[str, None] = None) -> None:
        """Initialize accordion on element."""
        self._element = element
        self._open_indices: List[int] = []

    def toggle(self, index: int) -> None:
        """Toggle accordion item by index."""
        if index in self._open_indices:
            self._open_indices.remove(index)
        else:
            self._open_indices.append(index)

    def open_all(self, total: int) -> None:
        """Open all accordion items."""
        self._open_indices = list(range(total))

    def close_all(self) -> None:
        """Close all accordion items."""
        self._open_indices.clear()

    def is_open(self, index: int) -> bool:
        """Check if item is open."""
        return index in self._open_indices
