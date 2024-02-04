import pytest
import time
from filter_list import filter_list

def test_length_not_multiple_of_10_raises_value_error():
    with pytest.raises(ValueError):
        filter_list([1, 2, 3, 4, 5, 6, 7, 8, 9])

def test_basic_filtering_criteria():
    input_list = list(range(1, 11))  # 1到10
    expected = [1, 5, 7]  
    assert filter_list(input_list) == expected

def test_input_with_non_integer_values_raises_type_error():
    with pytest.raises(TypeError):
        filter_list([1, 2, 'a', 4, 5, 6, 7, 8, 9, 10])

def test_performance_large_list():
    start_time = time.time()
    filter_list(list(range(1, 100001)))  # 100,000个元素
    end_time = time.time()
    assert end_time - start_time < 1  
