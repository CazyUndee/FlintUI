"""Search component."""

from dataclasses import dataclass
from typing import Callable, List, Optional, Union


@dataclass
class SearchItem:
    """Search result item."""

    title: str
    subtitle: Optional[str] = None
    action: Optional[Callable] = None


class Search:
    """Search component."""

    def __init__(self, element: Union[str, None] = None) -> None:
        """Initialize search on element."""
        self._element = element
        self._items: List[SearchItem] = []
        self._open: bool = False

    def set_items(self, items: List[SearchItem]) -> None:
        """Set searchable items."""
        self._items = items

    def filter(self, query: str) -> List[SearchItem]:
        """Filter items by query."""
        query_lower = query.lower()
        return [item for item in self._items if query_lower in item.title.lower()]

    def open(self) -> None:
        """Open search results."""
        self._open = True

    def close(self) -> None:
        """Close search results."""
        self._open = False

    def is_open(self) -> bool:
        """Check if search is open."""
        return self._open

    def select(self, index: int) -> None:
        """Select and execute item by index."""
        if 0 <= index < len(self._items) and self._items[index].action is not None:
            self._items[index].action()  # type: ignore
            self.close()
