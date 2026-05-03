"""Command palette component."""

from dataclasses import dataclass
from typing import Callable, List, Optional, Union


@dataclass
class CommandPaletteItem:
    """Command palette item."""

    title: str
    kbd: Optional[str] = None
    action: Optional[Callable] = None


class CommandPalette:
    """Command palette component."""

    def __init__(self, element: Union[str, None] = None) -> None:
        """Initialize command palette on element."""
        self._element = element
        self._items: List[CommandPaletteItem] = []
        self._open: bool = False

    def open(self) -> None:
        """Open command palette."""
        self._open = True

    def close(self) -> None:
        """Close command palette."""
        self._open = False

    def toggle(self) -> None:
        """Toggle command palette."""
        self._open = not self._open

    def is_open(self) -> bool:
        """Check if command palette is open."""
        return self._open

    def set_items(self, items: List[CommandPaletteItem]) -> None:
        """Set command items."""
        self._items = items

    def get_items(self) -> List[CommandPaletteItem]:
        """Get all items."""
        return self._items

    def execute(self, index: int) -> None:
        """Execute item by index."""
        if 0 <= index < len(self._items) and self._items[index].action is not None:
            self._items[index].action()  # type: ignore
            self.close()
