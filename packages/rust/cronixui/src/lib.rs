//! CronixUI - A dark-themed UI toolkit for egui
//!
//! ## Example
//!
//! ```rust
//! use cronixui::{CronixUI, Colors, components::*};
//!
//! // In your egui app
//! fn update(&mut self, ctx: &egui::Context) {
//!     CronixUI::apply_theme(ctx);
//!     
//!     egui::CentralPanel::default().show(ctx, |ui| {
//!         // Use components
//!         if ui.button_primary("Click me").clicked() {
//!             // handle click
//!         }
//!     });
//! }
//! ```

pub mod colors;
pub mod tokens;
pub mod components;

pub use colors::*;
pub use tokens::*;
pub use components::*;

use egui::{Color32, Vec2, Rounding};

/// Current version
pub const VERSION: &str = "1.0.6";

/// Apply CronixUI theme to egui context
pub fn apply_theme(ctx: &egui::Context) {
    let colors = Colors::default();
    
    let mut style = (*ctx.style()).clone();
    
    // Visuals
    style.visuals.window_fill = colors.bg;
    style.visuals.panel_fill = colors.bg;
    style.visuals.extreme_bg_color = colors.surface;
    style.visuals.faint_bg_color = colors.surface_2;
    style.visuals.code_bg_color = colors.surface_3;
    
    // Text colors
    style.visuals.strong_text_color = colors.text;
    style.visuals.weak_text_color = colors.text_muted;
    style.visuals.text_color = colors.text;
    
    // Widget colors
    style.visuals.widgets.noninteractive.bg_fill = colors.surface;
    style.visuals.widgets.noninteractive.bg_stroke.color = colors.border;
    style.visuals.widgets.noninteractive.fg_stroke.color = colors.text;
    
    style.visuals.widgets.inactive.bg_fill = colors.surface_2;
    style.visuals.widgets.inactive.bg_stroke.color = colors.border;
    style.visuals.widgets.inactive.fg_stroke.color = colors.text;
    
    style.visuals.widgets.hovered.bg_fill = colors.surface_3;
    style.visuals.widgets.hovered.bg_stroke.color = colors.border_hover;
    style.visuals.widgets.hovered.fg_stroke.color = colors.text;
    
    style.visuals.widgets.active.bg_fill = colors.accent;
    style.visuals.widgets.active.bg_stroke.color = colors.accent;
    style.visuals.widgets.active.fg_stroke.color = colors.text;
    
    style.visuals.widgets.open.bg_fill = colors.surface_3;
    style.visuals.widgets.open.bg_stroke.color = colors.accent;
    
    // Selection
    style.visuals.selection.bg_fill = colors.accent;
    style.visuals.selection.stroke.color = colors.accent_text;
    
    // Hyperlink
    style.visuals.hyperlink_color = colors.accent_text;
    
    // Button rounding
    style.visuals.button_rounding = Rounding::same(tokens::RADIUS);
    
    // Window rounding
    style.visuals.window_rounding = Rounding::same(tokens::RADIUS_LG);
    
    // Spacing
    style.spacing.button_padding = Vec2::new(tokens::SPACE_4, tokens::SPACE_2);
    style.spacing.item_spacing = Vec2::new(tokens::SPACE_2, tokens::SPACE_2);
    style.spacing.indent = tokens::SPACE_4;
    
    ctx.set_style(style);
}

/// Helper trait for CronixUI button variants
pub trait CronixButton {
    fn button_primary(&mut self, text: &str) -> egui::Response;
    fn button_danger(&mut self, text: &str) -> egui::Response;
    fn button_success(&mut self, text: &str) -> egui::Response;
    fn button_ghost(&mut self, text: &str) -> egui::Response;
    fn button_outline(&mut self, text: &str) -> egui::Response;
}

impl CronixButton for egui::Ui {
    fn button_primary(&mut self, text: &str) -> egui::Response {
        let colors = Colors::default();
        self.add(egui::Button::new(text).fill(colors.accent))
    }
    
    fn button_danger(&mut self, text: &str) -> egui::Response {
        let colors = Colors::default();
        self.add(egui::Button::new(text).fill(colors.error))
    }
    
    fn button_success(&mut self, text: &str) -> egui::Response {
        let colors = Colors::default();
        self.add(egui::Button::new(text).fill(colors.success))
    }
    
    fn button_ghost(&mut self, text: &str) -> egui::Response {
        self.add(egui::Button::new(text).fill(Color32::TRANSPARENT))
    }
    
    fn button_outline(&mut self, text: &str) -> egui::Response {
        let colors = Colors::default();
        self.add(egui::Button::new(text)
            .fill(Color32::TRANSPARENT)
            .stroke(egui::Stroke::new(1.0, colors.border)))
    }
}
