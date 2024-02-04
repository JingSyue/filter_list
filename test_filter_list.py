import pytest
from filter_list import filter_list

def test_length_not_multiple_of_10():
    with pytest.raises(ValueError):
        filter_list([1, 2, 3])

def test_filtering_criteria():
    assert filter_list(list(range(1, 11))) == [1, 5, 7]

def test_large_list():
    input_list = list(range(1, 101))
    expected = [x for x in input_list if x % 2 != 0 and x % 3 != 0]
    assert filter_list(input_list) == expected
