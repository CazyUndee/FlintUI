#[cfg(test)]
use crate::{add, multiply};

#[test]
fn test_add() {
    assert_eq!(add(2, 3), 5);
}

#[test]
fn test_multiply() {
    assert_eq!(multiply(2, 3), 6);
}
