"""CronixUI Badge & Tag Components.

Generates HTML for status badges and removable tags.
No browser DOM APIs are used - all output is HTML strings or data structures.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class BadgeElement:
    """Represents a rendered badge or tag element."""

    tag: str = "span"
    classes: list[str] = field(default_factory=list)
    attributes: dict[str, str] = field(default_factory=dict)
    inner_html: str = ""

    def render_html(self) -> str:
        """Render as HTML string.

        Returns:
            Complete HTML for the badge element
        """
        class_str = " ".join(self.classes)
        class_attr = f' class="{class_str}"' if class_str else ""
        attrs_str = "".join(f' {k}="{v}"' for k, v in self.attributes.items())
        return f"<{self.tag}{class_attr}{attrs_str}>{self.inner_html}</{self.tag}>"

    def render(self) -> BadgeElement:
        """Return self for API compatibility."""
        return self


class Badge:
    """Badge component for status indicators and labels.

    Args:
        text: Badge text content
        variant: Badge variant - default, accent, success, warning, error, info (default: default)
        solid: Whether to use solid styling (default: False)

    Example:
        >>> badge = Badge("Active", variant="success")
        >>> print(badge.render_html())
        <span class="cn-badge cn-badge-success">Active</span>

        >>> solid_badge = Badge("New", variant="accent", solid=True)
        >>> print(solid_badge.render_html())
        <span class="cn-badge cn-badge-accent cn-badge-solid">New</span>
    """

    VARIANTS = ("default", "accent", "success", "warning", "error", "info")

    def __init__(
        self,
        text: str,
        variant: str = "default",
        solid: bool = False,
    ):
        if not text:
            raise ValueError("text cannot be empty")
        if variant not in self.VARIANTS:
            raise ValueError(
                f"Invalid variant '{variant}'. Must be one of {self.VARIANTS}"
            )

        self.text = text
        self.variant = variant
        self.solid = solid

    def render(self) -> BadgeElement:
        """Render the badge as a BadgeElement data structure.

        Returns:
            BadgeElement representing the badge
        """
        classes = ["cn-badge", f"cn-badge-{self.variant}"]
        if self.solid:
            classes.append("cn-badge-solid")

        return BadgeElement(
            classes=classes,
            inner_html=self._esc(self.text),
        )

    def render_html(self) -> str:
        """Render the badge as an HTML string.

        Returns:
            HTML string representation of the badge
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


class Tag:
    """Tag component for labels with optional removal.

    Args:
        text: Tag text content
        removable: Whether to show a remove button (default: False)
        on_remove: Callback name for removal (stored as data attribute)

    Example:
        >>> tag = Tag("Python")
        >>> print(tag.render_html())
        <span class="cn-tag">Python</span>

        >>> removable = Tag("JavaScript", removable=True, on_remove="handleRemove")
        >>> print(removable.render_html())
        <span class="cn-tag" data-on-remove="handleRemove">
            JavaScript<span class="cn-tag-remove">...</span>
        </span>
    """

    _REMOVE_ICON = (
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor">'
        '<path d="M18 6L6 18M6 6l12 12"/>'
        '</svg>'
    )

    def __init__(
        self,
        text: str,
        removable: bool = False,
        on_remove: str | None = None,
    ):
        if not text:
            raise ValueError("text cannot be empty")

        self.text = text
        self.removable = removable
        self.on_remove = on_remove

    def render(self) -> BadgeElement:
        """Render the tag as a BadgeElement data structure.

        Returns:
            BadgeElement representing the tag
        """
        attrs: dict[str, str] = {}
        if self.removable and self.on_remove:
            attrs["data-on-remove"] = self.on_remove

        inner_parts = [self._esc(self.text)]

        if self.removable:
            inner_parts.append(
                f'<span class="cn-tag-remove">{self._REMOVE_ICON}</span>'
            )

        return BadgeElement(
            classes=["cn-tag"],
            attributes=attrs,
            inner_html="".join(inner_parts),
        )

    def render_html(self) -> str:
        """Render the tag as an HTML string.

        Returns:
            HTML string representation of the tag
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
