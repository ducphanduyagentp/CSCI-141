"""
File: slList_stu.py
Purpose: rit_lib-based singly-linked list for CS141 LECTURE.
Author: ben k steele <bks@cs.rit.edu>
Author: sean strout <sps@cs.rit.edu>
Author: duc phan <ddp3945@rit.edu>
Language: Python 3
Description: Implementation of a singly-linked list data structure.
"""

from myNode import *
from rit_lib import *


###########################################################
# LINKED LIST CLASS DEFINITION                                
###########################################################

class SlList(struct):
    """
    SlList class encapsulates a node-based linked list.
    'head' slot refers to a Node instance.
    'size' slot holds the number of nodes in the list.
    'cursor' slot refers to a Node instance.
    """
    _slots = (((Node, NoneType), 'head') \
                  , (int, 'size') \
                  , ((Node, NoneType), 'cursor'))


###########################################################
# LINKED LIST CLASS CONSTRUCTOR                                
###########################################################

def createList():
    """
       Create and return an instance
       of an empty node-based, sin-linked list.
       Parameters:
           None
       Returns: 
           An empty list
    """
    return SlList(None, 0, None)


###########################################################
# CURSOR FUNCTIONS                                
###########################################################

def reset(lst):
    """
    Resets the cursor to the start of the list
    
    Parameters:
        lst (SlList) - the linked list
    Returns:
        None
    """

    lst.cursor = lst.head


def hasNext(lst):
    """
    Returns True if the list has more elements.
    
    Parameters:
        lst (SlList) - the linked list
    Returns:
        True (bool) if the cursor refers to a valid Node
    """

    return not lst.cursor == None


def next(lst):
    """
    Returns the next element in the iteration.
    
    Parameters:
        lst (SlList) - the linked list
    Preconditions:
        If cursor is invalid, raises an IndexError exception
    Returns:
        The value (any type) referenced by the cursor
    """

    if lst.cursor == None:
        raise IndexError("cursor is invalid")

    val = lst.cursor.data
    lst.cursor = lst.cursor.next
    return val


###########################################################
# LINKED LIST FUNCTIONS                                
###########################################################

def clear(lst):
    """
       Make a list empty.
       Parameters:
           lst ( SlList ) - the linked list
       Returns:
           None
    """

    lst.head = None
    lst.size = 0
    lst.cursor = None  # invalidate cursor on clear()


def toString(lst):
    """
    Converts the linked list into a string form that is similar to Python's
    printed list.

    Parameters:
        lst (SlList) - The linked list
    Returns:
        A string representation of the list (e.g. '[1,2,3]')
    """

    result = '['
    curr = lst.head
    while not curr == None:
        if curr.next == None:
            result += str(curr.data)
        else:
            result += str(curr.data) + ', '
        curr = curr.next
    result += ']'

    return result


def append(lst, value):
    """
       Add a node containing the value to the end of the list. 

       Parameters:
           lst ( SlList ) - The linked list
           value ( any type ) - The data to append to the end of the list
       Returns:
           None
    """

    if lst.head == None:
        lst.head = Node(value, None)
    else:
        curr = lst.head
        while curr.next != None:
            curr = curr.next
        curr.next = Node(value, None)
    lst.size += 1


def insertAt(lst, idx, value):
    """
       Insert a new element before the index.

       Parameters:
           lst ( SlList ) - The list to insert value into
           idx ( int ) - The 0-based index to insert before
           value ( any type ) - The data to be inserted into the list
       Preconditions:
           0 <= idx <= lst.size, raises IndexError exception
       Returns:
           None
    """

    if idx < 0 or idx > lst.size:
        raise IndexError(str(idx) + ' is out of range.')

    if idx == 0:
        lst.head = Node(value, lst.head)
    else:
        prev = lst.head
        while idx > 1:
            prev = prev.next
            idx -= 1
        prev.next = Node(value, prev.next)

    lst.size += 1


def get(lst, idx):
    """
       Returns the element that is at index in the list.

       Parameters:
           lst ( SlList ) - The list to insert value into
           idx ( int ) - The 0-based index to get
       Preconditions:
           0 <= idx < lst.size, raises IndexError exception
       Returns:
           value at the index
    """

    if idx < 0 or idx >= lst.size:
        raise IndexError(str(idx) + ' is out of range.')

    curr = lst.head
    while idx > 0:
        curr = curr.next
        idx -= 1
    return curr.data


def set(lst, idx, value):
    """
       Sets the element that is at index in the list to the value.

       Parameters:
           lst ( SlList ) - The list to insert value into
           idx ( int ) - The 0-based index to set
           value ( any type )   
       Preconditions:
           0 <= idx < lst.size, raises IndexError exception
       Returns:
           None
    """

    if idx < 0 or idx >= lst.size:
        raise IndexError(str(idx) + ' is out of range.')

    curr = lst.head
    while idx > 0:
        curr = curr.next
        idx -= 1
    curr.data = value


