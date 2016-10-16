"""
Stack interface.
file: myStack.py
author: Sean Strout
"""

from lib.myNode import *


class Stack(struct):
    _slots = (((NoneType, Node), 'top'), (int, 'size'))


def createStack():
    return Stack(None, 0)


def emptyStack(stack):
    """Is the stack empty?"""
    return stack.top == None


def push(stack, element):
    """Add an element to the top of the stack.  Update size"""
    stack.top = Node(element, stack.top)
    stack.size += 1


def top(stack):
    """Return top element on stack.  Does not change stack"""
    if emptyStack(stack):
        raise IndexError("top of empty stack")
    return stack.top.data


def pop(stack):
    """Remove the top element on the stack.  Update size"""
    if emptyStack(stack):
        raise IndexError("pop on empty stack")
    stack.top = stack.top.next
    stack.size -= 1
