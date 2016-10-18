"""
file: dlNode.py
language: python 3
author: Duc Phan - ddp3945@rit.edu
description: double link Node class
"""

from rit_lib import *


class dlNode(struct):
    _slots = ((object, 'data'), ((NoneType, 'dlNode'), 'leftNode'), ((NoneType, 'dlNode'), 'rightNode'))
