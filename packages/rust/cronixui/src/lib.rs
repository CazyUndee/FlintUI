//! CronixUI - A dark-themed UI toolkit with crimson accents and Outfit typography
//!
//! ## Example
//!
//! ```rust
//! use cronixui::{Toast, Toggle, Modal};
//!
//! // Create a toast
//! let toast = Toast::success("Operation completed!");
//!
//! // Create a toggle
//! let mut toggle = Toggle::new();
//! toggle.toggle();
//! assert!(toggle.is_on());
//! ```

pub const VERSION: &str = "1.0.4";

mod toast;
mod toggle;
mod modal;
mod dropdown;
mod tabs;
mod accordion;
mod pagination;
mod command_palette;
mod search;

pub use toast::{Toast, ToastType};
pub use toggle::Toggle;
pub use modal::Modal;
pub use dropdown::Dropdown;
pub use tabs::Tabs;
pub use accordion::Accordion;
pub use pagination::Pagination;
pub use command_palette::{CommandPalette, CommandPaletteItem};
pub use search::{Search, SearchItem};

/// Initialize CronixUI
pub fn init() {
    println!("CronixUI {} initialized", VERSION);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_toggle() {
        let mut toggle = Toggle::new();
        assert!(!toggle.is_on());
        toggle.toggle();
        assert!(toggle.is_on());
        toggle.set_on(false);
        assert!(!toggle.is_on());
    }

    #[test]
    fn test_pagination() {
        let mut pagination = Pagination::new(10, 1);
        assert_eq!(pagination.current(), 1);
        pagination.next();
        assert_eq!(pagination.current(), 2);
        pagination.go_to(5);
        assert_eq!(pagination.current(), 5);
    }

    #[test]
    fn test_search() {
        let mut search = Search::new();
        search.set_items(vec![
            SearchItem::new("Apple"),
            SearchItem::new("Banana"),
            SearchItem::new("Apricot"),
        ]);
        let results = search.filter("ap");
        assert_eq!(results.len(), 2);
    }
}
