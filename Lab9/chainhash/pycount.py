""" 
file: pycount.py
language: python3
author: sps@cs.rit.edu Sean Strout 
description: Word Count Program for CS 141 Lecture
            This version uses the built-in dict type.
"""


def word_count(filename):
    """Report on the frequency of different words in the
       file named by the argument.
    """
    d = {}
    inFile = open(filename)

    for line in inFile:
        for word in line.split():
            word = word.strip(",.\"\';:-!?").lower()
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
    inFile.close()

    print("Total words:", sum(d.values()))
    print("Unique words:", len(d))
    most = list(d.values())
    most.sort()
    for k in d:
        if d[k] == most[-1]:
            print("Most used word:  ", k, "  occurred", d[k], "times.")


def main():
    filename = input("Enter filename: ")
    word_count(filename)


main()
