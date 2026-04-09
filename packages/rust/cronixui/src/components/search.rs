//! Search component

use egui::*;
use crate::{colors::*, tokens::*};

pub struct SearchItem {
    pub title: String,
    pub subtitle: Option<String>,
}

impl SearchItem {
    pub fn new(title: impl Into<String>) -> Self {
        Self { title: title.into(), subtitle: None }
    }

    pub fn subtitle(mut self, subtitle: impl Into<String>) -> Self {
        self.subtitle = Some(subtitle.into());
        self
    }
}

pub struct Search {
    pub items: Vec<SearchItem>,
    pub query: String,
    id: Id,
}

impl Search {
    pub fn new(id: impl Into<Id>) -> Self {
        Self { items: Vec::new(), query: String::new(), id: id.into() }
    }

    pub fn item(mut self, item: SearchItem) -> Self {
        self.items.push(item);
        self
    }

    pub fn set_items(&mut self, items: Vec<SearchItem>) {
        self.items = items;
    }

    pub fn filter(&self) -> Vec<&SearchItem> {
        if self.query.is_empty() {
            return self.items.iter().collect();
        }
        self.items
            .iter()
            .filter(|item| item.title.to_lowercase().contains(&self.query.to_lowercase()))
            .collect()
    }

    /// Render the search UI with text input and results list
    pub fn show(&mut self, ui: &mut Ui) -> Option<usize> {
        let colors = Colors::default();
        let mut selected = None;

        // Search input field
        ui.horizontal(|ui| {
            ui.label("🔍");
            let response = ui.add(
                TextEdit::singleline(&mut self.query)
                    .hint_text("Search...")
                    .desired_width(f32::INFINITY)
                    .font(FontId::new(tokens::FONT_SIZE_BASE, FontFamily::Proportional)),
            );

            if response.has_focus() {
                // Show results dropdown when focused
            }
        });

        // Results list
        let results = self.filter();
        if !results.is_empty() {
            egui::Frame::none()
                .fill(colors.surface)
                .stroke(egui::Stroke::new(1.0, colors.border))
                .rounding(Rounding::same(tokens::RADIUS))
                .inner_margin(SPACE_2)
                .show(ui, |ui| {
                    for (idx, item) in results.iter().enumerate() {
                        let response = ui.horizontal(|ui| {
                            ui.label(
                                RichText::new(&item.title)
                                    .size(tokens::FONT_SIZE_BASE)
                                    .color(colors.text),
                            );
                            if let Some(subtitle) = &item.subtitle {
                                ui.label(
                                    RichText::new(subtitle)
                                        .size(tokens::FONT_SIZE_SM)
                                        .color(colors.text_muted),
                                );
                            }
                        });

                        if response.response.clicked() {
                            // Find original index
                            if let Some(orig_idx) = self.items.iter().position(|i| std::ptr::eq(i, *item)) {
                                selected = Some(orig_idx);
                            }
                        }
                    }
                });
        } else if !self.query.is_empty() {
            ui.label(
                RichText::new("No results found")
                    .size(tokens::FONT_SIZE_SM)
                    .color(colors.text_muted),
            );
        }

        selected
    }
}

impl Default for Search {
    fn default() -> Self {
        Self::new("default_search")
    }
}

/// Functional search helper
pub fn search(ui: &mut Ui, query: &mut String, items: &[SearchItem]) -> Vec<&SearchItem> {
    let colors = Colors::default();

    ui.add(
        TextEdit::singleline(query)
            .hint_text("Search...")
            .desired_width(f32::INFINITY),
    );

    if query.is_empty() {
        return items.iter().collect();
    }

    items
        .iter()
        .filter(|item| item.title.to_lowercase().contains(&query.to_lowercase()))
        .collect()
}

/// Render search results list
pub fn search_results(ui: &mut Ui, results: &[&SearchItem]) -> Option<usize> {
    let colors = Colors::default();
    let mut clicked = None;

    if !results.is_empty() {
        egui::Frame::none()
            .fill(colors.surface)
            .stroke(egui::Stroke::new(1.0, colors.border))
            .rounding(Rounding::same(tokens::RADIUS))
            .inner_margin(SPACE_2)
            .show(ui, |ui| {
                for (idx, item) in results.iter().enumerate() {
                    let response = ui.horizontal(|ui| {
                        ui.label(
                            RichText::new(&item.title)
                                .size(tokens::FONT_SIZE_BASE)
                                .color(colors.text),
                        );
                        if let Some(subtitle) = &item.subtitle {
                            ui.label(
                                RichText::new(subtitle)
                                    .size(tokens::FONT_SIZE_SM)
                                    .color(colors.text_muted),
                            );
                        }
                    });

                    if response.response.clicked() {
                        clicked = Some(idx);
                    }
                }
            });
    } else {
        ui.label(
            RichText::new("No results found")
                .size(tokens::FONT_SIZE_SM)
                .color(colors.text_muted),
        );
    }

    clicked
}
