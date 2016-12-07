import random
import time

def createRandomList(min, max, size):
    return [random.randint(min, max) for _ in range(size)]

def timingIteration(lst):
    start = time.time()
    for c in lst:
        pass
    return time.time() - start

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
    lst = createRandomList(-100, 100, 1401)
    start = time.time()
    lst = selectionSort(lst)
    print(time.time() - start)

main()
