"""
file: dlList.py
language: python 3
author: Duc Phan - ddp3945@rit.edu
description: doubly linked list
"""

from dlNode import *


class dlList(struct):
    _slots = (((NoneType, dlNode), 'potatoHolder'), (int, 'size'))


def createdlList():
    return dlList(None, 0)


def emptyList(lst):
    return lst.size == 0


def addNode(element, lst, direction):
    if emptyList(lst):
        lst.potatoHolder = dlNode(element, )
