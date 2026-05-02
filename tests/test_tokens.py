"""Tests for CronixUI tokens module."""

import pytest
from cronixui.tokens import (
    ACCENT,
    BG,
    BORDER,
    BORDER_FOCUS,
    BORDER_HOVER,
    ERROR,
    INFO,
    SUCCESS,
    SURFACE,
    TEXT,
    TEXT_DIM,
    TEXT_MUTED,
    WARNING,
    Color,
    layout,
    radius,
    shadow,
    spacing,
    transition,
    typography,
    z_index,
)


class TestColor:
    """Test Color dataclass."""

    def test_color_creation(self):
        color = Color("#ff0000", (255, 0, 0))
        assert color.hex == "#ff0000"
        assert color.rgb == (255, 0, 0)

    def test_color_is_frozen(self):
        """Frozen dataclasses are immutable."""
        color = Color("#ff0000", (255, 0, 0))
        with pytest.raises(Exception):  # FrozenInstanceError
            color.hex = "#00ff00"


class TestDesignTokens:
    """Test design token values."""

    def test_background_colors(self):
        assert BG.hex == "#0a0a0a"
        assert SURFACE.hex == "#111111"

    def test_text_colors(self):
        assert TEXT.hex == "#f0ede8"
        assert TEXT_MUTED == "rgba(240, 237, 232, 0.5)"
        assert TEXT_DIM == "rgba(240, 237, 232, 0.25)"

    def test_accent_colors(self):
        assert ACCENT.hex == "#6b2323"
        assert ACCENT.rgb == (107, 35, 35)

    def test_semantic_colors(self):
        assert SUCCESS.hex == "#1e5028"
        assert WARNING.hex == "#503c14"
        assert ERROR.hex == "#501414"
        assert INFO.hex == "#143550"

    def test_border_colors(self):
        assert BORDER == "rgba(255, 255, 255, 0.08)"
        assert BORDER_HOVER == "rgba(255, 255, 255, 0.15)"
        assert BORDER_FOCUS == "rgba(255, 255, 255, 0.25)"


class TestTypographyTokens:
    """Test typography tokens."""

    def test_typography_instance(self):
        assert "Outfit" in typography.font_family
        assert "JetBrains Mono" in typography.font_mono

    def test_font_sizes(self):
        assert typography.xs == 11
        assert typography.sm == 12
        assert typography.base == 13
        assert typography.md == 14
        assert typography.lg == 16
        assert typography.xl == 20
        assert typography.xxl == 28
        assert typography.xxxl == 36


class TestSpacingTokens:
    """Test spacing tokens."""

    def test_spacing_values(self):
        assert spacing.space_1 == 4
        assert spacing.space_2 == 8
        assert spacing.space_3 == 12
        assert spacing.space_4 == 16
        assert spacing.space_12 == 48


class TestRadiusTokens:
    """Test border radius tokens."""

    def test_radius_values(self):
        assert radius.sm == 6
        assert radius.default == 10
        assert radius.lg == 14
        assert radius.xl == 20
        assert radius.full == 9999


class TestShadowTokens:
    """Test shadow tokens."""

    def test_shadow_values(self):
        assert "0 1px 2px" in shadow.sm
        assert "0 4px 12px" in shadow.default
        assert "0 8px 24px" in shadow.lg
        assert "rgba(107, 35, 35, 0.3)" in shadow.glow


class TestTransitionTokens:
    """Test transition tokens."""

    def test_transition_values(self):
        assert transition.fast == "0.1s ease"
        assert transition.default == "0.15s ease"
        assert transition.slow == "0.25s ease"


class TestZIndexTokens:
    """Test z-index tokens."""

    def test_zindex_values(self):
        assert z_index.dropdown == 100
        assert z_index.sticky == 200
        assert z_index.fixed == 300
        assert z_index.modal_backdrop == 400
        assert z_index.modal == 500
        assert z_index.popover == 600
        assert z_index.tooltip == 700
        assert z_index.toast == 800


class TestLayoutTokens:
    """Test layout tokens."""

    def test_layout_values(self):
        assert layout.container_max == 1200
        assert layout.sidebar_width == 260


class TestDataclassImmutability:
    """Test that all dataclasses are immutable."""

    def test_typography_immutable(self):
        with pytest.raises(Exception):
            typography.font_family = "Arial"

    def test_spacing_immutable(self):
        with pytest.raises(Exception):
            spacing.space_1 = 10

    def test_radius_immutable(self):
        with pytest.raises(Exception):
            radius.sm = 20
