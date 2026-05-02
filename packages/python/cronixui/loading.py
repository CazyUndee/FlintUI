"""CronixUI Loading Components.

Generates HTML for spinners and skeleton loading placeholders.
No browser DOM APIs are used - all output is HTML strings or data structures.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class LoadingElement:
    """Represents a rendered loading element."""

    tag: str = "div"
    classes: list[str] = field(default_factory=list)
    attributes: dict[str, str] = field(default_factory=dict)
    inner_html: str = ""

    def render_html(self) -> str:
        """Render as HTML string.

        Returns:
            Complete HTML for the loading element
        """
        class_str = " ".join(self.classes)
        class_attr = f' class="{class_str}"' if class_str else ""
        attrs_str = "".join(f' {k}="{v}"' for k, v in self.attributes.items())
        return f"<{self.tag}{class_attr}{attrs_str}>{self.inner_html}</{self.tag}>"

    def render(self) -> LoadingElement:
        """Return self for API compatibility."""
        return self


class Spinner:
    """Loading spinner component.

    Args:
        size: Spinner size - sm, md, lg (default: md)

    Example:
        >>> spinner = Spinner(size="lg")
        >>> print(spinner.render_html())
        <div class="cn-spinner cn-spinner-lg"></div>
    """

    SIZES = ("sm", "md", "lg")

    def __init__(self, size: str = "md"):
        if size not in self.SIZES:
            raise ValueError(f"Invalid size '{size}'. Must be one of {self.SIZES}")

        self.size = size

    def render(self) -> LoadingElement:
        """Render the spinner as a LoadingElement.

        Returns:
            LoadingElement representing the spinner
        """
        classes = ["cn-spinner"]
        if self.size != "md":
            classes.append(f"cn-spinner-{self.size}")

        return LoadingElement(classes=classes)

    def render_html(self) -> str:
        """Render the spinner as an HTML string.

        Returns:
            HTML string representation of the spinner
        """
        return self.render().render_html()


class Skeleton:
    """Skeleton loading placeholder for content while it loads.

    Args:
        variant: Skeleton type - text, title, avatar (default: text)
        width: Optional CSS width for the skeleton (e.g. "200px", "50%")

    Example:
        >>> skeleton = Skeleton(variant="title", width="300px")
        >>> print(skeleton.render_html())
        <div class="cn-skeleton cn-skeleton-title" style="width: 300px;"></div>
    """

    VARIANTS = ("text", "title", "avatar")

    def __init__(self, variant: str = "text", width: str | None = None):
        if variant not in self.VARIANTS:
            raise ValueError(f"Invalid variant '{variant}'. Must be one of {self.VARIANTS}")

        self.variant = variant
        self.width = width

    def render(self) -> LoadingElement:
        """Render the skeleton as a LoadingElement.

        Returns:
            LoadingElement representing the skeleton placeholder
        """
        classes = ["cn-skeleton", f"cn-skeleton-{self.variant}"]

        attrs: dict[str, str] = {}
        if self.width:
            attrs["style"] = f"width: {self.width};"

        return LoadingElement(
            classes=classes,
            attributes=attrs,
        )

    def render_html(self) -> str:
        """Render the skeleton as an HTML string.

        Returns:
            HTML string representation of the skeleton placeholder
        """
        return self.render().render_html()
