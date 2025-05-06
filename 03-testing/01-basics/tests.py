from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert not overlapping_intervals((2, 5), (7, 10))
    assert overlapping_intervals((4,5),(1,7))
    assert overlapping_intervals((3,6),(1,5))
    assert overlapping_intervals((1,5), (4,7))
    assert overlapping_intervals((2,3),(2,3))
    assert not overlapping_intervals((5,6),(2,3))
    assert not overlapping_intervals((0,0), (1,0))