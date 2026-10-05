"""Tests for the index module."""

from index import add


def test_add():
    """add() should return the sum of two numbers."""
    assert add(2, 3) == 5