def pop(lst, idx):
    """
       pop removes and returns the element at index.

       Parameters:
           lst ( SlList ) - The list from which to remove
           idx ( int ) - The 0-based index to remove
       Preconditions:
           0 <= idx < lst.size, raises IndexError exception
       Returns:
           The value ( any type ) being popped
    """

    if idx < 0 or idx >= lst.size:
        raise IndexError(str(idx) + ' is out of range.')

    if idx == 0:
        value = lst.head.data
        lst.head = lst.head.next
    else:
        prev = lst.head
        while idx > 1:
            prev = prev.next
            idx -= 1
        value = prev.next.data
        prev.next = prev.next.next

    lst.size -= 1
    lst.cursor = None  # invalidate cursor on pop()
    return value


def index(lst, value):
    """
       Returns the index of the first occurrence of a value in the list

       Parameters:
           lst ( SlList ) - The list to insert value into
           value ( any type ) - The data being searched for 
       Preconditions:
           value exists in list, otherwise raises ValueError exception
       Returns:
           The 0-based index of value
    """

    pos = 0
    curr = lst.head
    while not curr == None:
        if curr.data == value:
            return pos

        pos += 1
        curr = curr.next

    raise ValueError(str(value) + " is not present in the list")


############################## ADDED FUNCTIONS #####################

def insertListAt(lst1, idx, lst2):
    """
    Insert all elements of lst2 before the index.

    Parameters:
        lst1 (MyList) - The first list to insert into
        idx (int) - The 0 based index to insert before
        lst2 (MyList) - The second list to be inserted into the first list
    Preconditions:
            0 <= idx <= lst1.size, raises IndexError exception
    Returns:
        None.  lst1 absorbs lst2, and lst2 is cleared.
    """

    if idx < 0 or idx > lst1.size:
        raise IndexError(str(idx) + ' is out of range.')

    if lst2.size == 0:
        return  # no changes

    # PUT YOUR IMPLEMENTATION HERE
    if idx == 0:
        curr = lst2.head
        while curr.next != None:
            curr = curr.next
        curr.next = lst1.head
        lst1.head = lst2.head
    else:
        prev = lst1.head
        while idx > 1:
            prev = prev.next
            idx -= 1
        curr = lst2.head
        while curr.next != None:
            curr = curr.next
        curr.next = prev.next
        prev.next = lst2.head
    lst1.size += lst2.size

    clear(lst2)


def deleteSegment(lst, idx, segSize):
    """
    Delete a segment of segSize elements from lst.
    If idx is out of range of if there are not
    segSize elements that can be deleted starting
    from idx, raise error.  Invalidates the cursor.
    :param lst: list to delete elements from
    :param idx: index at which to begin deleting (including that one)
    :param segSize: number of elements of list to delete
    :return: None.  lst is modified.
    """
    if idx < 0 or idx >= lst.size:
        raise IndexError(str(idx) + ' is out of range.')

    if segSize < 0:
        raise ValueError('can not delete a negative number of elements:',
                         segSize)

    if idx + segSize > lst.size:
        raise IndexError('deletion interval extends beyond list end')

    # PUT YOUR IMPLEMENTATION HERE
    if segSize == 0:
        return
    elif idx == 0:
        while segSize > 0:
            lst.head = lst.head.next
            segSize -= 1
        return

    lst.size -= segSize
    prev = lst.head
    while idx > 1:
        prev = prev.next
        idx -= 1
    curr = prev.next
    while segSize > 1:
        curr = curr.next
        segSize -= 1
    prev.next = curr.next

    lst.cursor = None


def copySegment(lst, idx, segSize):
    """
    Copy the segment of segSize elements beginning at idx.
    Insert the copy immediately following the end of the
    segment to be copied. Error if idx out of range or
    not enough elements to copy starting from that point.
    Does NOT make a deepcopy.
    :param lst: lst to modify
    :param idx: index to begin copy segment
    :param segSize: number of elements to copy
    :return: None.  lst is modified.
    """
    if idx < 0 or idx >= lst.size:
        raise IndexError(str(idx) + ' is out of range.')

    if segSize < 0:
        raise ValueError('can not copy a negative number of elements:', segSize)

    if idx + segSize > lst.size:
        raise IndexError('copy interval extends beyond list end')

    if segSize == 0:  # no change
        return
    # PUT YOUR IMPLEMENTATION HERE
    lst.size += segSize

    if idx == 0:
        fakeNode = Node(None, lst.head)
        curr = fakeNode
    else:
        curr = lst.head

    while idx > 1:
        curr = curr.next
        idx -= 1
    prev = curr.next

    for i in range(segSize - 1):
        prev = prev.next

    for i in range(segSize):
        curr = curr.next
        newNode = Node(curr.data, prev.next)
        prev.next = newNode
        prev = prev.next
