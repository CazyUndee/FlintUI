"""CronixUI Breadcrumb Component.

Generates HTML for breadcrumb navigation.
No browser DOM APIs are used - all output is HTML strings or data structures.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class BreadcrumbElement:
    """Represents a rendered breadcrumb element."""

    tag: str = "nav"
    classes: list[str] = field(default_factory=list)
    attributes: dict[str, str] = field(default_factory=dict)
    inner_html: str = ""

    def render_html(self) -> str:
        """Render as HTML string.

        Returns:
            Complete HTML for the breadcrumb element
        """
        class_str = " ".join(self.classes)
        class_attr = f' class="{class_str}"' if class_str else ""
        attrs_str = "".join(f' {k}="{v}"' for k, v in self.attributes.items())
        return f"<{self.tag}{class_attr}{attrs_str}>{self.inner_html}</{self.tag}>"

    def render(self) -> BreadcrumbElement:
        """Return self for API compatibility."""
        return self


@dataclass
class BreadcrumbItem:
    """A breadcrumb item.

    Attributes:
        label: Display text
        href: Link URL (default: "#")
        active: Whether this is the current/active item (last item by default)
    """

    label: str
    href: str = "#"
    active: bool = False


class Breadcrumb:
    """Breadcrumb navigation component.

    Args:
        items: List of BreadcrumbItem instances
        separator: Separator between items (default: "/")

    Example:
        >>> breadcrumb = Breadcrumb(
        ...     items=[
        ...         BreadcrumbItem(label="Home", href="/"),
        ...         BreadcrumbItem(label="Details", active=True),
        ...     ],
        ... )
        >>> breadcrumb.render_html()
        '<nav class="cn-breadcrumb" aria-label="Breadcrumb"><a class="cn-breadcrumb-item" href="/">Home</a><span class="cn-breadcrumb-separator" aria-hidden="true">/</span><span class="cn-breadcrumb-current" aria-current="page">Details</span></nav>'
    """

    def __init__(
        self,
        items: list[BreadcrumbItem] | None = None,
        separator: str = "/",
    ):
        self.items = items or []
        self.separator = separator

    def render(self) -> BreadcrumbElement:
        """Render the breadcrumb as a BreadcrumbElement.

        Returns:
            BreadcrumbElement representing the breadcrumb
        """
        parts = []

        # Determine which item should be marked as current
        # Priority: explicit active item if present, otherwise the last item
        current_index: int | None = None
        for i, item in enumerate(self.items):
            if item.active:
                current_index = i
                break
        if current_index is None and self.items:
            current_index = len(self.items) - 1

        for i, item in enumerate(self.items):
            if i > 0:
                parts.append(
                    f'<span class="cn-breadcrumb-separator" aria-hidden="true">'
                    f"{self._esc(self.separator)}</span>"
                )

            if i == current_index:
                parts.append(
                    f'<span class="cn-breadcrumb-current" aria-current="page">'
                    f"{self._esc(item.label)}</span>"
                )
            else:
                parts.append(
                    f'<a class="cn-breadcrumb-item" href="{self._esc(item.href)}">'
                    f"{self._esc(item.label)}</a>"
                )

        return BreadcrumbElement(
            classes=["cn-breadcrumb"],
            attributes={"aria-label": "Breadcrumb"},
            inner_html="".join(parts),
        )

    def render_html(self) -> str:
        """Render the breadcrumb as an HTML string.

        Returns:
            HTML string representation of the breadcrumb
        """
        return self.render().render_html()

    @staticmethod
    def _esc(text: str) -> str:
        return (
            text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#x27;")
        )
