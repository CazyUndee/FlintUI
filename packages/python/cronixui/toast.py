"""Toast notification component."""

from enum import Enum
from typing import Optional


class ToastType(Enum):
    SUCCESS = "success"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


class Toast:
    """Toast notification component."""

    def __init__(self, element=None):
        self._element = element
        self._title: Optional[str] = None
        self._message: str = ""
        self._type: ToastType = ToastType.INFO
        self._duration: int = 4000

    @staticmethod
    def show(
        title: Optional[str] = None,
        message: str = "",
        type: str = "info",
        duration: int = 4000,
    ) -> "Toast":
        """Show a toast notification."""
        toast = Toast()
        toast._title = title
        toast._message = message
        toast._type = ToastType(type)
        toast._duration = duration
        return toast

    @staticmethod
    def success(message: str, title: Optional[str] = None) -> "Toast":
        """Show a success toast."""
        return Toast.show(title=title, message=message, type="success")

    @staticmethod
    def error(message: str, title: Optional[str] = None) -> "Toast":
        """Show an error toast."""
        return Toast.show(title=title, message=message, type="error")

    @staticmethod
    def warning(message: str, title: Optional[str] = None) -> "Toast":
        """Show a warning toast."""
        return Toast.show(title=title, message=message, type="warning")

    @staticmethod
    def info(message: str, title: Optional[str] = None) -> "Toast":
        """Show an info toast."""
        return Toast.show(title=title, message=message, type="info")

    @property
    def title(self) -> Optional[str]:
        return self._title

    @property
    def message(self) -> str:
        return self._message

    @property
    def type(self) -> ToastType:
        return self._type

    @property
    def duration(self) -> int:
        return self._duration
