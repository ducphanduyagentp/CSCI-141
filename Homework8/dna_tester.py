"""
Test suite provided to students.
Tests dna module functions and underlying list functions.

There are 8 tests overall.

Test 1: tests constructDnaList and convertDnaListToString
Test 2: tests isPairing (requires working constructDnaList)
Test 3: tests insertListAt (requires working constructDnaList
and convertDnaListToString functions)
Test 4: tests deleteSegment (requires working constructDnaList
and convertDnaListToString functions)
Test 5: tests copySegment (requires working constructDnaList
and convertDnaListToString functions)
Test 6: stress test for insertListAt
Test 7: stress test for deleteSegment
Test 8: stress test for copySegment

Tests 6-8 involve large enough lists to detect inefficient
implementations of the underlying list functions.

File: dna_tester.py
Author: Aaron Deever

"""

import time

from dna_stu import constructDnaList, convertDnaListToString, isPairing
from slList_stu import *


def test1():
    """ tests list construction and conversion back to string"""
    print("Testing constructDnaList and convertDnaListToString")
    dnaList1 = constructDnaList("ATC")
    print(dnaList1.head.data == "A" and
          dnaList1.head.next.data == "T" and
          dnaList1.head.next.next.data == "C" and
          dnaList1.head.next.next.next == None and
          dnaList1.size == 3)

    dnaList2 = createList()
    append(dnaList2, "C")
    append(dnaList2, "G")
    append(dnaList2, "T")
    dnaStr2 = convertDnaListToString(dnaList2)
    print(dnaStr2 == "CGT")

    dnaList3 = constructDnaList("")
    print(dnaList3.head == None)

    dnaStr3 = convertDnaListToString(createList())
    print(dnaStr3 == "")

    print()


def test2():
    """ tests isPairing function"""
    print("Testing isPairing")
    dnaList1 = constructDnaList("")
    dnaList2 = constructDnaList("")
    print(isPairing(dnaList1, dnaList2) == True)

    dnaList1 = constructDnaList("ACTAG")
    dnaList2 = constructDnaList("TGAGT")
    print(isPairing(dnaList1, dnaList2) == False)

    dnaList1 = constructDnaList("CGTACG")
    dnaList2 = constructDnaList("GCAT")
    print(isPairing(dnaList1, dnaList2) == False)

    dnaList1 = constructDnaList("GCTAGCTA")
    dnaList2 = constructDnaList("GCTAGCTA")
    print(isPairing(dnaList1, dnaList2) == False)

    dnaList1 = constructDnaList("AATTCCGG")
    dnaList2 = constructDnaList("TTAAGGCC")
    print(isPairing(dnaList1, dnaList2) == True)

    print()


def test3():
    """ test insertion of a list into another.  Requires
     that constructDnaList and convertDnaListToString are working."""
    print("Testing insertListAt")
    dnaList1 = constructDnaList("AGCT")
    dnaList2 = constructDnaList("TTA")
    try:
        insertListAt(dnaList1, 5, dnaList2)
        print(False)  # failed test if this doesn't raise an error
    except IndexError:
        print(True)  # passed the test if this raised an error

    dnaList1 = constructDnaList("AGCT")
    dnaList2 = constructDnaList("TTA")
    try:
        insertListAt(dnaList1, -1, dnaList2)
        print(False)  # failed test if this doesn't raise an error
    except IndexError:
        print(True)

    dnaList1 = constructDnaList("AGCT")
    dnaList2 = constructDnaList("TTA")
    insertListAt(dnaList1, 0, dnaList2)
    print(convertDnaListToString(dnaList1) == "TTAAGCT")
    print(convertDnaListToString(dnaList2) == "")
    print(dnaList1.size == 7)
    print(dnaList2.size == 0)

    dnaList1 = constructDnaList("AGCT")
    dnaList2 = constructDnaList("TTA")
    insertListAt(dnaList1, 2, dnaList2)
    print(convertDnaListToString(dnaList1) == "AGTTACT")

    dnaList1 = constructDnaList("AGCT")
    dnaList2 = constructDnaList("TTA")
    insertListAt(dnaList1, 4, dnaList2)
    print(convertDnaListToString(dnaList1) == "AGCTTTA")

    dnaList1 = constructDnaList("TTA")
    dnaList2 = constructDnaList("")
    insertListAt(dnaList2, 0, dnaList1)
    print(convertDnaListToString(dnaList2) == "TTA")

    dnaList1 = constructDnaList("AGCT")
    dnaList2 = constructDnaList("")
    insertListAt(dnaList1, 2, dnaList2)
    print(convertDnaListToString(dnaList1) == "AGCT")

    print()


