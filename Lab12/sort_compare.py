"""
file: sort_compare.py
language: python 3
author: Duc Phan - ddp3945@rit.edu
description: Compare running time of different sorting algorithms
"""

"""
Timing: seconds (s)

Size of list   | 10                     | 100                   | 1000                  | 10000               | 20000               |
---------------|------------------------|-----------------------|-----------------------|---------------------|---------------------|
Insertion Sort | 7.748603820800781e-05  | 0.0027000904083251953 | 0.19127416610717773   | 12.805873394012451  | 62.89388871192932   |
Selection Sort | 5.2928924560546875e-05 | 0.001369476318359375  | 0.05853462219238281   | 5.99941873550415    | 26.71444869041443   |
Heap Sort      | 0.0005838871002197266  | 0.0032377243041992188 | 0.017923355102539062  | 0.2280881404876709  | 0.4761674404144287  |
Merge Sort     | 0.0001201629638671875  | 0.0012657642364501953 | 0.006546497344970703  | 0.10056471824645996 | 0.18768930435180664 |
Quick Sort     | 6.914138793945312e-05  | 0.0005986690521240234 | 0.0027086734771728516 | 0.03392934799194336 | 0.07706403732299805 |
"""

from array_heap import *
import random
import time


def swap(lst, i, j):
    """
    swap: List( A ) * NatNum * NatNum -> NoneType
       where A is totally ordered
       effect: swaps the values in lst at positions i and j
    """
    (lst[i], lst[j]) = (lst[j], lst[i])


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


def insert(lst, mark):
    """
    insert: List( A ) * NatNum -> NoneType
       where A is totally ordered
       effect: moves the value just past the mark to its sorted position
    """
    for index in range(mark, -1, -1):
        if lst[index] > lst[index + 1]:
            swap(lst, index, index + 1)
        else:
            return


def insertionSort(lst):
    """
    insertionSort: List( A ) -> NoneType
       where A is totally ordered
       effect: modifies lst so that the elements are in order
    """
    for mark in range(len(lst) - 1):
        insert(lst, mark)


def split(L):
    """
    split: List( A ) -> Tuple( List( A ), List( A ) )
    """
    evens = []
    odds = []
    isEvenIndex = True
    for e in L:
        if isEvenIndex:
            evens.append(e)
        else:
            odds.append(e)
        isEvenIndex = not isEvenIndex
    return (evens, odds)


def merge(sorted1, sorted2):
    """
    merge: List( A ) * List( A ) -> List( A )
    precondition: sorted1 and sorted2 are lists whose elements are in order
    """
    result = []
    index1 = 0
    index2 = 0
    while index1 < len(sorted1) and index2 < len(sorted2):
        if sorted1[index1] <= sorted2[index2]:
            result.append(sorted1[index1])
            index1 = index1 + 1
        else:
            result.append(sorted2[index2])
            index2 = index2 + 1
    if index1 < len(sorted1):
        result.extend(sorted1[index1:])
    elif index2 < len(sorted2):
        result.extend(sorted2[index2:])
    return result


def mergeSort(L):
    """
    mergeSort: List( A ) -> List( A )
       where A is totally ordered
    """
    if L == []:
        return []
    elif len(L) == 1:
        return L
    else:
        (half1, half2) = split(L)
        return merge(mergeSort(half1), mergeSort(half2))


def partition(pivot, L):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    """
    (less, same, more) = ([], [], [])
    for e in L:
        if e < pivot:
            less.append(e)
        elif e > pivot:
            more.append(e)
        else:
            same.append(e)
    return (less, same, more)


def quickSort(L):
    """
    quickSort: List( A ) -> List( A )
        where A is 'totally ordered'
    """
    if L == []:
        return []
    else:
        pivot = L[0]
        (less, same, more) = partition(pivot, L)
        return quickSort(less) + same + quickSort(more)


def heapSort(lst):
    """
    list(int) -> list(int)
    Implementation for Heap Sort
    """
    heap = createEmptyHeap(len(lst), less)
    for n in lst:
        add(heap, n)
    sortedLst = []
    while heap.size > 0:
        sortedLst.append(removeMin(heap))
    return sortedLst


def test_selection_sort():
    lst = generateRandomList(0, 1000000, random.randint(0, 5000))
    sortedlst = lst[:]
    sortedlst.sort()
    selectionSort(lst)
    print(lst == sortedlst)


def test_insertion_sort():
    lst = generateRandomList(0, 1000000, random.randint(0, 5000))
    sortedlst = lst[:]
    sortedlst.sort()
    insertionSort(lst)
    print(lst == sortedlst)


def test_merge_sort():
    lst = generateRandomList(0, 1000000, random.randint(0, 5000))
    sortedlst = lst[:]
    sortedlst.sort()
    lst = mergeSort(lst)
    print(lst == sortedlst)


def test_quick_sort():
    lst = generateRandomList(0, 1000000, random.randint(0, 5000))
    sortedlst = lst[:]
    sortedlst.sort()
    lst = quickSort(lst)
    print(lst == sortedlst)


def test_heap_sort():
    lst = generateRandomList(0, 1000000, random.randint(0, 5000))
    sortedlst = lst[:]
    sortedlst.sort()
    lst = heapSort(lst)
    print(lst == sortedlst)


def generateRandomList(minval, maxval, size):
    """
    int * int * int -> list(int)
    Generate a random list of integer
    """
    return [random.randint(minval, maxval) for _ in range(size)]


def main():
    minval = int(
        input('What is the min possible value of an item in the list: '))
    maxval = int(
        input('What is the max possible value of an item in the list: '))
    size = int(input('What is the size of the list: '))
    lst = generateRandomList(minval, maxval, size)
    if input('Do you want to display the list? (Y/N) ') == 'Y':
        print('The random list is: {}'.format(lst))

    lst1 = lst[:]
    t = time.time()
    insertionSort(lst1)
    t = time.time() - t
    print('Insertion Sort Time: {} seconds'.format(t))

    lst1 = lst[:]
    t = time.time()
    selectionSort(lst1)
    t = time.time() - t
    print('Selection Sort Time: {} seconds'.format(t))

    lst1 = lst[:]
    t = time.time()
    heapSort(lst1)
    t = time.time() - t
    print('Heap Sort Time: {} seconds'.format(t))

    lst1 = lst[:]
    t = time.time()
    mergeSort(lst1)
    t = time.time() - t
    print('Merge Sort Time: {} seconds'.format(t))

    lst1 = lst[:]
    t = time.time()
    quickSort(lst1)
    t = time.time() - t
    print('Quick Sort Time: {} seconds'.format(t))


if __name__ == '__main__':
    main()
