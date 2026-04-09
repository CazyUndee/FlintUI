//! Dropdown component

use egui::*;
use crate::{colors::*, tokens::*};

/// Dropdown component with full rendering
pub struct Dropdown {
    pub items: Vec<String>,
    pub selected: Option<usize>,
    pub open: bool,
    id: Id,
}

impl Dropdown {
    pub fn new(id: impl Into<Id>, items: impl IntoIterator<Item = impl Into<String>>) -> Self {
        Self {
            id: id.into(),
            items: items.into_iter().map(|s| s.into()).collect(),
            selected: None,
            open: false,
        }
    }

    pub fn selected(mut self, index: usize) -> Self {
        if index < self.items.len() {
            self.selected = Some(index);
        }
        self
    }

    pub fn select(&mut self, index: usize) {
        if index < self.items.len() {
            self.selected = Some(index);
        }
    }

    pub fn toggle(&mut self) {
        self.open = !self.open;
    }

    pub fn close(&mut self) {
        self.open = false;
    }

    pub fn selected_text(&self) -> Option<&str> {
        self.selected.map(|i| self.items[i].as_str())
    }

    /// Render the dropdown trigger button and popup.
    /// Returns Some(index) when an item is selected.
    pub fn show(&mut self, ui: &mut Ui) -> Option<usize> {
        let colors = Colors::default();
        let label = self.selected_text().unwrap_or("Select an option...");

        let response = ui.add_sized(
            [ui.available_width(), 28.0],
            egui::Button::new(label)
                .fill(colors.surface_2)
                .stroke(egui::Stroke::new(1.0, colors.border))
                .rounding(Rounding::same(tokens::RADIUS)),
        );

        if response.clicked() {
            self.open = !self.open;
        }

        // Sync open state with egui memory
        if self.open {
            ui.memory_mut(|mem| mem.open_popup(self.id));
        } else {
            ui.memory_mut(|mem| mem.close_popup());
        }

        if !self.open {
            return None;
        }

        let items = &self.items;
        let selected = self.selected;
        let popup_id = self.id;

        egui::popup::popup_below_widget(ui, popup_id, &response, |ui| {
            // popup_below_widget already wraps in Frame::popup
            // Customize the style colors for our theme
            for (i, item) in items.iter().enumerate() {
                let is_selected = selected == Some(i);
                let text = if is_selected {
                    format!("✓ {}", item)
                } else {
                    item.clone()
                };

                if ui.selectable_label(is_selected, text).clicked() {
                    ui.memory_mut(|m| {
                        m.data.insert_temp(popup_id.with("chosen"), Some(i));
                        m.close_popup();
                    });
                }
            }
        });

        // Check if popup is still open
        let still_open = ui.memory(|mem| mem.is_popup_open(popup_id));
        if !still_open {
            self.open = false;
            let chosen = ui.memory_mut(|m| m.data.get_temp::<usize>(popup_id.with("chosen")));
            if let Some(idx) = chosen {
                self.selected = Some(idx);
                ui.memory_mut(|m| m.data.remove::<usize>(popup_id.with("chosen")));
                return Some(idx);
            }
        }

        // Also check result for chosen item stored in memory
        let chosen = ui.memory_mut(|m| m.data.get_temp::<usize>(popup_id.with("chosen")));
        if let Some(idx) = chosen {
            self.selected = Some(idx);
            self.open = false;
            ui.memory_mut(|m| m.data.remove::<usize>(popup_id.with("chosen")));
            return Some(idx);
        }

        None
    }
}

/// Functional dropdown helper
pub fn dropdown(ui: &mut Ui, id: impl Into<Id>, items: &[String], selected: &mut Option<usize>) {
    let colors = Colors::default();
    let popup_id = id.into();

    let label = selected
        .and_then(|i| items.get(i))
        .map(|s| s.as_str())
        .unwrap_or("Select an option...");

    let response = ui.add_sized(
        [ui.available_width(), 28.0],
        egui::Button::new(label)
            .fill(colors.surface_2)
            .stroke(egui::Stroke::new(1.0, colors.border))
            .rounding(Rounding::same(tokens::RADIUS)),
    );

    if response.clicked() {
        ui.memory_mut(|mem| {
            if mem.is_popup_open(popup_id) {
                mem.close_popup();
            } else {
                mem.open_popup(popup_id);
            }
        });
    }

    let is_open = ui.memory(|mem| mem.is_popup_open(popup_id));

    if is_open {
        let current_selected = *selected;
        egui::popup::popup_below_widget(ui, popup_id, &response, |ui| {
            for (i, item) in items.iter().enumerate() {
                let is_sel = current_selected == Some(i);
                let text = if is_sel { format!("✓ {}", item) } else { item.clone() };
                if ui.selectable_label(is_sel, text).clicked() {
                    ui.memory_mut(|m| {
                        m.data.insert_temp(popup_id.with("result"), i);
                        m.close_popup();
                    });
                }
            }
        });

        // Check result
        let result = ui.memory_mut(|m| m.data.get_temp::<usize>(popup_id.with("result")));
        if let Some(idx) = result {
            *selected = Some(idx);
            ui.memory_mut(|m| m.data.remove::<usize>(popup_id.with("result")));
        }
    }
}
