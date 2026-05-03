"""CronixUI Alert Component.

Generates HTML for alert banners with icon, title, message, and optional dismiss button.
No browser DOM APIs are used - all output is HTML strings or data structures.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class AlertElement:
    """Represents a rendered alert element."""

    tag: str = "div"
    classes: list[str] = field(default_factory=list)
    attributes: dict[str, str] = field(default_factory=dict)
    inner_html: str = ""

    def render_html(self) -> str:
        """Render the alert as HTML string.

        Returns:
            Complete HTML for the alert including icon, content, and optional close button
        """
        class_str = " ".join(self.classes)
        class_attr = f' class="{class_str}"' if class_str else ""
        attrs_str = "".join(f' {k}="{v}"' for k, v in self.attributes.items())
        return f"<{self.tag}{class_attr}{attrs_str}>{self.inner_html}</{self.tag}>"

    def render(self) -> AlertElement:
        """Return self for API compatibility."""
        return self


class Alert:
    """Alert component for displaying informational, success, warning, or error messages.

    Args:
        message: The alert message text
        title: Optional alert title
        variant: Alert variant - info, success, warning, error (default: info)
        dismissible: Whether to show a close button (default: False)

    Example:
        >>> alert = Alert("Your changes were saved.", title="Success", variant="success")
        >>> print(alert.render_html())
        <div class="cn-alert cn-alert-success">...</div>

        >>> dismissible = Alert("Dismiss me", dismissible=True)
        >>> print(dismissible.render_html())
        <div class="cn-alert cn-alert-info" data-dismissible="true">...</div>
    """

    VARIANTS = ("info", "success", "warning", "error")

    _ICONS = {
        "info": (
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor">'
            '<circle cx="12" cy="12" r="10"/>'
            '<path d="M12 16v-4M12 8h.01"/>'
            "</svg>"
        ),
        "success": (
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor">'
            '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>'
            '<polyline points="22 4 12 14.01 9 11.01"/>'
            "</svg>"
        ),
        "warning": (
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor">'
            '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94'
            'a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>'
            '<line x1="12" y1="9" x2="12" y2="13"/>'
            '<line x1="12" y1="17" x2="12.01" y2="17"/>'
            "</svg>"
        ),
        "error": (
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor">'
            '<circle cx="12" cy="12" r="10"/>'
            '<line x1="15" y1="9" x2="9" y2="15"/>'
            '<line x1="9" y1="9" x2="15" y2="15"/>'
            "</svg>"
        ),
    }

    def __init__(
        self,
        message: str,
        title: str | None = None,
        variant: str = "info",
        dismissible: bool = False,
    ):
        if variant not in self.VARIANTS:
            raise ValueError(f"Invalid variant '{variant}'. Must be one of {self.VARIANTS}")
        if not message:
            raise ValueError("message cannot be empty")

        self.message = message
        self.title = title
        self.variant = variant
        self.dismissible = dismissible

    def render(self) -> AlertElement:
        """Render the alert as an AlertElement data structure.

        Returns:
            AlertElement representing the complete alert banner
        """
        icon_svg = self._ICONS.get(self.variant, "")

        parts = []

        # Icon
        if icon_svg:
            parts.append(f'<span class="cn-alert-icon">{icon_svg}</span>')

        # Content area
        content_parts = []
        if self.title:
            content_parts.append(f'<div class="cn-alert-title">{self._esc(self.title)}</div>')
        content_parts.append(f'<div class="cn-alert-message">{self._esc(self.message)}</div>')
        parts.append(f'<div class="cn-alert-content">{"".join(content_parts)}</div>')

        # Dismiss button
        if self.dismissible:
            parts.append('<button class="cn-alert-close" data-dismiss="alert">&times;</button>')

        inner = "".join(parts)

        return AlertElement(
            classes=["cn-alert", f"cn-alert-{self.variant}"],
            attributes={"data-dismissible": "true"} if self.dismissible else {},
            inner_html=inner,
        )

    def render_html(self) -> str:
        """Render the alert as an HTML string.

        Returns:
            Complete HTML string for the alert
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
