"""CronixUI Table Component.

Generates HTML for data tables with optional sorting indication.
No browser DOM APIs are used - all output is HTML strings or data structures.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TableElement:
    """Represents a rendered table element."""

    tag: str = "div"
    classes: list[str] = field(default_factory=list)
    attributes: dict[str, str] = field(default_factory=dict)
    inner_html: str = ""

    def render_html(self) -> str:
        """Render as HTML string.

        Returns:
            Complete HTML for the table element
        """
        class_str = " ".join(self.classes)
        class_attr = f' class="{class_str}"' if class_str else ""
        attrs_str = "".join(f' {k}="{v}"' for k, v in self.attributes.items())
        return f"<{self.tag}{class_attr}{attrs_str}>{self.inner_html}</{self.tag}>"

    def render(self) -> TableElement:
        """Return self for API compatibility."""
        return self


class Table:
    """Table component for displaying tabular data.

    Args:
        headers: List of column header strings
        rows: List of rows, where each row is a list of cell strings
        sortable: Whether to add sortable class to the table (default: False)
        caption: Optional table caption/summary

    Example:
        >>> table = Table(
        ...     headers=["Name", "Email", "Role"],
        ...     rows=[
        ...         ["Alice", "alice@example.com", "Admin"],
        ...         ["Bob", "bob@example.com", "User"],
        ...     ],
        ... )
        >>> print(table.render_html())
        <div class="cn-table-wrapper">
            <table class="cn-table">
                <thead><tr><th>Name</th><th>Email</th><th>Role</th></tr></thead>
                <tbody>
                    <tr><td>Alice</td><td>alice@example.com</td><td>Admin</td></tr>
                    <tr><td>Bob</td><td>bob@example.com</td><td>User</td></tr>
                </tbody>
            </table>
        </div>
    """

    def __init__(
        self,
        headers: list[str],
        rows: list[list[str]],
        sortable: bool = False,
        caption: str | None = None,
    ):
        if not headers:
            raise ValueError("headers cannot be empty")

        self.headers = headers
        self.rows = rows
        self.sortable = sortable
        self.caption = caption

    def render(self) -> TableElement:
        """Render the table as a TableElement.

        Returns:
            TableElement containing the complete table markup
        """
        parts = []

        # Optional caption
        if self.caption:
            parts.append(f"<caption>{self._esc(self.caption)}</caption>")

        # Header
        header_cells = "".join(f"<th>{self._esc(h)}</th>" for h in self.headers)
        parts.append(f"<thead><tr>{header_cells}</tr></thead>")

        # Body
        body_rows = []
        for row in self.rows:
            cells = "".join(f"<td>{self._esc(str(cell))}</td>" for cell in row)
            body_rows.append(f"<tr>{cells}</tr>")
        parts.append(f"<tbody>{''.join(body_rows)}</tbody>")

        table_classes = ["cn-table"]
        if self.sortable:
            table_classes.append("cn-table-sortable")

        table_html = f'<table class="{" ".join(table_classes)}">{"".join(parts)}</table>'

        return TableElement(
            classes=["cn-table-wrapper"],
            inner_html=table_html,
        )

    def render_html(self) -> str:
        """Render the table as an HTML string.

        Returns:
            HTML string representation of the table
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
