from typing import List

def filter_list(input_list: List[int]) -> List[int]:
    """
    Filters out elements from the input list based on their position.
    
    This function removes elements located at positions that are multiples of 2 or 3.
    Positions are considered starting from 1, making the first element at position 1.
    The function requires the length of the input list to be a multiple of 10.
    
    Parameters:
    - input_list: List[int] - A list of integers.
    
    Returns:
    - List[int]: A new list with elements filtered out according to the specified criteria.
    
    Raises:
    - ValueError: If the length of the input list is not a multiple of 10.
    """
    if len(input_list) % 10 != 0:
        raise ValueError("Input list length must be a multiple of 10. Received length: {}".format(len(input_list)))
    
    # Efficiently filter the list with comprehension, leveraging the fact that
    # we only need to include elements not at positions multiple of 2 or 3.
    filtered_list = [
        item for index, item in enumerate(input_list, start=1)
        if index % 2 != 0 and index % 3 != 0
    ]
    
    return filtered_list
