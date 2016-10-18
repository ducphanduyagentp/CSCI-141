"""
file: dlNode.py
language: python 3
author: Duc Phan - ddp3945@rit.edu
description: definition of doubly-linked Node
"""

from rit_lib import *


class dlNode(struct):
    _slots = (((NoneType, 'dlNode'), 'left'), (object, 'data'), ((NoneType, 'dlNode'), 'right'))
