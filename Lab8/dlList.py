"""
file: dlList.py
language: python 3
author: Duc Phan - ddp3945@rit.edu
description: definition of doubly-linked List
"""

from dlNode import *


class dlList(struct):
    _slots = (((NoneType, dlNode), 'potatoHolder'), (int, 'size'))


def createdlList():
    """
    Create a new empty doubly-linked List
    :return: dlList
    """
    return dlList(None, 0)


def emptyList(lst):
    """
    Determine if a dlList is empty or not
    :param lst: dlList
    :return: boolean
    """
    return lst.size == 0


def addNode(element, lst, position=-1):
    """
    - Insert an element to the dlList with the provided direction and position.
    - Go clockwise if the position is positive
    - Go counter-clockwise if the position is negative
    :param element: object
    :param lst: dlList
    :param position: int
    :return: NoneType
    """
    if emptyList(lst):
        newNode = dlNode(None, element, None)
        newNode.left = newNode
        newNode.right = newNode
        lst.potatoHolder = newNode
    else:
        currentNode = lst.potatoHolder
        if position >= 0:
            for i in range(position):
                currentNode = currentNode.right
            newNode = dlNode(currentNode.left, element, currentNode)
            currentNode.left.right = newNode
            currentNode.left = newNode
        elif position < 0:
            for i in range(-position):
                currentNode = currentNode.left
            newNode = dlNode(currentNode, element, currentNode.right)
            currentNode.right.left = newNode
            currentNode.right = newNode
    lst.size += 1


def getNode(lst, position):
    """
    - Get the data of a node at a specific position in a list
    - Go clockwise if the position if positive
    - Go counter-clockwise if the position is negative
    :param lst: dlList
    :param position: int
    :param direction: int
    :return: object
    """
    currentNode = lst.potatoHolder
    for i in range(abs(position)):
        if position > 0:
            currentNode = currentNode.right
        elif position < 0:
            currentNode = currentNode.left
    return currentNode.data


def removeNode(lst, position=0):
    """
    - Remove the node at the specific position in the provided direction.
    - Pass the potato to the next contestant in the provided direction after removing the node
    - Print all the contestants on the path to the node being removed
    :param lst: dlList
    :param position: int. By default, remove the current potatorHolder in the list
    :return: NoneType
    """
    currentNode = lst.potatoHolder
    if position >= 0:
        for i in range(position):
            print(currentNode.data, end='')
            print(' -> ', end='')
            currentNode = currentNode.right
        currentNode.right.left = currentNode.left
        currentNode.left.right = currentNode.right
        lst.potatoHolder = currentNode.right
    elif position < 0:
        for i in range(-position):
            print(currentNode.data, end='')
            print(' -> ', end='')
            currentNode = currentNode.left
        currentNode.right.left = currentNode.left
        currentNode.left.right = currentNode.right
        lst.potatoHolder = currentNode.left
    print('{} is stuck holding the potato!'.format(currentNode.data))
    lst.size -= 1