def test4():
    """ test deletion of a segment of a list.  Requires
     that constructDnaList and convertDnaListToString are working."""
    print("Testing deleteSegment")
    dnaList1 = constructDnaList("AGCTAGCTAGCT")
    try:
        deleteSegment(dnaList1, -1, 1)
        print(False)  # failed test if this doesn't raise an error
    except IndexError:
        print(True)  # passed the test if this raised an error

    dnaList1 = constructDnaList("AGCTAGCTAGCT")
    try:
        deleteSegment(dnaList1, 12, 1)
        print(False)  # failed test if this doesn't raise an error
    except IndexError:
        print(True)

    dnaList1 = constructDnaList("AGCTAGCTAGCT")
    try:
        deleteSegment(dnaList1, 4, -2)
        print(False)  # failed test if this doesn't raise an error
    except ValueError:
        print(True)

    dnaList1 = constructDnaList("AGCTAGCTAGCT")
    try:
        deleteSegment(dnaList1, 7, 9)
        print(False)  # failed test if this doesn't raise an error
    except IndexError:
        print(True)

    dnaList1 = constructDnaList("AGCTAGCTAGCT")
    deleteSegment(dnaList1, 4, 0)
    print(convertDnaListToString(dnaList1) == "AGCTAGCTAGCT")

    dnaList1 = constructDnaList("AGCTAGCTAGCT")
    deleteSegment(dnaList1, 0, 3)
    print(convertDnaListToString(dnaList1) == "TAGCTAGCT")

    dnaList1 = constructDnaList("AGCTAGCTAGCT")
    deleteSegment(dnaList1, 2, 2)
    print(convertDnaListToString(dnaList1) == "AGAGCTAGCT")

    dnaList1 = constructDnaList("AGCTAGCTAGCT")
    deleteSegment(dnaList1, 8, 4)
    print(convertDnaListToString(dnaList1) == "AGCTAGCT")

    print()


def test5():
    """ test copying of a segment of a list.  Requires
     that constructDnaList and convertDnaListToString are working."""
    print("Testing copySegment")
    dnaList1 = constructDnaList("AGCTAGCT")
    try:
        copySegment(dnaList1, -1, 1)
        print(False)  # failed test if this doesn't raise an error
    except IndexError:
        print(True)  # passed the test if this raised an error

    dnaList1 = constructDnaList("AGCTAGCT")
    try:
        copySegment(dnaList1, 8, 1)
        print(False)  # failed test if this doesn't raise an error
    except IndexError:
        print(True)

    dnaList1 = constructDnaList("AGCTAGCT")
    try:
        copySegment(dnaList1, 4, -2)
        print(False)  # failed test if this doesn't raise an error
    except ValueError:
        print(True)

    dnaList1 = constructDnaList("AGCTAGCT")
    try:
        copySegment(dnaList1, 5, 6)
        print(False)  # failed test if this doesn't raise an error
    except IndexError:
        print(True)

    dnaList1 = constructDnaList("AGCTAGCT")
    copySegment(dnaList1, 4, 0)
    print(convertDnaListToString(dnaList1) == "AGCTAGCT")

    dnaList1 = constructDnaList("AGCTAGCT")
    copySegment(dnaList1, 0, 3)
    print(convertDnaListToString(dnaList1) == "AGCAGCTAGCT")

    dnaList1 = constructDnaList("AGCAGCTAGCT")
    copySegment(dnaList1, 5, 5)
    print(convertDnaListToString(dnaList1) == "AGCAGCTAGCCTAGCT")

    dnaList1 = constructDnaList("AGCT")
    copySegment(dnaList1, 1, 3)
    print(convertDnaListToString(dnaList1) == "AGCTGCT")

    print()


def test6():
    """ Stress test for insertListAt function.  If the function is
    implemented inefficiently, this test may take a couple
    minutes to complete. If the function is implemented efficiently,
    it will take less than 1 second."""

    print("Stress test for insertListAt function")

    # get lists populated before starting timer
    lst1 = createList()
    for _ in range(100000):
        insertAt(lst1, 0, "A")  # for efficiency, insert at front

    lst2 = createList()
    for _ in range(20000):
        insertAt(lst2, 0, "T")  # for efficiency, insert at front

    print("Should take less than 1 second")

    start_time = time.time()
    # now put lst2 roughly in the middle of lst 1
    insertListAt(lst1, (lst1.size // 2), lst2)
    end_time = time.time()

    print("Took:", end_time - start_time, "seconds")
    print(end_time - start_time < 1)  # should take less than 1 second

    print()


def test7():
    """ Stress test for deleteSegment function.  If the function is
    implemented inefficiently, this test may take a couple
    minutes to complete. If the function is implemented efficiently,
    it will take less than 1 second. """

    print("Stress test for deleteSegment function")

    # don't start timer yet
    lst = createList()
    for _ in range(100000):
        insertAt(lst, 0, "A")

    print("Should take less than 1 second")

    start_time = time.time()
    # delete 20000 elements from middle of 100000 element list
    deleteSegment(lst, (lst.size // 2), 20000)
    end_time = time.time()

    print("Took:", end_time - start_time, "seconds")
    print(end_time - start_time < 1)  # should take less than 1 second

    print()


def test8():
    """ Stress test for copySegment function.  If the function is
    implemented inefficiently, this test may take a couple
    minutes to complete. If the function is implemented efficiently,
    it will take less than 1 second. """

    print("Stress test for copySegment function")

    # don't start timer yet
    lst = createList()
    for _ in range(100000):
        insertAt(lst, 0, "A")

    print("Should take less than 1 second")

    start_time = time.time()
    # copy 10000 elements from middle of 100000 element list
    copySegment(lst, (lst.size // 2), 10000)
    end_time = time.time()

    print("Took:", end_time - start_time, "seconds")
    print(end_time - start_time < 1)  # should take less than 1 second

    print()


def main():
    # comment out tests to restrict testing to certain functions
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    # test7()
    test8()


main()
