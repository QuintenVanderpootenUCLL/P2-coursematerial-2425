import mergesort
import pytest
import random

@pytest.mark.parametrize("n", range(101))
def test_split_in_two(n):
    lst = random.sample(range(1000), n)
    left, right = mergesort.split_in_two(lst)
    assert left + right == lst

    assert abs(len(left) - len(right)) <= 1


