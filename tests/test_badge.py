"""Tests for CronixUI badge and tag components."""

from cronixui.badge import Badge, Tag


class TestBadge:
    """Test Badge component."""

    def test_basic_badge(self):
        badge = Badge("New")
        html = badge.render_html()
        assert "cn-badge" in html
        assert "New" in html

    def test_badge_variants(self):
        variants = ["default", "accent", "success", "warning", "error", "info"]
        for variant in variants:
            badge = Badge("Test", variant=variant)
            html = badge.render_html()
            if variant != "default":
                assert f"cn-badge-{variant}" in html

    def test_badge_solid_variant(self):
        badge = Badge("Solid", solid=True)
        html = badge.render_html()
        assert "cn-badge-solid" in html

    def test_badge_default_variant(self):
        badge = Badge("Default")
        html = badge.render_html()
        # Default badge shouldn't have variant class
        assert "cn-badge" in html


class TestTag:
    """Test Tag component."""

    def test_basic_tag(self):
        tag = Tag("Tag Name")
        html = tag.render_html()
        assert "cn-tag" in html
        assert "Tag Name" in html

    def test_tag_with_remove(self):
        tag = Tag("Removable", removable=True)
        html = tag.render_html()
        assert "cn-tag" in html
        assert "cn-tag-remove" in html

    def test_tag_without_remove_button(self):
        tag = Tag("No Remove", removable=False)
        html = tag.render_html()
        assert "cn-tag-remove" not in html
