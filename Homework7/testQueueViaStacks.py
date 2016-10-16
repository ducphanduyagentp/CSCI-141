"""
file: testQueueViaStacks.py
language: python 3
author: Duc Phan - ddp3945@rit.edu
description: Test queue via stacks implementation
"""

from myQueueViaStacks import *


def main():
    # begin with an empty queue
    queueCh = createQVS()
    print("Creating empty queue...")
    print("Queue empty?", True == emptyQueue(queueCh))
    print("Queue size is 0?", 0 == queueCh.size)

    # add first element
    print("enqueue A...")
    enqueue(queueCh, 'A')
    print("Queue not empty?", False == emptyQueue(queueCh))
    print("Queue size is 1?", 1 == queueCh.size)
    print("front is A?", 'A' == front(queueCh))
    print("back is A?", 'A' == back(queueCh))

    # add second element
    print("enqueue B...")
    enqueue(queueCh, 'B')
    print("front is A?", 'A' == front(queueCh))
    print("back is B?", 'B' == back(queueCh))

    # add third element
    print("enqueue C...")
    enqueue(queueCh, 'C')
    print("Queue size is 3?", 3 == queueCh.size)
    print("front is A?", 'A' == front(queueCh))
    print("back is C?", 'C' == back(queueCh))

    # dequeue top element, C
    print("dequeue...")
    dequeue(queueCh)
    print("Queue not empty?", False == emptyQueue(queueCh))
    print("Queue size is 2?", 2 == queueCh.size)
    print("front is B?", 'B' == front(queueCh))
    print("back is C?", 'C' == back(queueCh))

    # add fourth element
    print("enqueue D...")
    enqueue(queueCh, 'D')
    print("front is B?", 'B' == front(queueCh))
    print("back is D?", 'D' == back(queueCh))

    # Empty the queue
    print("Emptying the queue...")
    while not emptyQueue(queueCh):
        print("Front of queue:", front(queueCh))
        print("Back of queue:", back(queueCh))
        print("dequeue...")
        dequeue(queueCh)


main()
