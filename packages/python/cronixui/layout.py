"""CronixUI Layout Components.

Generates HTML for headers, sidebars, footers, containers, dividers, and sections.
No browser DOM APIs are used - all output is HTML strings or data structures.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class LayoutElement:
    """Represents a rendered layout element."""

    tag: str = "div"
    classes: list[str] = field(default_factory=list)
    attributes: dict[str, str] = field(default_factory=dict)
    inner_html: str = ""

    def render_html(self) -> str:
        """Render as HTML string.

        Returns:
            Complete HTML for the layout element
        """
        class_str = " ".join(self.classes)
        class_attr = f' class="{class_str}"' if class_str else ""
        attrs_str = "".join(f' {k}="{v}"' for k, v in self.attributes.items())
        return f"<{self.tag}{class_attr}{attrs_str}>{self.inner_html}</{self.tag}>"

    def render(self) -> LayoutElement:
        """Return self for API compatibility."""
        return self


@dataclass
class NavItem:
    """A navigation item for headers and sidebars.

    Attributes:
        text: Display text
        href: Link URL (default: "#")
        icon: Optional SVG icon markup
        active: Whether item is highlighted
    """

    text: str
    href: str = "#"
    icon: str | None = None
    active: bool = False


class Header:
    """Header component with brand, navigation, and action slots.

    Args:
        brand: Brand/site name
        nav_items: Optional list of NavItem instances
        action_html: Optional HTML string for the actions slot

    Example:
        >>> header = Header(
        ...     brand="MyApp",
        ...     nav_items=[
        ...         NavItem(text="Home", href="/"),
        ...         NavItem(text="About", href="/about"),
        ...     ],
        ... )
        >>> print(header.render_html())
        <header class="cn-header">
            <a class="cn-header-brand">MyApp</a>
            <nav class="cn-header-nav">
                <a class="cn-btn cn-btn-ghost" href="/">Home</a>
                <a class="cn-btn cn-btn-ghost" href="/about">About</a>
            </nav>
            <div class="cn-header-actions"></div>
        </header>
    """

    def __init__(
        self,
        brand: str = "",
        nav_items: list[NavItem] | None = None,
        action_html: str | None = None,
    ):
        self.brand = brand
        self.nav_items = nav_items or []
        self.action_html = action_html or ""

    def render(self) -> LayoutElement:
        """Render the header as a LayoutElement.

        Returns:
            LayoutElement representing the header
        """
        parts = [f'<a class="cn-header-brand">{self._esc(self.brand)}</a>']

        # Navigation
        nav_items_html = "".join(
            f'<a class="cn-btn cn-btn-ghost" href="{self._esc(item.href)}">'
            f"{self._esc(item.text)}</a>"
            for item in self.nav_items
        )
        parts.append(f'<nav class="cn-header-nav">{nav_items_html}</nav>')

        # Actions
        parts.append(f'<div class="cn-header-actions">{self.action_html}</div>')

        return LayoutElement(
            tag="header",
            classes=["cn-header"],
            inner_html="".join(parts),
        )

    def render_html(self) -> str:
        """Render the header as an HTML string.

        Returns:
            HTML string representation of the header
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


