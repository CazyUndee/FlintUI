//! Table component

use egui::*;
use crate::{colors::*, tokens::*};

pub struct Table<'a> {
    headers: Vec<&'a str>,
    rows: Vec<Vec<String>>,
}

impl<'a> Table<'a> {
    pub fn new(headers: impl IntoIterator<Item = &'a str>) -> Self {
        Self { headers: headers.into_iter().collect(), rows: Vec::new() }
    }

    pub fn row(mut self, cells: impl IntoIterator<Item = impl Into<String>>) -> Self {
        self.rows.push(cells.into_iter().map(|s| s.into()).collect());
        self
    }

    pub fn show(&self, ui: &mut Ui) {
        let colors = Colors::default();

        // Render headers
        ui.horizontal(|ui| {
            for header in &self.headers {
                egui::Frame::none()
                    .fill(colors.surface_2)
                    .stroke(egui::Stroke::new(1.0, colors.border))
                    .rounding(Rounding::same(tokens::RADIUS_SM))
                    .inner_margin(vec2(tokens::SPACE_2, tokens::SPACE_1))
                    .show(ui, |ui| {
                        ui.strong(*header);
                    });
            }
        });

        ui.add_space(tokens::SPACE_2);

        // Render rows
        for row in &self.rows {
            ui.horizontal(|ui| {
                for cell in row {
                    egui::Frame::none()
                        .fill(colors.surface)
                        .stroke(egui::Stroke::new(1.0, colors.border))
                        .rounding(Rounding::same(tokens::RADIUS_SM))
                        .inner_margin(vec2(tokens::SPACE_2, tokens::SPACE_1))
                        .show(ui, |ui| {
                            ui.label(cell);
                        });
                }
            });
        }
    }
}
