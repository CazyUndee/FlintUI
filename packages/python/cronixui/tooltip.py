"""CronixUI Tooltip Component.

Generates HTML for tooltips that can wrap other elements.
No browser DOM APIs are used - all output is HTML strings or data structures.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TooltipElement:
    """Represents a rendered tooltip element."""

    tag: str = "div"
    classes: list[str] = field(default_factory=list)
    attributes: dict[str, str] = field(default_factory=dict)
    inner_html: str = ""

    def render_html(self) -> str:
        """Render as HTML string.

        Returns:
            Complete HTML for the tooltip element
        """
        class_str = " ".join(self.classes)
        class_attr = f' class="{class_str}"' if class_str else ""
        attrs_str = "".join(f' {k}="{v}"' for k, v in self.attributes.items())
        return f"<{self.tag}{class_attr}{attrs_str}>{self.inner_html}</{self.tag}>"

    def render(self) -> TooltipElement:
        """Return self for API compatibility."""
        return self


class Tooltip:
    """Tooltip component for displaying contextual information on hover.

    The tooltip content is generated as a data attribute and HTML structure
    that can be styled with CSS to appear on hover.

    Args:
        content: Tooltip text content
        position: Tooltip position - top, bottom, left, right (default: top)

    Example:
        >>> tooltip = Tooltip("Click to edit", position="top")
        >>> print(tooltip.render_html())
        <div class="cn-tooltip cn-tooltip-top">
            <div class="cn-tooltip-content">Click to edit</div>
        </div>

        >>> # Wrap an element with tooltip
        >>> wrapped = tooltip.wrap_html("<button>Edit</button>")
        >>> print(wrapped)
        <span class="cn-tooltip-wrapper" data-tooltip="Click to edit" data-position="top">
            <button>Edit</button>
        </span>
    """

    POSITIONS = ("top", "bottom", "left", "right")

    def __init__(self, content: str, position: str = "top"):
        if not content:
            raise ValueError("content cannot be empty")
        if position not in self.POSITIONS:
            raise ValueError(f"Invalid position '{position}'. Must be one of {self.POSITIONS}")

        self.content = content
        self.position = position

    def render(self) -> TooltipElement:
        """Render the tooltip as a TooltipElement.

        Returns:
            TooltipElement representing the tooltip
        """
        inner = f'<div class="cn-tooltip-content">{self._esc(self.content)}</div>'

        return TooltipElement(
            classes=["cn-tooltip", f"cn-tooltip-{self.position}"],
            inner_html=inner,
        )

    def render_html(self) -> str:
        """Render the tooltip as an HTML string.

        Returns:
            HTML string representation of the tooltip
        """
        return self.render().render_html()

    def wrap_html(self, element_html: str) -> str:
        """Wrap an HTML element with tooltip data attributes.

        This generates a wrapper with data attributes that CSS can use
        to display the tooltip on hover.

        Args:
            element_html: HTML string of the element to wrap

        Returns:
            HTML string with the element wrapped in a tooltip wrapper

        Example:
            >>> tooltip = Tooltip("Click to save")
            >>> wrapped = tooltip.wrap_html("<button>Save</button>")
            >>> print(wrapped)
            <span class="cn-tooltip-wrapper" data-tooltip="Click to save" data-position="top">
                <button>Save</button>
            </span>
        """
        return (
            f'<span class="cn-tooltip-wrapper"'
            f' data-tooltip="{self._esc(self.content)}"'
            f' data-position="{self.position}">'
            f"{element_html}"
            f"</span>"
        )

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
