import pytest

from calculator import sum

def test_sum_of_none():
    assert sum() == 0

def test_sum_of_two():
    assert sum(3, 2) == 5

def test_sum_of_four():
    assert sum(3, 2, 1, 10) == 16

def test_cannot_sum_negative_numbers():
    with pytest.raises(ValueError):
        sum(3, -1)
