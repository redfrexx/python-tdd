# Develop a function to sum up an unknown number of non-negative numbers:
# - no numbers
# - single number
# - several numbers
# - decimals
# - negative number -> Error

import pytest

from calculator import sum_up


def test_sum_of_none():
    """No numbers sum up to 0"""
    assert sum_up() == 0


def test_sum_of_single_number():
    """Single number sums up to itself"""
    assert sum_up(42) == 42


def test_sum_of_several_numbers():
    """Several numbers can be summed up"""
    assert sum_up(3, 2) == 5
    assert sum_up(3, 2, 1, 10) == 16


def test_sum_of_decimals():
    """Decimal numbers can be summed up"""
    # assert sum_up(3.1, 5.9, 9.01, 0.04) == 18.05 # Fails due to floating point rounding errors
    assert sum_up(3.1, 5.9, 9.01, 0.04) == pytest.approx(18.05)


def test_cannot_sum_negative_numbers():
    """Negative number lead to ValueError"""
    with pytest.raises(ValueError):
        sum_up(3, -1)
