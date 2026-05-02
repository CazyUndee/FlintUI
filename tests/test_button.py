"""Tests for CronixUI button component."""

import pytest
from cronixui.button import Button, ButtonElement, ButtonGroup


class TestButtonElement:
    """Test ButtonElement dataclass."""

    def test_basic_render(self):
        el = ButtonElement(text="Click me", classes=["cn-btn"])
        html = el.render()
        assert '<button class="cn-btn">Click me</button>' == html

    def test_render_with_attributes(self):
        el = ButtonElement(
            text="Submit",
            classes=["cn-btn", "cn-btn-primary"],
            attributes={"disabled": "", "type": "submit"},
        )
        html = el.render()
        assert 'class="cn-btn cn-btn-primary"' in html
        assert "Submit" in html
        assert "disabled" in html
        assert 'type="submit"' in html

    def test_render_empty_classes(self):
        el = ButtonElement(text="Test", classes=[])
        html = el.render()
        assert '<button class="">Test</button>' == html


class TestButton:
    """Test Button component."""

    def test_default_button(self):
        btn = Button("Click me")
        assert btn.text == "Click me"
        assert btn.variant == "default"
        assert btn.size == "md"
        assert btn.disabled is False

    def test_button_variant(self):
        btn = Button("Primary", variant="primary")
        html = btn.render_html()
        assert "cn-btn-primary" in html
        assert "cn-btn" in html

    def test_button_size_sm(self):
        btn = Button("Small", size="sm")
        html = btn.render_html()
        assert "cn-btn-sm" in html

    def test_button_size_lg(self):
        btn = Button("Large", size="lg")
        html = btn.render_html()
        assert "cn-btn-lg" in html

    def test_button_icon(self):
        btn = Button("Icon", icon=True)
        html = btn.render_html()
        assert "cn-btn-icon" in html

    def test_button_disabled(self):
        btn = Button("Disabled", disabled=True)
        html = btn.render_html()
        assert "disabled" in html

    def test_button_with_onclick(self):
        def handler():
            pass

        btn = Button("Click", onclick=handler)
        assert btn.onclick == handler

    def test_invalid_variant_raises_error(self):
        with pytest.raises(ValueError, match="Invalid variant"):
            Button("Test", variant="invalid")

    def test_invalid_size_raises_error(self):
        with pytest.raises(ValueError, match="Invalid size"):
            Button("Test", size="xl")

    def test_all_variants_work(self):
        for variant in Button.VARIANTS:
            btn = Button(f"{variant} button", variant=variant)
            html = btn.render_html()
            assert f"cn-btn-{variant}" in html

    def test_all_sizes_work(self):
        for size in Button.SIZES:
            btn = Button(f"{size} button", size=size)
            if size == "md":
                assert "cn-btn-md" not in btn.render_html()
            else:
                assert f"cn-btn-{size}" in btn.render_html()

    def test_enable_disable(self):
        btn = Button("Toggle")
        assert btn.disabled is False

        btn.disable()
        assert btn.disabled is True

        btn.enable()
        assert btn.disabled is False

    def test_render_returns_button_element(self):
        btn = Button("Test")
        result = btn.render()
        assert isinstance(result, ButtonElement)


class TestButtonGroup:
    """Test ButtonGroup component."""

    def test_button_group_render(self):
        btn1 = Button("Left")
        btn2 = Button("Center")
        btn3 = Button("Right")

        group = ButtonGroup(btn1, btn2, btn3)
        html = group.render_html()

        assert 'class="cn-btn-group"' in html
        assert "Left" in html
        assert "Center" in html
        assert "Right" in html

    def test_empty_button_group(self):
        group = ButtonGroup()
        html = group.render_html()
        assert 'class="cn-btn-group"' in html
        assert html.count("<button") == 0

    def test_button_group_with_variants(self):
        btn1 = Button("Primary", variant="primary")
        btn2 = Button("Danger", variant="danger")

        group = ButtonGroup(btn1, btn2)
        html = group.render_html()

        assert "cn-btn-primary" in html
        assert "cn-btn-danger" in html
