//! Skeleton loading placeholder

use egui::*;

use crate::{colors::*, tokens::*};

pub struct Skeleton {
    pub width: f32,
    pub height: f32,
    pub variant: SkeletonVariant,
}

#[derive(Clone, Copy)]
pub enum SkeletonVariant {
    Text,
    Title,
    Avatar,
    Block,
}

impl Skeleton {
    pub fn text() -> Self {
        Self { width: 100.0, height: 14.0, variant: SkeletonVariant::Text }
    }

    pub fn title() -> Self {
        Self { width: 150.0, height: 20.0, variant: SkeletonVariant::Title }
    }

    pub fn avatar() -> Self {
        Self { width: 40.0, height: 40.0, variant: SkeletonVariant::Avatar }
    }

    pub fn block(width: f32, height: f32) -> Self {
        Self { width, height, variant: SkeletonVariant::Block }
    }

    pub fn width(mut self, width: f32) -> Self {
        self.width = width;
        self
    }

    pub fn height(mut self, height: f32) -> Self {
        self.height = height;
        self
    }

    pub fn show(&self, ui: &mut Ui) -> Response {
        let colors = Colors::default();

        let rounding = match self.variant {
            SkeletonVariant::Avatar => Rounding::same(self.width / 2.0),
            SkeletonVariant::Block => Rounding::same(tokens::RADIUS),
            _ => Rounding::same(tokens::RADIUS_SM),
        };

        let (rect, response) = ui.allocate_at_least(vec2(self.width, self.height), Sense::hover());
        ui.painter().rect_filled(rect, rounding, colors.surface_3);
        ui.painter().rect_stroke(rect, rounding, Stroke::new(1.0, colors.border));

        response
    }
}
