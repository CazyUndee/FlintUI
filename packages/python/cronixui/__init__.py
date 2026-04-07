"""
CronixUI - A dark-themed UI toolkit with crimson accents and Outfit typography
"""

from .toast import Toast
from .toggle import Toggle
from .modal import Modal
from .dropdown import Dropdown
from .tabs import Tabs
from .accordion import Accordion
from .pagination import Pagination
from .command_palette import CommandPalette, CommandPaletteItem
from .search import Search, SearchItem
from .nav import Nav
from .core import init, query, query_all, create_el

__version__ = "1.0.4"
__all__ = [
    "Toast",
    "Toggle",
    "Modal",
    "Dropdown",
    "Tabs",
    "Accordion",
    "Pagination",
    "CommandPalette",
    "CommandPaletteItem",
    "Search",
    "SearchItem",
    "Nav",
    "init",
    "query",
    "query_all",
    "create_el",
]
