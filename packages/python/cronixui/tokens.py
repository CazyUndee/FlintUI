"""
CronixUI Design Tokens
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Color:
    """Color token."""

    hex: str
    rgb: Tuple[int, int, int]


# Background colors
BG = Color("#0a0a0a", (10, 10, 10))
SURFACE = Color("#111111", (17, 17, 17))
SURFACE_2 = Color("#1a1a1a", (26, 26, 26))
SURFACE_3 = Color("#222222", (34, 34, 34))
SURFACE_4 = Color("#2a2a2a", (42, 42, 42))

# Text colors
TEXT = Color("#f0ede8", (240, 237, 232))
TEXT_MUTED = "rgba(240, 237, 232, 0.5)"
TEXT_DIM = "rgba(240, 237, 232, 0.25)"

# Accent (Crimson)
ACCENT = Color("#6b2323", (107, 35, 35))
ACCENT_HOVER = Color("#7d2a2a", (125, 42, 42))
ACCENT_LIGHT = Color("#8a3535", (138, 53, 53))
ACCENT_GLOW = "rgba(107, 35, 35, 0.3)"
ACCENT_TEXT = Color("#c97a7a", (201, 122, 122))

# Semantic colors
SUCCESS = Color("#1e5028", (30, 80, 40))
SUCCESS_BORDER = "rgba(60, 140, 70, 0.4)"
SUCCESS_TEXT = Color("#6bc47a", (107, 196, 122))

WARNING = Color("#503c14", (80, 60, 20))
WARNING_BORDER = "rgba(150, 110, 30, 0.4)"
WARNING_TEXT = Color("#c4a43a", (196, 164, 58))

ERROR = Color("#501414", (80, 20, 20))
ERROR_BORDER = "rgba(180, 60, 60, 0.4)"
ERROR_TEXT = Color("#c46b6b", (196, 107, 107))

INFO = Color("#143550", (20, 53, 80))
INFO_BORDER = "rgba(60, 140, 200, 0.4)"
INFO_TEXT = Color("#6ba8c4", (107, 168, 196))

# Border
BORDER = "rgba(255, 255, 255, 0.08)"
BORDER_HOVER = "rgba(255, 255, 255, 0.15)"
BORDER_FOCUS = "rgba(255, 255, 255, 0.25)"


@dataclass(frozen=True)
class Typography:
    """Typography tokens."""

    font_family: str = "'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    font_mono: str = "'JetBrains Mono', 'Fira Code', 'Consolas', monospace"

    # Font sizes
    xs: int = 11
    sm: int = 12
    base: int = 13
    md: int = 14
    lg: int = 16
    xl: int = 20
    xxl: int = 28
    xxxl: int = 36


@dataclass(frozen=True)
class Spacing:
    """Spacing tokens."""

    space_1: int = 4
    space_2: int = 8
    space_3: int = 12
    space_4: int = 16
    space_5: int = 20
    space_6: int = 24
    space_8: int = 32
    space_10: int = 40
    space_12: int = 48


@dataclass(frozen=True)
class Radius:
    """Border radius tokens."""

    sm: int = 6
    default: int = 10
    lg: int = 14
    xl: int = 20
    full: int = 9999


@dataclass(frozen=True)
class Shadow:
    """Shadow tokens."""

    sm: str = "0 1px 2px rgba(0, 0, 0, 0.3)"
    default: str = "0 4px 12px rgba(0, 0, 0, 0.4)"
    lg: str = "0 8px 24px rgba(0, 0, 0, 0.5)"
    glow: str = "0 0 20px rgba(107, 35, 35, 0.3)"


@dataclass(frozen=True)
class Transition:
    """Transition tokens."""

    fast: str = "0.1s ease"
    default: str = "0.15s ease"
    slow: str = "0.25s ease"


@dataclass(frozen=True)
class ZIndex:
    """Z-index tokens."""

    dropdown: int = 100
    sticky: int = 200
    fixed: int = 300
    modal_backdrop: int = 400
    modal: int = 500
    popover: int = 600
    tooltip: int = 700
    toast: int = 800


@dataclass(frozen=True)
class Layout:
    """Layout tokens."""

    container_max: int = 1200
    sidebar_width: int = 260


# Token instances
typography = Typography()
spacing = Spacing()
radius = Radius()
shadow = Shadow()
transition = Transition()
z_index = ZIndex()
layout = Layout()


__all__ = [
    "Color",
    "BG",
    "SURFACE",
    "SURFACE_2",
    "SURFACE_3",
    "SURFACE_4",
    "TEXT",
    "TEXT_MUTED",
    "TEXT_DIM",
    "ACCENT",
    "ACCENT_HOVER",
    "ACCENT_LIGHT",
    "ACCENT_GLOW",
    "ACCENT_TEXT",
    "SUCCESS",
    "SUCCESS_BORDER",
    "SUCCESS_TEXT",
    "WARNING",
    "WARNING_BORDER",
    "WARNING_TEXT",
    "ERROR",
    "ERROR_BORDER",
    "ERROR_TEXT",
    "INFO",
    "INFO_BORDER",
    "INFO_TEXT",
    "BORDER",
    "BORDER_HOVER",
    "BORDER_FOCUS",
    "Typography",
    "typography",
    "Spacing",
    "spacing",
    "Radius",
    "radius",
    "Shadow",
    "shadow",
    "Transition",
    "transition",
    "ZIndex",
    "z_index",
    "Layout",
    "layout",
]
