//! Breadcrumb component

use egui::*;
use crate::{colors::*, tokens::*};

pub struct Breadcrumb {
    pub items: Vec<String>,
}

impl Breadcrumb {
    pub fn new() -> Self {
        Self { items: Vec::new() }
    }

    pub fn item(mut self, item: impl Into<String>) -> Self {
        self.items.push(item.into());
        self
    }

    pub fn show(&self, ui: &mut Ui) -> Response {
        let colors = Colors::default();

        ui.horizontal(|ui| {
            for (i, item) in self.items.iter().enumerate() {
                if i > 0 {
                    ui.label(
                        RichText::new("/")
                            .size(tokens::FONT_SIZE_SM)
                            .color(colors.text_muted),
                    );
                }

                let is_last = i == self.items.len() - 1;
                if is_last {
                    ui.label(
                        RichText::new(item)
                            .size(tokens::FONT_SIZE_BASE)
                            .color(colors.text)
                            .strong(),
                    );
                } else {
                    ui.hyperlink_to(
                        RichText::new(item)
                            .size(tokens::FONT_SIZE_BASE)
                            .color(colors.accent_text),
                        format!("#{}", item.to_lowercase().replace(" ", "-")),
                    );
                }
            }
        }).response
    }
}

impl Default for Breadcrumb {
    fn default() -> Self {
        Self::new()
    }
}
