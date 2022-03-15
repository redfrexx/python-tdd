from calculator import sum

def test_sum():
    assert sum(3, 2) == 5

def test_sum_three_values():
    assert sum(3, 2, 1) == 6
