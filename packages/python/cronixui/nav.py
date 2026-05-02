"""Navigation component."""

from typing import Union


class Nav:
    """Navigation component."""

    _instances: list["Nav"] = []

    def __init__(self, element: Union[str, None] = None) -> None:
        """Initialize navigation on element."""
        self._element = element
        self._active: str = ""
        Nav._instances.append(self)

    def set_active(self, item: str) -> None:
        """Set active navigation item."""
        self._active = item

    def get_active(self) -> str:
        """Get active navigation item."""
        return self._active

    @classmethod
    def init(cls) -> None:
        """Initialize all navigation components."""
        pass

    @classmethod
    def get_all(cls) -> list:
        """Get all navigation instances."""
        return cls._instances
