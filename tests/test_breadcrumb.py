"""Tests for CronixUI breadcrumb component."""

from cronixui.breadcrumb import Breadcrumb, BreadcrumbElement, BreadcrumbItem


class TestBreadcrumbElement:
    """Test BreadcrumbElement dataclass."""

    def test_default_render(self):
        el = BreadcrumbElement(classes=["cn-breadcrumb"], inner_html="x")
        html = el.render_html()
        assert html == '<nav class="cn-breadcrumb">x</nav>'

    def test_render_with_attributes(self):
        el = BreadcrumbElement(
            classes=["cn-breadcrumb"],
            attributes={"aria-label": "Breadcrumb"},
            inner_html="",
        )
        html = el.render_html()
        assert 'class="cn-breadcrumb"' in html
        assert 'aria-label="Breadcrumb"' in html

    def test_render_returns_self(self):
        el = BreadcrumbElement()
        assert el.render() is el


class TestBreadcrumb:
    """Test Breadcrumb component."""

    def test_empty_breadcrumb(self):
        bc = Breadcrumb()
        html = bc.render_html()
        assert "cn-breadcrumb" in html
        assert 'aria-label="Breadcrumb"' in html

    def test_single_item_renders_as_current(self):
        bc = Breadcrumb(items=[BreadcrumbItem(label="Home", href="/")])
        html = bc.render_html()
        assert "cn-breadcrumb-current" in html
        assert 'aria-current="page"' in html
        assert "Home" in html
        assert "cn-breadcrumb-item" not in html

    def test_last_item_is_current(self):
        bc = Breadcrumb(
            items=[
                BreadcrumbItem(label="Home", href="/"),
                BreadcrumbItem(label="Products", href="/products"),
                BreadcrumbItem(label="Details", href="/products/1"),
            ]
        )
        html = bc.render_html()
        assert html.count("cn-breadcrumb-item") == 2
        assert html.count("cn-breadcrumb-current") == 1
        assert html.endswith(
            '<span class="cn-breadcrumb-current" aria-current="page">Details</span></nav>'
        )

    def test_separator_between_items(self):
        bc = Breadcrumb(
            items=[
                BreadcrumbItem(label="Home", href="/"),
                BreadcrumbItem(label="Products", href="/products"),
            ]
        )
        html = bc.render_html()
        assert html.count("cn-breadcrumb-separator") == 1
        assert 'aria-hidden="true"' in html

    def test_custom_separator(self):
        bc = Breadcrumb(
            items=[
                BreadcrumbItem(label="A", href="/a"),
                BreadcrumbItem(label="B", href="/b"),
            ],
            separator=">",
        )
        html = bc.render_html()
        assert '<span class="cn-breadcrumb-separator" aria-hidden="true">&gt;</span>' in html
        assert '<span class="cn-breadcrumb-separator" aria-hidden="true">/</span>' not in html

    def test_explicit_active_item(self):
        bc = Breadcrumb(
            items=[
                BreadcrumbItem(label="Home", href="/"),
                BreadcrumbItem(label="Active", href="/active", active=True),
                BreadcrumbItem(label="Trailing", href="/trailing"),
            ]
        )
        html = bc.render_html()
        assert html.count("cn-breadcrumb-current") == 1
        assert html.count("cn-breadcrumb-item") == 2
        assert "Active" in html
        assert 'aria-current="page"' in html
        # The explicit active item should be current, not the last item
        assert '<span class="cn-breadcrumb-current" aria-current="page">Active</span>' in html

    def test_html_escaping(self):
        bc = Breadcrumb(
            items=[
                BreadcrumbItem(label="<Home>", href='/?a=1&b="2"'),
                BreadcrumbItem(label="A & B"),
            ]
        )
        html = bc.render_html()
        assert "<Home>" not in html
        assert "&lt;Home&gt;" in html
        assert "&amp;" in html
        assert "&quot;" in html

    def test_render_returns_breadcrumb_element(self):
        bc = Breadcrumb(items=[BreadcrumbItem(label="Home")])
        result = bc.render()
        assert isinstance(result, BreadcrumbElement)
        assert result.tag == "nav"
        assert result.classes == ["cn-breadcrumb"]
        assert result.attributes == {"aria-label": "Breadcrumb"}

    def test_default_href(self):
        item = BreadcrumbItem(label="Test")
        assert item.href == "#"
        assert item.active is False
