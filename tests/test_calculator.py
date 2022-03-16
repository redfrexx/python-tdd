# Develop a function sum() to add up an unknown number of non-negative numbers:
# - no numbers
# - single number
# - several numbers
# - decimals
# - negative number -> Error

import pytest

from calculator import sum


def test_sum_of_none():
    """No numbers sum up to 0"""
    assert sum() == 0


def test_sum_of_single_number():
    """Single number sums up to itself"""
    assert sum(42) == 42


def test_sum_of_several_numbers():
    """Several numbers can be summed up"""
    assert sum(3, 2) == 5
    assert sum(3, 2, 1, 10) == 16


def test_sum_of_decimals():
    """Decimal numbers can be summed up"""
    assert sum(3.1, 4.2, 100.01) == 107.31


def test_cannot_sum_negative_numbers():
    """Negative number lead to ValueError"""
    with pytest.raises(ValueError):
        sum(3, -1)
