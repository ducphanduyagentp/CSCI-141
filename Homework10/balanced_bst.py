"""
file: balanced_bst.py
language: python 3
author: Duc Phan - ddp3945@rit.edu
description: Implementation for Homework 10 - CSCI-141
"""

from rit_lib import *
import random
import math


class BinaryTree(struct):
    _slots = (((NoneType, 'BinaryTree'), 'left'), (object, 'value'), ((NoneType, 'BinaryTree'), 'right'))


def create_tree(value, left=None, right=None):
    """
    Create a binary tree with optional left and right sub-trees.
    :param value: object
    :param left: NoneType or BinaryTree
    :param right: NoneType or BinaryTree
    :return: BinaryTree
    """
    return BinaryTree(left, value, right)


def balanced_bst_tree_from_list(lst):
    """
    Create a balanced binary search tree from a list.
    Pre-condition: lst is a sorted list.
    :param lst: list
    :return: BinaryTree
    """
    if len(lst) == 0:
        return None
    mid_index = len(lst) // 2
    mid_value = lst[mid_index]
    return create_tree(mid_value, balanced_bst_tree_from_list(lst[:mid_index]),
                       balanced_bst_tree_from_list(lst[mid_index + 1:]))


def in_order_traversal(bst):
    """
    Perform in-order traversal on a binary tree.
    :param bst: BinaryTree
    :return: list
    """
    if bst == None:
        return []
    return in_order_traversal(bst.left) + [bst.value] + in_order_traversal(bst.right)


def tree_height(bst):
    """
    Determine the height (depth) of a binary tree.
    :param bst: BinaryTree
    :return: int
    """
    if bst == None:
        return -1
    return 1 + max(tree_height(bst.left), tree_height(bst.right))


def main():
    """
    - Prompt user for a list size number N
    - Generate a list of N elements of random integers between [-1000, 1000]
    - Print the list
    - Sort the list and print the sorted list
    - Create a binary search tree using the sorted list
    - Perform in-order traversal on the created tree
    - Calculate and print the height of the tree
    - Calculate and print the value log2(N)
    """
    size = input('Enter size: ')
    for c in size:
        if not c.isdigit():
            print('Usage: run python3 balanced_bst.py and enter a non-negative integer')
            return
    size = int(size)
    print('Entered: {}'.format(size))

    lst = []
    for _ in range(size):
        lst.append(random.randint(-1000, 1000))
    print('Number List: {}'.format(lst))
    lst.sort()
    print('Sorted List: {}'.format(lst))

    bst = balanced_bst_tree_from_list(lst)
    t = in_order_traversal(bst)
    print('In Order Traversal:')
    print(t)
    print('Height: {}'.format(tree_height(bst)))
    if size > 0:
        print('Log2 of N is: {}'.format(math.log2(size)))
    else:
        print('Log2 of N is undefined')


main()
