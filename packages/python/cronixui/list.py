"""CronixUI List Component.

Generates HTML for lists with optional icons, titles, subtitles, and actions.
No browser DOM APIs are used - all output is HTML strings or data structures.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ListElement:
    """Represents a rendered list element."""

    tag: str = "div"
    classes: list[str] = field(default_factory=list)
    attributes: dict[str, str] = field(default_factory=dict)
    inner_html: str = ""

    def render_html(self) -> str:
        """Render as HTML string.

        Returns:
            Complete HTML for the list element
        """
        class_str = " ".join(self.classes)
        class_attr = f' class="{class_str}"' if class_str else ""
        attrs_str = "".join(f' {k}="{v}"' for k, v in self.attributes.items())
        return f"<{self.tag}{class_attr}{attrs_str}>{self.inner_html}</{self.tag}>"

    def render(self) -> ListElement:
        """Return self for API compatibility."""
        return self


class CronixList:
    """List component for displaying collections of items.

    Items can be simple strings or dictionaries with optional keys:
        - icon: SVG markup for the item icon
        - title: Primary text for the item
        - subtitle: Secondary/description text
        - actions: HTML string for action buttons/links

    Args:
        items: List of items (strings or dicts)
        clickable: Whether items should appear clickable (default: False)

    Example:
        >>> simple = List(["Item 1", "Item 2", "Item 3"])
        >>> print(simple.render_html())
        <div class="cn-list">
            <div class="cn-list-item"><div class="cn-list-item-content">Item 1</div></div>
            <div class="cn-list-item"><div class="cn-list-item-content">Item 2</div></div>
            <div class="cn-list-item"><div class="cn-list-item-content">Item 3</div></div>
        </div>

        >>> rich = List([
        ...     {
        ...         "icon": "<svg>...</svg>",
        ...         "title": "Dashboard",
        ...         "subtitle": "Main overview",
        ...         "actions": "<button>Edit</button>",
        ...     },
        ...     {"title": "Settings", "subtitle": "App configuration"},
        ... ], clickable=True)
        >>> print(rich.render_html())
    """

    def __init__(self, items: list[Any], clickable: bool = False):
        if not items:
            raise ValueError("items cannot be empty")

        self.items = items
        self.clickable = clickable

    def render(self) -> ListElement:
        """Render the list as a ListElement.

        Returns:
            ListElement containing all list items
        """
        item_parts = []
        for item in self.items:
            item_classes = ["cn-list-item"]
            if self.clickable:
                item_classes.append("cn-list-item-clickable")

            if isinstance(item, dict):
                item_parts.append(self._render_dict_item(item, item_classes))
            else:
                content = self._esc(str(item))
                item_parts.append(
                    f'<div class="{" ".join(item_classes)}">'
                    f'<div class="cn-list-item-content">{content}</div>'
                    f"</div>"
                )

        return ListElement(
            classes=["cn-list"],
            inner_html="".join(item_parts),
        )

    def _render_dict_item(self, item: dict, item_classes: list[str]) -> str:
        """Render a single dict-based list item."""
        class_str = " ".join(item_classes)
        parts = [f'<div class="{class_str}">']

        # Icon
        if icon := item.get("icon"):
            parts.append(f'<span class="cn-list-item-icon">{icon}</span>')

        # Content
        content_parts = []
        if title := item.get("title"):
            content_parts.append(f'<div class="cn-list-item-title">{self._esc(title)}</div>')
        if subtitle := item.get("subtitle"):
            content_parts.append(f'<div class="cn-list-item-subtitle">{self._esc(subtitle)}</div>')
        if content_parts:
            parts.append(f'<div class="cn-list-item-content">{"".join(content_parts)}</div>')

        # Actions
        if actions := item.get("actions"):
            parts.append(f'<div class="cn-list-item-actions">{actions}</div>')

        parts.append("</div>")
        return "".join(parts)

    def render_html(self) -> str:
        """Render the list as an HTML string.

        Returns:
            HTML string representation of the list
        """
        return self.render().render_html()

    @staticmethod
    def _esc(text: str) -> str:
        """Escape HTML special characters."""
        return (
            text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#x27;")
        )


# Backward compatibility alias - allows `from cronixui.list import List`
List = CronixList
