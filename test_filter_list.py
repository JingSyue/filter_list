import pytest
import time
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
    
def test_empty_list():
    with pytest.raises(ValueError):
        filter_list([])

def test_length_exactly_multiple_of_10():
    input_list = list(range(1, 21))  # 20 is a multiple of 10
    expected = [1, 5, 7, 11, 13, 17, 19]
    assert filter_list(input_list) == expected

def test_length_not_exactly_multiple_of_10_but_more():
    with pytest.raises(ValueError):
        filter_list(list(range(1, 15)))  # Length is 14, more than 10 but not a multiple

def test_negative_and_zero_values():
    input_list = [-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
    expected = [0, 5, 25, 35, 55, 65, 85]
    assert filter_list(input_list) == expected

def test_duplicate_values():
    input_list = [1, 2, 3, 3, 4, 5, 6, 7, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17]
    expected = [1, 5, 7, 11, 13, 17]
    assert filter_list(input_list) == expected

def test_performance_large_list():
    start_time = time.time()
    filter_list(list(range(1, 100001)))  # 100,000 items
    end_time = time.time()
    assert end_time - start_time < 1  


