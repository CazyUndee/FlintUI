"""CronixUI Avatar Component.

Generates HTML for user avatars (images or initials) and avatar groups.
No browser DOM APIs are used - all output is HTML strings or data structures.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class AvatarElement:
    """Represents a rendered avatar element."""

    tag: str = "div"
    classes: list[str] = field(default_factory=list)
    attributes: dict[str, str] = field(default_factory=dict)
    inner_html: str = ""

    def render_html(self) -> str:
        """Render the avatar as HTML string.

        Returns:
            Complete HTML for the avatar element
        """
        class_str = " ".join(self.classes)
        class_attr = f' class="{class_str}"' if class_str else ""
        attrs_str = "".join(f' {k}="{v}"' for k, v in self.attributes.items())
        return f"<{self.tag}{class_attr}{attrs_str}>{self.inner_html}</{self.tag}>"

    def render(self) -> AvatarElement:
        """Return self for API compatibility."""
        return self


class Avatar:
    """Avatar component for displaying user images or initials.

    Args:
        initials: User initials to display (e.g. "JD")
        image_url: URL to user's avatar image
        size: Avatar size - sm, md, lg, xl (default: md)

    Note:
        If both image_url and initials are provided, image_url takes precedence.

    Example:
        >>> avatar = Avatar(initials="JD", size="lg")
        >>> print(avatar.render_html())
        <div class="cn-avatar cn-avatar-lg">JD</div>

        >>> img_avatar = Avatar(image_url="/path/to/photo.jpg")
        >>> print(img_avatar.render_html())
        <div class="cn-avatar"><img src="/path/to/photo.jpg" alt="" /></div>
    """

    SIZES = ("sm", "md", "lg", "xl")

    def __init__(
        self,
        initials: str | None = None,
        image_url: str | None = None,
        size: str = "md",
    ):
        if size not in self.SIZES:
            raise ValueError(f"Invalid size '{size}'. Must be one of {self.SIZES}")
        if not initials and not image_url:
            raise ValueError("At least one of 'initials' or 'image_url' must be provided")

        self.initials = initials
        self.image_url = image_url
        self.size = size

    def render(self) -> AvatarElement:
        """Render the avatar as an AvatarElement data structure.

        Returns:
            AvatarElement representing the avatar
        """
        classes = ["cn-avatar"]
        if self.size != "md":
            classes.append(f"cn-avatar-{self.size}")

        if self.image_url:
            alt_text = self.initials[:2].upper() if self.initials else "Avatar"
            inner = f'<img src="{self.image_url}" alt="{self._esc(alt_text)}" />'
        elif self.initials:
            inner = self._esc(self.initials[:2].upper())
        else:
            inner = ""

        return AvatarElement(classes=classes, inner_html=inner)

    def render_html(self) -> str:
        """Render the avatar as an HTML string.

        Returns:
            HTML string representation of the avatar
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


class AvatarGroup:
    """Group of overlapping avatars, typically for showing multiple users.

    Args:
        *avatars: Avatar instances to include in the group

    Example:
        >>> avatars = AvatarGroup(
        ...     Avatar(initials="AB"),
        ...     Avatar(initials="CD"),
        ...     Avatar(initials="EF"),
        ... )
        >>> print(avatars.render_html())
        <div class="cn-avatar-group">...</div>
    """

    def __init__(self, *avatars: Avatar):
        if not avatars:
            raise ValueError("At least one avatar must be provided")
        self.avatars = avatars

    def render(self) -> AvatarElement:
        """Render the avatar group as an AvatarElement.

        Returns:
            AvatarElement wrapping all avatar children
        """
        children_html = "".join(a.render_html() for a in self.avatars)
        return AvatarElement(
            classes=["cn-avatar-group"],
            inner_html=children_html,
        )

    def render_html(self) -> str:
        """Render the avatar group as an HTML string.

        Returns:
            HTML string representation of the group
        """
        return self.render().render_html()
