# Develop a function sum() to add up an unknown number of non-negative numbers:
# - no numbers
# - single number
# - several numbers
# - decimals
# - negative number -> Error

import pytest

from calculator import sum

def test_sum_of_none():
    assert sum() == 0

def test_sum_of_two():
    assert sum(3, 2) == 5

def test_sum_of_four():
    assert sum(3, 2, 1, 10) == 16

def test_sum_of_decimals():
    assert sum(3.1, 4.2, 100.01) == 107.31

def test_cannot_sum_negative_numbers():
    with pytest.raises(ValueError):
        sum(3, -1)
