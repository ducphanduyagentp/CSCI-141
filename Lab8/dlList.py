"""
file: dlList.py
language: python 3
author: Duc Phan - ddp3945@rit.edu
description: definition of doubly-linked List
"""

from dlNode import *


class dlList(struct):
    _slots = (((NoneType, dlNode), 'potatoHolder'), (int, 'size'))
