"""CronixUI Button Component"""

from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional


@dataclass
class ButtonElement:
    """Represents a rendered button element."""

    tag: str = "button"
    classes: List[str] = field(default_factory=list)
    attributes: Dict[str, str] = field(default_factory=dict)
    text: str = ""
    onclick: Optional[Callable] = field(default=None, repr=False)

    def render(self) -> str:
        """Render the button as HTML string."""
        class_str = " ".join(self.classes)
        attrs_str = " ".join(f'{k}="{v}"' for k, v in self.attributes.items())
        attrs_str = f" {attrs_str}" if attrs_str else ""

        return f'<{self.tag} class="{class_str}"{attrs_str}>{self.text}</{self.tag}>'


class Button:
    """Button component with variants.

    Args:
        text: Button text
        variant: Button variant (default, primary, ghost, outline, danger, success)
        size: Button size (sm, md, lg)
        icon: Whether button is icon-only
        disabled: Whether button is disabled
        onclick: Click handler callback (for documentation purposes)

    Example:
        >>> btn = Button("Click me", variant="primary")
        >>> print(btn.render())
        <button class="cn-btn cn-btn-primary">Click me</button>
    """

    VARIANTS = ("default", "primary", "ghost", "outline", "danger", "success")
    SIZES = ("sm", "md", "lg")

    def __init__(
        self,
        text: str,
        variant: str = "default",
        size: str = "md",
        icon: bool = False,
        disabled: bool = False,
        onclick: Optional[Callable] = None,
    ):
        if variant not in self.VARIANTS:
            raise ValueError(f"Invalid variant '{variant}'. Must be one of {self.VARIANTS}")
        if size not in self.SIZES:
            raise ValueError(f"Invalid size '{size}'. Must be one of {self.SIZES}")

        self.text = text
        self.variant = variant
        self.size = size
        self.icon = icon
        self.disabled = disabled
        self.onclick = onclick

    def render(self) -> ButtonElement:
        """Render the button as a ButtonElement.

        Returns:
            ButtonElement object representing the rendered button
        """
        classes = ["cn-btn", f"cn-btn-{self.variant}"]

        if self.size != "md":
            classes.append(f"cn-btn-{self.size}")

        if self.icon:
            classes.append("cn-btn-icon")

        attributes: Dict[str, str] = {}
        if self.disabled:
            attributes["disabled"] = ""

        return ButtonElement(
            classes=classes,
            attributes=attributes,
            text=self.text,
            onclick=self.onclick,
        )

    def render_html(self) -> str:
        """Render the button as HTML string.

        Returns:
            HTML string representation of the button
        """
        return self.render().render()

    def disable(self) -> None:
        """Disable the button."""
        self.disabled = True

    def enable(self) -> None:
        """Enable the button."""
        self.disabled = False


class ButtonGroup:
    """Button group component.

    Args:
        *buttons: Button instances to include in the group

    Example:
        >>> group = ButtonGroup(Button("Left"), Button("Right"))
        >>> print(group.render_html())
    """

    def __init__(self, *buttons: Button):
        self.buttons = buttons

    def render_html(self) -> str:
        """Render the button group as HTML string.

        Returns:
            HTML string representation of the button group
        """
        buttons_html = "".join(btn.render_html() for btn in self.buttons)
        return f'<div class="cn-btn-group">{buttons_html}</div>'
