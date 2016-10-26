"""
description: Word Count Program for CSCI 141
file: word_count.py
language: python3
author: sps@cs.rit.edu Sean Strout
author: jeh@cs.rit.edu James Heliotis
author: bks@cs.rit.edu ben k steele
author: jsb@cs.rit.edu Jeremy Brown
author: anh@cs.rit.edu Arthur Nunes-Harwitt
"""

# import the functions needed from the hashtable.py module.

from hashtable import *


def word_count(hTable, filename):
    """
        Record the frequency of all words in the named file in the hashtable.
        word_count : HashTable String -> HashTable
    """

    # Read the words of the text file into the word count table.
    fd = open(filename)
    for line in fd:
        for word in line.split():
            # using a regular expression argument to strip(),
            # strip out punctuation and convert token to lower-case.
            word = word.strip(",.\"\';:-!?").lower()
            if has(hTable, word):
                count = get(hTable, word)
                put(hTable, word, count + 1)
            else:
                put(hTable, word, 1)

    fd.close()  # closing the file is a 'good practice'.
    return hTable


def printSummary(theTable):
    """
    printSummary prints a summary of information about the hash table contents.
    printSummary : HashTable -> NoneType
    """

    # Display the entire table!
    print("Unique words:", theTable.size)

    # Find the most common word in the text file.
    total = 0
    maxWord = ""
    maxCount = 0
    for key in keys(theTable):
        thisCount = get(theTable, key)
        total += thisCount
        if thisCount > maxCount:
            maxCount = thisCount
            maxWord = key

    print("There are " + str(len(keys(theTable))) + " words.")
    print("Total words:", total)
    print('"' + maxWord + "\" appeared ", str(maxCount),
          " times, more than any other word.")


def printTable(hTable):
    """
        Print the contents of the given hash table.
        Each key/value pair is displayed in parentheses, tuple-style.
        All pairs appear on a single line.
        printTable : HashTable -> NoneType
    """
    print("Word Count Data ---------------")
    lcount = 0
    ltext = 0
    for key in keys(hTable):
        # print( "(" + key + "," + str( get( hTable, key ) ) + ")", end=" " )
        txt = "(" + key + "," + str(get(hTable, key)) + ")"
        ltext += len(txt)
        if ltext > 51:
            print(txt)
            ltext = 0
        else:
            print(txt, end=" ")
    print()


def hash_function(val):
    """
    hash_function: K NatNum -> NatNum
    Compute a hash of the val string that is in [0 ... n).
    """
    return hash(val)


def main():
    capacity = int(input("Enter capacity (-1 for default): "))
    if capacity < 0:
        hTable = createHashTable(hash_function)
    else:
        hTable = createHashTable(hash_function, capacity)
    filename = input("Enter filename: ")

    wordTable = word_count(hTable, filename)
    printSummary(wordTable)

    while True:

        print("Commands: k[ey] <word> f[ind] <word> q[uit] ? ", end=" ")
        response = input(":- ")  # the displayed prompt
        query = response.split()

        if len(response) == 0 or not response[0] in "fkq":
            print(response + " invalid. Please enter a command and a word.")
            response = ""
            continue

        if query[0] == "k":
            print("( " + query[1] + " in text ) is " \
                  + str(has(wordTable, query[1])) + ".")

        if query[0] == "f":
            if has(wordTable, query[1]):
                print(query[1] + " appears " \
                      + str(get(wordTable, query[1])) + " times.")
            else:
                print(query[1] + " in not in the text.")

        if query[0] == "q":
            break
    #
    answer = input("Do you want to see the entire table?(y/n) ")
    if answer != "y":
        return
    printTable(wordTable)


# run the main program
main()