class Sidebar:
    """Sidebar navigation component.

    Args:
        items: Optional list of NavItem instances
        header_html: Optional HTML for the sidebar header
        footer_html: Optional HTML for the sidebar footer

    Example:
        >>> sidebar = Sidebar(
        ...     items=[
        ...         NavItem(text="Dashboard", icon="<svg>...</svg>", active=True),
        ...         NavItem(text="Settings", icon="<svg>...</svg>"),
        ...     ],
        ... )
        >>> print(sidebar.render_html())
    """

    def __init__(
        self,
        items: list[NavItem] | None = None,
        header_html: str | None = None,
        footer_html: str | None = None,
    ):
        self.items = items or []
        self.header_html = header_html or ""
        self.footer_html = footer_html or ""

    def render(self) -> LayoutElement:
        """Render the sidebar as a LayoutElement.

        Returns:
            LayoutElement representing the sidebar
        """
        parts = []

        # Header
        if self.header_html:
            parts.append(f'<div class="cn-sidebar-header">{self.header_html}</div>')
        else:
            parts.append('<div class="cn-sidebar-header"></div>')

        # Nav items
        nav_parts = []
        for item in self.items:
            active_class = " cn-sidebar-active" if item.active else ""
            item_html = f'<a class="cn-sidebar-item{active_class}" href="{self._esc(item.href)}">'
            if item.icon:
                item_html += f"<span>{item.icon}</span>"
            item_html += f"<span>{self._esc(item.text)}</span>"
            item_html += "</a>"
            nav_parts.append(item_html)

        parts.append(f'<nav class="cn-sidebar-nav">{"".join(nav_parts)}</nav>')

        # Footer
        if self.footer_html:
            parts.append(f'<div class="cn-sidebar-footer">{self.footer_html}</div>')
        else:
            parts.append('<div class="cn-sidebar-footer"></div>')

        return LayoutElement(
            tag="aside",
            classes=["cn-sidebar"],
            inner_html="".join(parts),
        )

    def render_html(self) -> str:
        """Render the sidebar as an HTML string.

        Returns:
            HTML string representation of the sidebar
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


class Footer:
    """Footer component with links and copyright.

    Args:
        copyright: Copyright text
        links: Optional list of (text, href) tuples

    Example:
        >>> footer = Footer(
        ...     copyright="© 2026 My Company",
        ...     links=[("Privacy", "/privacy"), ("Terms", "/terms")],
        ... )
        >>> print(footer.render_html())
    """

    def __init__(
        self,
        copyright: str = "",
        links: list[tuple] | None = None,
    ):
        self.copyright = copyright
        self.links = links or []

    def render(self) -> LayoutElement:
        """Render the footer as a LayoutElement.

        Returns:
            LayoutElement representing the footer
        """
        links_html = "".join(
            f'<a class="cn-footer-link" href="{self._esc(href)}">{self._esc(text)}</a>'
            for text, href in self.links
        )

        inner = (
            f'<div class="cn-footer-content">'
            f'<div class="cn-footer-links">{links_html}</div>'
            f'<div class="cn-footer-copyright">{self._esc(self.copyright)}</div>'
            f"</div>"
        )

        return LayoutElement(
            tag="footer",
            classes=["cn-footer"],
            inner_html=inner,
        )

    def render_html(self) -> str:
        """Render the footer as an HTML string.

        Returns:
            HTML string representation of the footer
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


class Container:
    """Container component for constrained-width layouts.

    Args:
        size: Container size - sm, md, lg, xl, fluid (default: lg)
        inner_html: Optional inner HTML content

    Example:
        >>> container = Container(size="xl", inner_html="<h1>Welcome</h1>")
        >>> print(container.render_html())
        <div class="cn-container cn-container-xl"><h1>Welcome</h1></div>
    """

    SIZES = ("sm", "md", "lg", "xl", "fluid")

    def __init__(self, size: str = "lg", inner_html: str = ""):
        if size not in self.SIZES:
            raise ValueError(f"Invalid size '{size}'. Must be one of {self.SIZES}")

        self.size = size
        self.inner_html = inner_html

    def render(self) -> LayoutElement:
        """Render the container as a LayoutElement.

        Returns:
            LayoutElement representing the container
        """
        classes = ["cn-container"]
        if self.size != "lg":
            classes.append(f"cn-container-{self.size}")

        return LayoutElement(
            classes=classes,
            inner_html=self.inner_html,
        )

    def render_html(self) -> str:
        """Render the container as an HTML string.

        Returns:
            HTML string representation of the container
        """
        return self.render().render_html()


class Divider:
    """Divider component (horizontal rule).

    Example:
        >>> divider = Divider()
        >>> print(divider.render_html())
        <div class="cn-divider" />
    """

    def render(self) -> LayoutElement:
        """Render the divider as a LayoutElement.

        Returns:
            LayoutElement representing the divider
        """
        return LayoutElement(
            classes=["cn-divider"],
        )

    def render_html(self) -> str:
        """Render the divider as an HTML string.

        Returns:
            HTML string representation of the divider
        """
        return self.render().render_html()


class Section:
    """Section spacing component.

    Args:
        size: Section size - sm, md, lg (default: md)
        inner_html: Optional inner HTML content

    Example:
        >>> section = Section(size="lg", inner_html="<p>Section content</p>")
        >>> print(section.render_html())
        <section class="cn-section cn-section-lg"><p>Section content</p></section>
    """

    SIZES = ("sm", "md", "lg")

    def __init__(self, size: str = "md", inner_html: str = ""):
        if size not in self.SIZES:
            raise ValueError(f"Invalid size '{size}'. Must be one of {self.SIZES}")

        self.size = size
        self.inner_html = inner_html

    def render(self) -> LayoutElement:
        """Render the section as a LayoutElement.

        Returns:
            LayoutElement representing the section
        """
        classes = ["cn-section"]
        if self.size != "md":
            classes.append(f"cn-section-{self.size}")

        return LayoutElement(
            tag="section",
            classes=classes,
            inner_html=self.inner_html,
        )

    def render_html(self) -> str:
        """Render the section as an HTML string.

        Returns:
            HTML string representation of the section
        """
        return self.render().render_html()
