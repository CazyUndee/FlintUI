//! File input component

use egui::*;
use crate::{colors::*, tokens::*};

pub struct FileInput {
    pub accept: String,
    pub multiple: bool,
    pub files: Vec<String>,
}

impl FileInput {
    pub fn new() -> Self {
        Self { accept: String::new(), multiple: false, files: Vec::new() }
    }

    pub fn accept(mut self, accept: impl Into<String>) -> Self {
        self.accept = accept.into();
        self
    }

    pub fn multiple(mut self) -> Self {
        self.multiple = true;
        self
    }

    pub fn show(&mut self, ui: &mut Ui) -> Response {
        let colors = Colors::default();

        egui::Frame::none()
            .fill(colors.surface)
            .stroke(egui::Stroke::new(1.0, colors.border))
            .rounding(Rounding::same(tokens::RADIUS))
            .inner_margin(tokens::SPACE_4)
            .show(ui, |ui| {
                ui.vertical(|ui| {
                    ui.label(
                        RichText::new("📁 Drop files here or click to browse")
                            .size(tokens::FONT_SIZE_BASE)
                            .color(colors.text_muted),
                    );

                    if ui.button_primary("Browse files").clicked() {
                        // Note: actual file selection requires platform-specific code
                        // This is a UI placeholder
                    }

                    if !self.files.is_empty() {
                        ui.add_space(tokens::SPACE_2);
                        ui.separator();
                        ui.add_space(tokens::SPACE_2);

                        for file in &self.files {
                            ui.horizontal(|ui| {
                                ui.label("📄");
                                ui.label(
                                    RichText::new(file)
                                        .size(tokens::FONT_SIZE_SM)
                                        .color(colors.text),
                                );
                            });
                        }
                    }
                });
            })
            .response
    }
}

impl Default for FileInput {
    fn default() -> Self {
        Self::new()
    }
}
