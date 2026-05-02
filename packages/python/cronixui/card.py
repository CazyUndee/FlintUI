"""CronixUI Card Component.

Generates HTML for cards with header, body, footer, and optional icon variants.
No browser DOM APIs are used - all output is HTML strings or data structures.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class CardElement:
    """Represents a rendered card element."""

    tag: str = "div"
    classes: list[str] = field(default_factory=list)
    attributes: dict[str, str] = field(default_factory=dict)
    inner_html: str = ""

    def render_html(self) -> str:
        """Render the card as HTML string.

        Returns:
            Complete HTML for the card element
        """
        class_str = " ".join(self.classes)
        class_attr = f' class="{class_str}"' if class_str else ""
        attrs_str = "".join(f' {k}="{v}"' for k, v in self.attributes.items())
        return f"<{self.tag}{class_attr}{attrs_str}>{self.inner_html}</{self.tag}>"

    def render(self) -> CardElement:
        """Return self for API compatibility."""
        return self


class Card:
    """Card container component with optional header, body, and footer sections.

    Args:
        title: Optional card title
        subtitle: Optional card subtitle
        clickable: Whether card should appear clickable (default: False)
        body: Optional card body content (HTML string)
        footer: Optional card footer content (HTML string)

    Example:
        >>> card = Card(
        ...     title="Welcome",
        ...     subtitle="Getting started guide",
        ...     body="<p>Card body content here.</p>",
        ...     footer="<a href='#'>Learn more</a>",
        ... )
        >>> print(card.render_html())
        <div class="cn-card">
            <div class="cn-card-header">
                <h3 class="cn-card-title">Welcome</h3>
                <p class="cn-card-subtitle">Getting started guide</p>
            </div>
            <div class="cn-card-body"><p>Card body content here.</p></div>
            <div class="cn-card-footer"><a href='#'>Learn more</a></div>
        </div>
    """

    def __init__(
        self,
        title: str | None = None,
        subtitle: str | None = None,
        clickable: bool = False,
        body: str | None = None,
        footer: str | None = None,
    ):
        self.title = title
        self.subtitle = subtitle
        self.clickable = clickable
        self._body = body
        self._footer = footer

    def render(self) -> CardElement:
        """Render the card as a CardElement data structure.

        Returns:
            CardElement representing the complete card
        """
        classes = ["cn-card"]
        if self.clickable:
            classes.append("cn-card-clickable")

        parts = []

        # Header
        if self.title or self.subtitle:
            header_parts = []
            if self.title:
                header_parts.append(f'<h3 class="cn-card-title">{self._esc(self.title)}</h3>')
            if self.subtitle:
                header_parts.append(f'<p class="cn-card-subtitle">{self._esc(self.subtitle)}</p>')
            parts.append(f'<div class="cn-card-header">{"".join(header_parts)}</div>')

        # Body
        if self._body is not None:
            parts.append(f'<div class="cn-card-body">{self._body}</div>')

        # Footer
        if self._footer is not None:
            parts.append(f'<div class="cn-card-footer">{self._footer}</div>')

        return CardElement(
            classes=classes,
            inner_html="".join(parts),
        )

    def render_html(self) -> str:
        """Render the card as an HTML string.

        Returns:
            HTML string representation of the card
        """
        return self.render().render_html()

    def with_body(self, content: str) -> Card:
        """Set the card body content and return self for chaining.

        Args:
            content: HTML string for the card body

        Returns:
            Self for method chaining

        Example:
            >>> card = Card(title="Title").with_body("<p>Body content</p>")
        """
        self._body = content
        return self

    def with_footer(self, content: str) -> Card:
        """Set the card footer content and return self for chaining.

        Args:
            content: HTML string for the card footer

        Returns:
            Self for method chaining

        Example:
            >>> card = Card(title="Title").with_footer("<a href='#'>Link</a>")
        """
        self._footer = content
        return self

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


class CardIcon:
    """Card variant with an icon display.

    Args:
        icon_svg: SVG markup string for the icon
        title: Optional card title
        subtitle: Optional card subtitle

    Example:
        >>> icon_card = CardIcon(
        ...     icon_svg='<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/></svg>',
        ...     title="Settings",
        ... )
        >>> print(icon_card.render_html())
    """

    def __init__(
        self,
        icon_svg: str,
        title: str | None = None,
        subtitle: str | None = None,
    ):
        if not icon_svg:
            raise ValueError("icon_svg cannot be empty")
        self.icon_svg = icon_svg
        self.title = title
        self.subtitle = subtitle

    def render(self) -> CardElement:
        """Render the icon card as a CardElement.

        Returns:
            CardElement representing the icon card
        """
        classes = ["cn-card", "cn-card-icon"]

        parts = [f'<div class="cn-card-icon-inner">{self.icon_svg}</div>']

        if self.title:
            parts.append(f'<h3 class="cn-card-title">{self._esc(self.title)}</h3>')
        if self.subtitle:
            parts.append(f'<p class="cn-card-subtitle">{self._esc(self.subtitle)}</p>')

        return CardElement(
            classes=classes,
            inner_html="".join(parts),
        )

    def render_html(self) -> str:
        """Render the icon card as an HTML string.

        Returns:
            HTML string representation of the icon card
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
