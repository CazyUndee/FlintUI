"""Tests for CronixUI core module."""

from cronixui.core import (
    ComponentGroup,
    HtmlElement,
    attrs,
    classes,
    el,
    escape_html,
)


class TestHtmlElement:
    """Test HtmlElement dataclass."""

    def test_basic_element(self):
        el = HtmlElement(tag="div", text="Hello")
        html = el.render_html()
        assert "<div>Hello</div>" == html

    def test_element_with_classes(self):
        el = HtmlElement(tag="div", classes=["container", "main"])
        html = el.render_html()
        assert 'class="container main"' in html

    def test_element_with_attributes(self):
        el = HtmlElement(tag="input", attributes={"type": "text", "placeholder": "Enter"})
        html = el.render_html()
        assert 'type="text"' in html
        assert 'placeholder="Enter"' in html

    def test_element_with_nested_html(self):
        inner = HtmlElement(tag="span", text="inner")
        outer = HtmlElement(tag="div", children=[inner])
        html = outer.render_html()
        assert "<div><span>inner</span></div>" == html

    def test_self_closing_element(self):
        el = HtmlElement(tag="br")
        html = el.render_html()
        assert "<br />" == html

    def test_escape_html_content(self):
        el = HtmlElement(tag="div", text="<script>alert('xss')</script>")
        html = el.render_html()
        assert "&lt;script&gt;" in html


class TestHelperFunctions:
    """Test core helper functions."""

    def test_el_function(self):
        result = el("div", "container")
        assert isinstance(result, HtmlElement)
        assert result.tag == "div"
        assert "container" in result.classes

    def test_el_with_attributes(self):
        result = el("input", attrs={"type": "text", "placeholder": "Search"})
        assert result.attributes.get("type") == "text"
        assert result.attributes.get("placeholder") == "Search"

    def test_classes_function(self):
        result = classes("btn", "btn-primary", "btn-lg")
        assert "btn btn-primary btn-lg" == result

    def test_classes_function_with_empty(self):
        result = classes()
        assert result == ""

    def test_attrs_function(self):
        result = attrs(id="main", class_name="container")
        assert 'id="main"' in result
        assert 'class-name="container"' in result

    def test_attrs_function_with_empty(self):
        result = attrs()
        assert result == ""

    def test_escape_html_function(self):
        assert escape_html("<div>") == "&lt;div&gt;"
        assert escape_html("&") == "&amp;"
        assert escape_html('"') == "&quot;"
        assert escape_html("'") == "&#x27;"

    def test_escape_html_with_safe_string(self):
        # Should not escape already safe strings
        safe = "Hello World"
        assert escape_html(safe) == safe


class TestComponentGroup:
    """Test ComponentGroup."""

    def test_component_group_render(self):
        group = ComponentGroup()
        html = group.render_html()
        assert "<div></div>" == html

    def test_component_group_with_elements(self):
        el1 = HtmlElement(tag="div", text="One")
        el2 = HtmlElement(tag="div", text="Two")
        group = ComponentGroup(children=[el1, el2])
        html = group.render_html()
        assert "<div>One</div><div>Two</div>" in html
