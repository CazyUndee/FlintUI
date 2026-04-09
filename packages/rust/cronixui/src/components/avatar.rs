//! Avatar component

use egui::*;
use crate::{colors::*, tokens::*};

pub struct Avatar {
    pub initials: String,
    pub size: AvatarSize,
}

#[derive(Clone, Copy)]
pub enum AvatarSize {
    SM,
    MD,
    LG,
    XL,
}

impl AvatarSize {
    pub fn diameter(&self) -> f32 {
        match self {
            AvatarSize::SM => 24.0,
            AvatarSize::MD => 32.0,
            AvatarSize::LG => 40.0,
            AvatarSize::XL => 56.0,
        }
    }

    pub fn font_size(&self) -> f32 {
        match self {
            AvatarSize::SM => 10.0,
            AvatarSize::MD => 12.0,
            AvatarSize::LG => 14.0,
            AvatarSize::XL => 18.0,
        }
    }
}

impl Avatar {
    pub fn new(initials: impl Into<String>) -> Self {
        Self {
            initials: initials.into(),
            size: AvatarSize::MD,
        }
    }

    pub fn size(mut self, size: AvatarSize) -> Self {
        self.size = size;
        self
    }

    pub fn show(&self, ui: &mut Ui) -> Response {
        let colors = Colors::default();
        let diameter = self.size.diameter();
        let font_size = self.size.font_size();
        let radius = diameter / 2.0;

        let (rect, response) = ui.allocate_exact_size(vec2(diameter, diameter), Sense::hover());

        // Draw background circle
        ui.painter().circle_filled(
            rect.center(),
            radius,
            colors.accent,
        );

        // Draw border
        ui.painter().circle_stroke(
            rect.center(),
            radius,
            Stroke::new(1.0, colors.border),
        );

        // Draw initials text
        ui.painter().text(
            rect.center(),
            Align2::CENTER_CENTER,
            &self.initials,
            FontId::new(font_size, FontFamily::Proportional),
            colors.accent_text,
        );

        response
    }
}
