"""Tests for CronixUI card component."""

from cronixui.card import Card, CardElement


class TestCard:
    """Test Card component."""

    def test_basic_card(self):
        card = Card(title="My Card", body="Card content")
        html = card.render_html()
        assert "cn-card" in html
        assert "My Card" in html
        assert "Card content" in html

    def test_card_with_subtitle(self):
        card = Card(title="Title", subtitle="Subtitle", body="Body")
        html = card.render_html()
        assert "Title" in html
        assert "Subtitle" in html
        assert "Body" in html

    def test_clickable_card(self):
        card = Card(title="Clickable", body="Content", clickable=True)
        html = card.render_html()
        assert "cn-card-clickable" in html

    def test_card_without_title(self):
        card = Card(body="Just body")
        html = card.render_html()
        assert "Just body" in html

    def test_card_without_body(self):
        card = Card(title="Just title")
        html = card.render_html()
        assert "Just title" in html

    def test_card_empty(self):
        card = Card()
        html = card.render_html()
        assert "cn-card" in html

    def test_card_returns_card_element(self):
        card = Card()
        result = card.render()
        assert isinstance(result, CardElement)
