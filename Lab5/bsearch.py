"""
file: bsearch.py
language: python 3
Demonstrate the recursive binary search algorithm.
author: Sean Strout (sps@cs.rit.edu)
contributor: Trudy Howles tmh 
contributor: ben k steele bks 
contributor: Arthur Nunes-Harwitt anh
contributor: Duc Duy Phan - ddp3945@rit.edu
Modification History:
10/8/2010 -- lecture content reordering 
01/13/2011 -- docstring content revisions
08/28/2012 -- Sentinel changed to None
10/02/2016 -- Source code modified for lab assignment #5
"""


def binary_search(data, target, start, end):
    """
    binary_search : List(Orderable) Orderable NatNum NatNum -> NatNum or NoneType
    Perform a binary search for a target value between start and end indices.
    Parameters:
        data - a list of sorted data
        target - the target value to search for
        start - the starting index in data that is part of this search
        end - the ending index in data that is part of this search
    Returns:
        index of target in data, if present; otherwise None.
    """

    # base condition - terminate when start passes end index
    if start > end:
        return None

    # find the middle value between start and end indices
    mid_index = (start + end) // 2
    mid_value = data[mid_index][:len(target)]

    if target == mid_value:
        return mid_index
    elif target < mid_value:
        return binary_search(data, target, start, mid_index - 1)
    else:
        return binary_search(data, target, mid_index + 1, end)


def get_index(data, target):
    """
    get_index : List(Orderable) Orderable -> NatNum or NoneType
    get_index returns the index of target in data or None if not target found.
    Parameters:
        data - a list of sorted data
        target - the target value to search for
    Returns:
        The index of the target element in data, if it is present,
        otherwise None.
    """

    # search for the target across all elements in data
    return binary_search(data, target, 0, len(data) - 1)
