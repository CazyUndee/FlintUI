//! Command palette component

use egui::*;
use crate::{colors::*, tokens::*};

pub struct CommandItem {
    pub title: String,
    pub subtitle: Option<String>,
    pub kbd: Option<String>,
}

impl CommandItem {
    pub fn new(title: impl Into<String>) -> Self {
        Self { title: title.into(), subtitle: None, kbd: None }
    }

    pub fn subtitle(mut self, subtitle: impl Into<String>) -> Self {
        self.subtitle = Some(subtitle.into());
        self
    }

    pub fn kbd(mut self, kbd: impl Into<String>) -> Self {
        self.kbd = Some(kbd.into());
        self
    }
}

pub struct CommandPalette {
    pub items: Vec<CommandItem>,
    pub query: String,
    pub open: bool,
    pub selected_index: usize,
    id: Id,
}

impl CommandPalette {
    pub fn new(id: impl Into<Id>) -> Self {
        Self { items: Vec::new(), query: String::new(), open: false, selected_index: 0, id: id.into() }
    }

    pub fn item(mut self, item: CommandItem) -> Self {
        self.items.push(item);
        self
    }

    pub fn set_items(&mut self, items: Vec<CommandItem>) {
        self.items = items;
    }

    pub fn open(&mut self) {
        self.open = true;
        self.query.clear();
        self.selected_index = 0;
    }

    pub fn close(&mut self) {
        self.open = false;
        self.query.clear();
        self.selected_index = 0;
    }

    pub fn toggle(&mut self) {
        if self.open {
            self.close();
        } else {
            self.open();
        }
    }

    pub fn filter(&self) -> Vec<&CommandItem> {
        if self.query.is_empty() {
            return self.items.iter().collect();
        }
        self.items
            .iter()
            .filter(|item| item.title.to_lowercase().contains(&self.query.to_lowercase()))
            .collect()
    }

    /// Render the command palette as a modal dialog
    /// Returns the index of the selected command (into the filtered list)
    pub fn show(&mut self, ctx: &egui::Context) -> Option<usize> {
        if !self.open {
            return None;
        }

        let colors = Colors::default();
        let mut result = None;

        // Modal backdrop
        egui::Area::new(self.id.with("backdrop"))
            .order(Order::Foreground)
            .interactable(true)
            .show(ctx, |ui| {
                let screen_size = ctx.screen_rect().size();
                ui.set_min_size(screen_size);

                // Semi-transparent backdrop
                let painter = ui.painter_at(ui.max_rect());
                painter.rect_filled(
                    ui.max_rect(),
                    Rounding::ZERO,
                    Color32::from_black_alpha(150),
                );

                // Command palette panel centered on screen
                let panel_width = 500.0;
                let panel_height = 400.0;

                egui::Frame::none()
                    .fill(colors.surface)
                    .stroke(egui::Stroke::new(1.0, colors.border))
                    .rounding(Rounding::same(tokens::RADIUS_LG))
                    .shadow(egui::Shadow {
                        offset: [0.0, 8.0].into(),
                        blur: 24.0,
                        spread: 0.0,
                        color: Color32::from_black_alpha(100),
                    })
                    .show(ui, |ui| {
                        ui.set_min_size(vec2(panel_width, panel_height));

                        // Search input at top
                        ui.horizontal(|ui| {
                            ui.label("⌘");
                            let response = ui.add(
                                TextEdit::singleline(&mut self.query)
                                    .hint_text("Type a command...")
                                    .desired_width(f32::INFINITY)
                                    .font(FontId::new(tokens::FONT_SIZE_BASE, FontFamily::Proportional)),
                            );

                            if response.has_focus() {
                                // Handle keyboard navigation
                                if ui.input(|i| i.key_pressed(Key::ArrowDown)) {
                                    let filtered = self.filter();
                                    if !filtered.is_empty() {
                                        self.selected_index = (self.selected_index + 1) % filtered.len();
                                    }
                                }
                                if ui.input(|i| i.key_pressed(Key::ArrowUp)) {
                                    let filtered = self.filter();
                                    if !filtered.is_empty() {
                                        self.selected_index = if self.selected_index == 0 {
                                            filtered.len() - 1
                                        } else {
                                            self.selected_index - 1
                                        };
                                    }
                                }
                                if ui.input(|i| i.key_pressed(Key::Enter)) {
                                    result = Some(self.selected_index);
                                }
                                if ui.input(|i| i.key_pressed(Key::Escape)) {
                                    self.close();
                                }
                            }
                        });

                        ui.add_space(SPACE_2);

                        // Separator
                        ui.separator();

                        ui.add_space(SPACE_2);

                        // Command list
                        let filtered = self.filter();
                        if !filtered.is_empty() {
                            // Ensure selected_index is valid
                            if self.selected_index >= filtered.len() {
                                self.selected_index = 0;
                            }

                            egui::ScrollArea::vertical()
                                .max_height(280.0)
                                .show(ui, |ui| {
                                    for (idx, item) in filtered.iter().enumerate() {
                                        let is_selected = idx == self.selected_index;

                                        let response = ui.horizontal(|ui| {
                                            if is_selected {
                                                ui.label(
                                                    RichText::new("→")
                                                        .size(tokens::FONT_SIZE_BASE)
                                                        .color(colors.accent_text),
                                                );
                                            } else {
                                                ui.add_space(SPACE_4);
                                            }

                                            ui.label(
                                                RichText::new(&item.title)
                                                    .size(tokens::FONT_SIZE_BASE)
                                                    .color(if is_selected { colors.accent_text } else { colors.text }),
                                            );

                                            if let Some(subtitle) = &item.subtitle {
                                                ui.label(
                                                    RichText::new(subtitle)
                                                        .size(tokens::FONT_SIZE_SM)
                                                        .color(colors.text_muted),
                                                );
                                            }

                                            if let Some(kbd) = &item.kbd {
                                                ui.with_layout(egui::Layout::right_to_left(Align::Center), |ui| {
                                                    egui::Frame::none()
                                                        .fill(colors.surface_3)
                                                        .stroke(egui::Stroke::new(1.0, colors.border))
                                                        .rounding(Rounding::same(tokens::RADIUS_SM))
                                                        .inner_margin(vec2(SPACE_2, SPACE_1))
                                                        .show(ui, |ui| {
                                                            ui.label(
                                                                RichText::new(kbd)
                                                                    .size(tokens::FONT_SIZE_XS)
                                                                    .color(colors.text_muted)
                                                                    .font(FontFamily::Monospace),
                                                            );
                                                        });
                                                });
                                            }
                                        });

                                        if response.response.clicked() {
                                            result = Some(idx);
                                        }
                                    }
                                });
                        } else if !self.query.is_empty() {
                            ui.centered_and_justified(|ui| {
                                ui.label(
                                    RichText::new("No commands found")
                                        .size(tokens::FONT_SIZE_SM)
                                        .color(colors.text_muted),
                                );
                            });
                        }
                    });
            });

        if result.is_some() {
            self.close();
        }

        result
    }
}

impl Default for CommandPalette {
    fn default() -> Self {
        Self::new("default_command_palette")
    }
}
