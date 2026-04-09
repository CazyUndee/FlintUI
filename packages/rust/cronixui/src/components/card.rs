//! Card component

use egui::*;
use crate::{colors::*, tokens::*};

/// Icon component for Card header
pub struct CardIcon {
    pub icon: String,
    pub size: f32,
}

impl CardIcon {
    pub fn new(icon: impl Into<String>) -> Self {
        Self { icon: icon.into(), size: tokens::FONT_SIZE_LG }
    }

    pub fn size(mut self, size: f32) -> Self {
        self.size = size;
        self
    }

    pub fn show(&self, ui: &mut Ui) {
        let colors = Colors::default();
        ui.label(
            RichText::new(&self.icon)
                .size(self.size)
                .color(colors.text_muted),
        );
    }
}

/// Title component
pub struct CardTitle {
    pub text: String,
    pub size: f32,
}

impl CardTitle {
    pub fn new(text: impl Into<String>) -> Self {
        Self { text: text.into(), size: tokens::FONT_SIZE_MD }
    }

    pub fn size(mut self, size: f32) -> Self {
        self.size = size;
        self
    }

    pub fn show(&self, ui: &mut Ui) {
        let colors = Colors::default();
        ui.label(
            RichText::new(&self.text)
                .size(self.size)
                .color(colors.text)
                .strong(),
        );
    }
}

/// Subtitle component
pub struct CardSubtitle {
    pub text: String,
    pub size: f32,
}

impl CardSubtitle {
    pub fn new(text: impl Into<String>) -> Self {
        Self { text: text.into(), size: tokens::FONT_SIZE_SM }
    }

    pub fn size(mut self, size: f32) -> Self {
        self.size = size;
        self
    }

    pub fn show(&self, ui: &mut Ui) {
        let colors = Colors::default();
        ui.label(
            RichText::new(&self.text)
                .size(self.size)
                .color(colors.text_muted),
        );
    }
}

/// Card header component (combines icon, title, subtitle)
pub struct CardHeader {
    pub icon: Option<CardIcon>,
    pub title: Option<CardTitle>,
    pub subtitle: Option<CardSubtitle>,
}

impl CardHeader {
    pub fn new() -> Self {
        Self { icon: None, title: None, subtitle: None }
    }

    pub fn icon(mut self, icon: CardIcon) -> Self {
        self.icon = Some(icon);
        self
    }

    pub fn title(mut self, title: CardTitle) -> Self {
        self.title = Some(title);
        self
    }

    pub fn subtitle(mut self, subtitle: CardSubtitle) -> Self {
        self.subtitle = Some(subtitle);
        self
    }

    pub fn show(&self, ui: &mut Ui) {
        ui.horizontal(|ui| {
            if let Some(icon) = &self.icon {
                icon.show(ui);
                ui.add_space(tokens::SPACE_2);
            }

            ui.vertical(|ui| {
                if let Some(title) = &self.title {
                    title.show(ui);
                }
                if let Some(subtitle) = &self.subtitle {
                    subtitle.show(ui);
                }
            });
        });
    }
}

impl Default for CardHeader {
    fn default() -> Self {
        Self::new()
    }
}

/// Card body component
pub struct CardBody;

impl CardBody {
    pub fn new() -> Self {
        Self
    }

    pub fn show<R>(&self, ui: &mut Ui, add_contents: impl FnOnce(&mut Ui) -> R) {
        add_contents(ui);
    }
}

impl Default for CardBody {
    fn default() -> Self {
        Self::new()
    }
}

/// Card footer component
pub struct CardFooter {
    pub separator: bool,
}

impl CardFooter {
    pub fn new() -> Self {
        Self { separator: true }
    }

    pub fn separator(mut self, separator: bool) -> Self {
        self.separator = separator;
        self
    }

    pub fn show<R>(&self, ui: &mut Ui, add_contents: impl FnOnce(&mut Ui) -> R) {
        if self.separator {
            ui.separator();
            ui.add_space(tokens::SPACE_2);
        }
        add_contents(ui);
    }
}

impl Default for CardFooter {
    fn default() -> Self {
        Self::new()
    }
}

/// Main Card component with builder pattern
pub struct Card {
    pub header: Option<CardHeader>,
    pub clickable: bool,
}

impl Card {
    pub fn new() -> Self {
        Self { header: None, clickable: false }
    }

    pub fn title(mut self, title: impl Into<String>) -> Self {
        let title_comp = CardTitle::new(title);
        self.header = Some(
            self.header.unwrap_or_else(CardHeader::new).title(title_comp),
        );
        self
    }

    pub fn subtitle(mut self, subtitle: impl Into<String>) -> Self {
        let subtitle_comp = CardSubtitle::new(subtitle);
        self.header = Some(
            self.header.unwrap_or_else(CardHeader::new).subtitle(subtitle_comp),
        );
        self
    }

    pub fn icon(mut self, icon: impl Into<String>) -> Self {
        let icon_comp = CardIcon::new(icon);
        self.header = Some(
            self.header.unwrap_or_else(CardHeader::new).icon(icon_comp),
        );
        self
    }

    pub fn header(mut self, header: CardHeader) -> Self {
        self.header = Some(header);
        self
    }

    pub fn clickable(mut self, clickable: bool) -> Self {
        self.clickable = clickable;
        self
    }

    pub fn show<R>(&self, ui: &mut Ui, add_contents: impl FnOnce(&mut Ui) -> R) -> Response {
        let colors = Colors::default();

        let frame = egui::Frame::none()
            .fill(colors.surface)
            .stroke(Stroke::new(1.0, colors.border))
            .rounding(Rounding::same(RADIUS_LG))
            .inner_margin(SPACE_5);

        let inner_response = frame.show(ui, |ui| {
            // Render header if present
            if let Some(header) = &self.header {
                header.show(ui);
                ui.add_space(SPACE_4);
            }

            // Render body
            add_contents(ui)
        });

        inner_response.response
    }
}

impl Default for Card {
    fn default() -> Self {
        Self::new()
    }
}
