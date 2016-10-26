"""
file: potato.py
language: python 3
author: Duc Phan - ddp3945@rit.edu
description: Implementation for Lab 8 - CSCI-141
"""

import random

from dlList import *


def playGame(lst):
    """
    Play the Hot Potato Game and determine the winner
    :param lst: dlList
    :return: NoneType
    """
    nRound = lst.size - 1
    for i in range(nRound):
        position = random.randint(-2 * lst.size, 2 * lst.size)
        print('The music starts ({}): '.format(position), end='')
        if position == 0:
            removeNode(lst)
        else:
            removeNode(lst, position)
    print('{} is the winner!'.format(getNode(lst, 0)))


def main():
    """
    - Prompt user for a list of contestants
    - Prompt user for a seed for random number generator
    - Print the list of contestants
    - Play the game with the required number of rounds and determine the winner.
    - For each round, print all the contestants on the path of the potato.
    :return: NoneType
    """
    print('Welcome to the Hot Potato Game!')
    filename = input('Enter a file of contestants: ')
    intSeed = int(input('Enter a seed number for random number generator: '))

    random.seed(intSeed)
    lst = createdlList()
    print('Ready to play Hot Potato. Contestants are:')
    flag = False
    for line in open(filename):
        addNode(line.strip(), lst)
        if flag:
            print(', ', end='')
        flag = True
        print(line.strip(), end='')
    print()

    playGame(lst)


main()
