"""Pagination component."""

from typing import Callable, Optional


class Pagination:
    """Pagination component."""

    def __init__(
        self,
        element=None,
        total: int = 1,
        current: int = 1,
        on_change: Optional[Callable[[int], None]] = None,
    ):
        """Initialize pagination.

        Args:
            element: Target element
            total: Total number of pages
            current: Current page (default: 1)
            on_change: Callback when page changes
        """
        self._element = element
        self._total = total
        self._current = current
        self._on_change = on_change

    def go_to(self, page: int) -> None:
        """Go to specific page."""
        if 1 <= page <= self._total:
            self._current = page
            if self._on_change:
                self._on_change(page)

    def next(self) -> None:
        """Go to next page."""
        if self._current < self._total:
            self.go_to(self._current + 1)

    def prev(self) -> None:
        """Go to previous page."""
        if self._current > 1:
            self.go_to(self._current - 1)

    @property
    def current(self) -> int:
        """Get current page."""
        return self._current

    @property
    def total(self) -> int:
        """Get total pages."""
        return self._total

    def render(self) -> None:
        """Re-render pagination."""
        pass
