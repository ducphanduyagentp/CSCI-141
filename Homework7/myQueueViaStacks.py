"""
file: myQueueViaStacks.py
language: python 3
author: Duc Phan - ddp3945@rit.edu
description: Implementation of queue data structure using two (2) stacks
"""

from lib.myStack import *


class QueueViaStacks(struct):
    _slots = ((Stack, 'stack1'), (Stack, 'stack2'), (int, 'size'))


def createQVS():
    """Create an empty queue"""
    return QueueViaStacks(createStack(), createStack(), 0)


def emptyQueue(queue):
    """Determine if the queue is empty or not"""
    return emptyStack(queue.stack1)


def enqueue(queue, element):
    """Insert the element to the back of the queue"""
    push(queue.stack1, element)
    queue.size += 1


def dequeue(queue):
    """Remove the element at the front of the queue"""
    if emptyQueue(queue):
        raise IndexError("dequeue on empty queue")
    while not emptyStack(queue.stack1):
        push(queue.stack2, top(queue.stack1))
        pop(queue.stack1)
    pop(queue.stack2)
    while not emptyStack(queue.stack2):
        push(queue.stack1, top(queue.stack2))
        pop(queue.stack2)
    queue.size -= 1


def front(queue):
    """Access and return the element at the front of the queue"""
    if emptyQueue(queue):
        raise IndexError("front on empty queue")
    while not emptyStack(queue.stack1):
        push(queue.stack2, top(queue.stack1))
        pop(queue.stack1)
    front = top(queue.stack2)
    while not emptyStack(queue.stack2):
        push(queue.stack1, top(queue.stack2))
        pop(queue.stack2)
    return front


def back(queue):
    """Access and return the element at the back of the queue"""
    if emptyQueue(queue):
        raise IndexError("back on empty queue")
    return top(queue.stack1)
