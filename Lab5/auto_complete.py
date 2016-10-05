"""
file: auto_complete.py
language: python 3
author: Duc Duy Phan - ddp3945@rit.edu
description: Searching/Sorting Lab - CSCI-141
"""

import bsearch
import selection_sort


def startsWith(prefix, word):
    """
    Check if the word starts with the prefix
    :param prefix: string
    :param word: string
    :return: Boolean
    """
    return prefix == word[:len(prefix)]


def linearSearch(prefix, data):
    """
    Using linear searching, find all words in the list that start with the prefix and store in a list
    :param prefix: string
    :param data: list
    :return: list
    """
    lst = []
    for i in range(len(data)):
        if startsWith(prefix, data[i]):
            lst.append(data[i])
    return lst


def binarySearch(prefix, data):
    """
    - Using binary searching to find an occurrence of a word in the list that starts with the prefix
    - Using linear searching to iterate forward from that occurrence to find matches
    - Using linear searching to iterate backward from that occurrence to find matches
    - Store all matches in a list
    :param prefix: string
    :param data: list
    :return: list
    """
    lst = []
    index = bsearch.get_index(data, prefix)
    if index == None:
        return lst
    lst.append(data[index])
    for i in range(index + 1, len(data)):
        if startsWith(prefix, data[i]):
            lst.append(data[i])
    for i in range(index - 1, -1, -1):
        if startsWith(prefix, data[i]):
            lst.append(data[i])
    return lst


def readFile(filename):
    """
    Read the provided file and store all words in the file in a list
    :param filename: string
    :return: list
    """
    lst = []
    for lines in open(filename):
        lst += lines.split()
    return lst


def main():
    """
    - Prompt users for a file name containing words
    - Read the words in the file. Make a list of known words
    - Make a sorted and an unsorted list of the known words
    - Repeatedly ask the user for a prefix to search for. Stop the program when user enters <QUIT>
    - Search for the word match using 3 different methods
    :return: NoneType
    """
    filename = input('Enter the name of the known words file: ')
    known_words = readFile(filename)

    unsorted_lst = known_words[:]
    print('The unsorted list: ', unsorted_lst)

    sorted_lst = known_words[:]
    sorted_lst = selection_sort.selectionSort(sorted_lst)
    print('The sorted list: ', sorted_lst)

    print('Welcome to Auto-complete!')
    print('Usage: Enter a prefix to auto-complete.')
    print('Entering nothing will search for the next word with that prefix.')
    print('Enter <QUIT> when asked for a prefix to exit.')

    # flag == -1: Search has not started
    # flag == 0: Perform a search with a new prefix
    # flag == 1: Searching for the next match
    flag = -1

    while True:
        prefix = input('Enter a prefix to search for: ')

        # <QUIT> Command
        if prefix == '<QUIT>':
            print('Exiting Auto-complete! Good bye.')
            return
        elif prefix == '':
            if flag == -1:  # Keep asking users for prefix if nothing has been entered
                continue
            else:  # Users ask for the next match
                flag = 1
        else:  # Initialization for a new search
            flag = 0
            saved_data = []
            noMatches = False
            index = 0

        if flag == 1 and noMatches:
            print('There are no matches.')
            continue

        if flag == 0:
            saved_data.append(linearSearch(prefix, unsorted_lst))
            if len(saved_data[0]) == 0:
                noMatches = True
                print('There are no matches')
                continue
            saved_data.append(linearSearch(prefix, sorted_lst))
            saved_data.append(binarySearch(prefix, sorted_lst))

        print('Match for linear unsorted is ', saved_data[0][index])
        print('Match for linear sorted is ', saved_data[1][index])
        print('Match for binary sorted is ', saved_data[2][index])
        index = (index + 1) % len(saved_data[0])


main()
