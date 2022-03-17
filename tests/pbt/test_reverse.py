from hypothesis import given
from hypothesis.strategies import integers, lists


def reverse(list):
    clone = list.copy()
    clone.reverse()
    return clone


# nonEmptyLists = lists(integers()).filter(lambda l: len(l) > 0)
# nonEmptyLists = lists(integers()).filter(lambda l: bool(l))
nonEmptyLists = lists(integers(), min_size=1)


@given(lists(integers()))
def test_double_reverse_creates_original(original: list[int]):
    # print(original)
    assert reverse(reverse(original)) == original


@given(nonEmptyLists)
def test_reverse_makes_last_first(original: list[int]):
    # print(original)
    reversed_ = reverse(original)
    assert original[-1] == reversed_[0]
