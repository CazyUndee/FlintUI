"""Core CronixUI functions - HTML string generation utilities.

This module provides helper functions and dataclasses for generating HTML
as strings or structured data. It does NOT use browser DOM APIs.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union


def escape_html(text: str) -> str:
    """Escape HTML special characters in text.

    Args:
        text: Raw text that may contain HTML special characters

    Returns:
        Text with HTML special characters escaped

    Example:
        >>> escape_html("<script>alert('xss')</script>")
        '&lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;'
    """
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#x27;")
    )


def classes(*names: str | None, **flags: bool) -> str:
    """Build a CSS class string from names and conditional flags.

    Args:
        *names: Always-included class names (None values are skipped)
        **flags: Conditional class names (key is class suffix, value is boolean)

    Returns:
        Space-separated class string

    Example:
        >>> classes("cn-btn", "cn-btn-primary", active=True, disabled=False)
        'cn-btn cn-btn-primary cn-btn-active'
        >>> classes("cn-btn", size="lg")  # size is truthy string, adds nothing
        'cn-btn'
    """
    parts = [n for n in names if n]
    parts.extend(f"cn-{k}" for k, v in flags.items() if v)
    return " ".join(parts)


def attrs(**kwargs: str | None) -> str:
    """Build an HTML attribute string from keyword arguments.

    Args:
        **kwargs: Attribute name-value pairs (None values are skipped)

    Returns:
        Space-separated attribute string, each as name="value"

    Example:
        >>> attrs(type="text", placeholder="Enter name", disabled="")
        'type="text" placeholder="Enter name" disabled=""'
    """
    parts = []
    for name, value in kwargs.items():
        if value is not None:
            attr_name = name.replace("_", "-")
            parts.append(f'{attr_name}="{value}"')
    result = " ".join(parts)
    return f" {result}" if result else ""


@dataclass
class HtmlElement:
    """Represents a rendered HTML element as a data structure.

    This is the core building block for component rendering. Components
    return HtmlElement instances from their render() method.

    Attributes:
        tag: HTML tag name (e.g. "div", "span", "button")
        classes: List of CSS class names
        attributes: Dictionary of HTML attributes
        text: Text content (escaped automatically in render_html)
        inner_html: Raw HTML content (NOT escaped, use carefully)
        children: Nested child HtmlElement instances

    Example:
        >>> el = HtmlElement(
        ...     tag="div",
        ...     classes=["cn-card"],
        ...     attributes={"data-id": "123"},
        ...     text="Hello"
        ... )
        >>> print(el.render_html())
        <div class="cn-card" data-id="123">Hello</div>
    """

    tag: str
    classes: list[str] = field(default_factory=list)
    attributes: dict[str, str] = field(default_factory=dict)
    text: str = ""
    inner_html: str = ""
    children: list[HtmlElement] = field(default_factory=list)

    def render_html(self) -> str:
        """Render this element and all children as an HTML string.

        Returns:
            Complete HTML string for this element tree
        """
        class_str = " ".join(self.classes)
        class_attr = f' class="{class_str}"' if class_str else ""
        attrs_str = "".join(f' {k}="{v}"' for k, v in self.attributes.items())

        if self.inner_html:
            content = self.inner_html
        elif self.text:
            content = escape_html(self.text)
        elif self.children:
            content = "".join(child.render_html() for child in self.children)
        else:
            return f"<{self.tag}{class_attr}{attrs_str} />"

        return f"<{self.tag}{class_attr}{attrs_str}>{content}</{self.tag}>"

    def render(self) -> HtmlElement:
        """Return self (for API compatibility with components).

        Returns:
            This HtmlElement instance
        """
        return self


@dataclass
class ComponentGroup:
    """Represents a group of components wrapped in a container.

    Useful for rendering multiple components together.

    Attributes:
        tag: Container tag name (default: "div")
        classes: CSS classes for the container
        children: List of components or HtmlElements

    Example:
        >>> group = ComponentGroup(
        ...     classes="cn-stack",
        ...     children=[Button("A"), Button("B")]
        ... )
        >>> print(group.render_html())
    """

    tag: str = "div"
    classes: list[str] = field(default_factory=list)
    attributes: dict[str, str] = field(default_factory=dict)
    children: list[Union[HtmlElement, ComponentGroup]] = field(default_factory=list)

    def render_html(self) -> str:
        """Render all children as HTML inside the container.

        Returns:
            HTML string with container wrapping all children
        """
        class_str = " ".join(self.classes)
        class_attr = f' class="{class_str}"' if class_str else ""
        attrs_str = "".join(f' {k}="{v}"' for k, v in self.attributes.items())
        children_html = "".join(
            child.render_html() if hasattr(child, "render_html") else str(child)
            for child in self.children
        )
        return f"<{self.tag}{class_attr}{attrs_str}>{children_html}</{self.tag}>"

    def render(self) -> ComponentGroup:
        """Return self (for API compatibility).

        Returns:
            This ComponentGroup instance
        """
        return self


def el(
    tag: str,
    class_name: str | None = None,
    attrs: dict[str, str] | None = None,
    text: str = "",
    inner_html: str = "",
    children: list[HtmlElement] | None = None,
) -> HtmlElement:
    """Create an HtmlElement with a convenient builder API.

    This is the primary replacement for the old create_el() function.
    Instead of returning DOM-like objects, it returns data structures
    that can generate HTML strings.

    Args:
        tag: HTML tag name
        class_name: Space-separated CSS class string (auto-split)
        attrs: HTML attributes dictionary
        text: Text content (will be escaped)
        inner_html: Raw HTML content (not escaped)
        children: List of child HtmlElement instances

    Returns:
        HtmlElement instance

    Example:
        >>> card = el("div", "cn-card", {"data-id": "1"})
        >>> title = el("h3", "cn-card-title", text="My Card")
        >>> card.children.append(title)
        >>> print(card.render_html())
        <div class="cn-card" data-id="1"><h3 class="cn-card-title">My Card</h3></div>
    """
    classes_list = class_name.split() if class_name else []
    return HtmlElement(
        tag=tag,
        classes=classes_list,
        attributes=attrs or {},
        text=text,
        inner_html=inner_html,
        children=children or [],
    )
