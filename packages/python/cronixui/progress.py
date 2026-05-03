"""CronixUI Progress Components.

Generates HTML for progress bars and stat/metric displays.
No browser DOM APIs are used - all output is HTML strings or data structures.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ProgressElement:
    """Represents a rendered progress/stat element."""

    tag: str = "div"
    classes: list[str] = field(default_factory=list)
    attributes: dict[str, str] = field(default_factory=dict)
    inner_html: str = ""

    def render_html(self) -> str:
        """Render as HTML string.

        Returns:
            Complete HTML for the element
        """
        class_str = " ".join(self.classes)
        class_attr = f' class="{class_str}"' if class_str else ""
        attrs_str = "".join(f' {k}="{v}"' for k, v in self.attributes.items())
        return f"<{self.tag}{class_attr}{attrs_str}>{self.inner_html}</{self.tag}>"

    def render(self) -> ProgressElement:
        """Return self for API compatibility."""
        return self


class Progress:
    """Progress bar component for showing completion percentage.

    Args:
        value: Current progress value (default: 0)
        max: Maximum value (default: 100)
        variant: Progress variant - default, success, warning, error (default: default)
        size: Progress bar size - sm, md, lg (default: md)
        show_label: Whether to show value/max text (default: False)

    Example:
        >>> progress = Progress(value=75, max=100, show_label=True)
        >>> print(progress.render_html())
        <div>
            <div class="cn-progress-label"><span>75</span><span>100</span></div>
            <div class="cn-progress">
                <div class="cn-progress-bar" style="width: 75.0%;"></div>
            </div>
        </div>

        >>> success = Progress(value=100, variant="success", size="lg")
        >>> print(success.render_html())
    """

    VARIANTS = ("default", "success", "warning", "error")
    SIZES = ("sm", "md", "lg")

    def __init__(
        self,
        value: float = 0,
        max: float = 100,
        variant: str = "default",
        size: str = "md",
        show_label: bool = False,
    ):
        if max <= 0:
            raise ValueError("max must be greater than 0")
        if value < 0:
            raise ValueError("value cannot be negative")
        if variant not in self.VARIANTS:
            raise ValueError(f"Invalid variant '{variant}'. Must be one of {self.VARIANTS}")
        if size not in self.SIZES:
            raise ValueError(f"Invalid size '{size}'. Must be one of {self.SIZES}")

        self.value = value
        self.max = max
        self.variant = variant
        self.size = size
        self.show_label = show_label

    def render(self) -> ProgressElement:
        """Render the progress bar as a ProgressElement.

        Returns:
            ProgressElement representing the progress bar
        """
        parts = []

        # Label
        if self.show_label:
            parts.append(
                f'<div class="cn-progress-label">'
                f"<span>{int(self.value)}</span>"
                f"<span>{int(self.max)}</span>"
                f"</div>"
            )

        # Progress bar container
        bar_classes = ["cn-progress"]
        if self.size != "md":
            bar_classes.append(f"cn-progress-{self.size}")
        if self.variant != "default":
            bar_classes.append(f"cn-progress-{self.variant}")

        # Bar fill
        percentage = (self.value / self.max) * 100
        bar_fill = f'<div class="cn-progress-bar" style="width: {percentage}%;"></div>'

        parts.append(f'<div class="{" ".join(bar_classes)}">{bar_fill}</div>')

        return ProgressElement(inner_html="".join(parts))

    def render_html(self) -> str:
        """Render the progress bar as an HTML string.

        Returns:
            HTML string representation of the progress bar
        """
        return self.render().render_html()

    def with_value(self, value: float) -> Progress:
        """Return a new Progress with updated value (immutable pattern).

        Since components generate strings, we can't update in place after rendering.
        Use this to create an updated copy.

        Args:
            value: New progress value

        Returns:
            New Progress instance with the updated value
        """
        return Progress(
            value=value,
            max=self.max,
            variant=self.variant,
            size=self.size,
            show_label=self.show_label,
        )


class Stat:
    """Stat component for displaying metrics with optional delta/ trend.

    Args:
        value: Primary stat value (e.g. "1,234")
        label: Stat label (e.g. "Total Users")
        delta: Optional delta text (e.g. "+12%")
        delta_type: Optional delta type for styling (e.g. "positive", "negative")

    Example:
        >>> stat = Stat(value="1,234", label="Total Users", delta="+12%", delta_type="positive")
        >>> print(stat.render_html())
        <div class="cn-stat">
            <div class="cn-stat-value">1,234</div>
            <div class="cn-stat-label">Total Users</div>
            <div class="cn-stat-delta cn-stat-delta-positive">+12%</div>
        </div>
    """

    def __init__(
        self,
        value: str,
        label: str,
        delta: str | None = None,
        delta_type: str | None = None,
    ):
        if not value:
            raise ValueError("value cannot be empty")
        if not label:
            raise ValueError("label cannot be empty")

        self.value = value
        self.label = label
        self.delta = delta
        self.delta_type = delta_type

    def render(self) -> ProgressElement:
        """Render the stat as a ProgressElement.

        Returns:
            ProgressElement representing the stat display
        """
        parts = [
            f'<div class="cn-stat-value">{self._esc(self.value)}</div>',
            f'<div class="cn-stat-label">{self._esc(self.label)}</div>',
        ]

        if self.delta:
            delta_classes = ["cn-stat-delta"]
            if self.delta_type:
                delta_classes.append(f"cn-stat-delta-{self.delta_type}")
            parts.append(f'<div class="{" ".join(delta_classes)}">{self._esc(self.delta)}</div>')

        return ProgressElement(
            classes=["cn-stat"],
            inner_html="".join(parts),
        )

    def render_html(self) -> str:
        """Render the stat as an HTML string.

        Returns:
            HTML string representation of the stat
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
