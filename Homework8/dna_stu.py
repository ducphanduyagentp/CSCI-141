"""
Program with three basic DNA functions that are used in
conjunction with a test function for homework.

File: dna_stu.py
Author: Aaron Deever
Author: Duc Phan - ddp3945@rit.edu
"""

from slList_stu import *


def constructDnaList(dnaString):
    """
    Given a DNA string, converts it into a list in which
    each character is a node.
    :param dnaString: string of DNA
    :return: dna string as a list
    """

    # PUT YOUR IMPLEMENTATION HERE
    lst = createList()
    for c in dnaString:
        append(lst, c)
    return lst


def convertDnaListToString(lst):
    """
    Given a dna string in list form, convert back to string
    :param lst: dna list
    :return: dna as string
    """

    # PUT YOUR IMPLEMENTATION HERE
    curr = lst.head
    s = ''
    while curr != None:
        s += str(curr.data)
        curr = curr.next
    return s


def isPairing(lst1, lst2):
    """
    tests if the two strings are dna complementary base pairs.
    A must match with T, G with C.  Strings must be same length too.
    :param lst1: first dna list
    :param lst2: second dna list
    :return: boolean True if match, False else
    """

    # PUT YOUR IMPLEMENTATION HERE
    if lst1.size != lst2.size:
        return False

    curr1 = lst1.head
    curr2 = lst2.head
    while curr1 != None and curr2 != None:
        if curr1.data == 'A' and curr2.data != 'T':
            return False
        elif curr1.data == 'T' and curr2.data != 'A':
            return False
        elif curr1.data == 'G' and curr2.data != 'C':
            return False
        elif curr1.data == 'C' and curr2.data != 'G':
            return False
        curr1 = curr1.next
        curr2 = curr2.next

    return True
