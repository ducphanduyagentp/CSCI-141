"""
file: selectionsort.py
language: python3
author: Duc Duy Phan - ddp3945@rit.edu
description: Homework 5 - Selection Sort

Questions:
1. In case the input is a sorted list in non-decreasing order, insertion sort will perform
    better than selection sort.
    For example: [-1, 0, 1, 2, 3, 4, 5, 10, 12]

2. The reason why selection sort performs worse than insertion sort in this test case is that:
    - Both of these sorting algorithm using 2 loops. The first loop is used to
    iterate through every elements of the list

    - The difference is in the second loop of each algorithm:

        + The inserting operation in insertion sort (which uses the second loop) will stop swapping
        and iterating if the immediate preceding element is smaller than or equal to the current element.
        In this test case or a sorted list, for every i-th element in the list, the (i-1)-th element
        is already smaller than the i-th element. Therefore, there is no insertion needed in the second loop.
        The time complexity of insertion sort for a n-element sorted list is O(n)

        + The selecting operation in selection sort will always find the smallest element in
        the subsequence that it has not iterated thorugh. The behavior of selection sort for
        every kind of input is the same.
        In this test case, in the iteration process, the current i-th element is always the
        smallest element in the subsequence from i-th to (n-1)-th (inclusive),
        but selection sort still needs to iterate through that sequence as a default behavior.
        The time complexity of selection sort in this case is O(n^2)
"""


def swap(lst, i, j):
    """ Swap the i-th and j-th element of the list lst """
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp


def findMinFrom(lst, mark):
    """ Find and return the index of the smallest element in the list lst
    from index mark to the end of the list """
    iMin = mark
    for i in range(mark + 1, len(lst)):
        if lst[i] < lst[iMin]:
            iMin = i
    return iMin


def selectionSort(lst):
    """ Implementation of Selection sort """
    for i in range(len(lst) - 1):
        iMin = findMinFrom(lst, i)
        swap(lst, i, iMin)

    return lst


def main():
    """
    - Prompt users for a filename
    - Read the integers from the file to a list
    - Print the provided list of integers
    - Use selection sort to sort the list and print the sorted list
    """
    lst = []
    filename = input('Please input the file name: ')
    for x in open(filename):
        lst.append(int(x))
    print(lst)
    print(selectionSort(lst))


main()
