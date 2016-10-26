"""
description: open addressing Hash Table for CS 141 Lecture
file: hashtable.py
language: python3
author: sps@cs.rit.edu Sean Strout
author: jeh@cs.rit.edu James Heliotis
author: anh@cs.rit.edu Arthur Nunes-Harwitt
author: jsb@cs.rit.edu Jeremy Brown
author: as@cs.rit.edu Amar Saric
author: scj@cs.rit.edu Scott Johnson
           -- Added the hash function as a slot to the hash table
		   -- Added a capacity slot in the hash table
"""

from rit_lib import *


class HashTable(struct):
    """
           The HashTable data structure contains a collection of values
       where each value is located by a hashable key.
       No two values may have the same key, but more than one
       key may have the same value.
       table is the list holding the hash table
       size is the number of elements in occupying the hashtable

    """
    _slots = ((list, 'table'), (int, 'size'),
              (int, 'capacity'), (object, 'hash_func'))


def createHashTable(hash_func, capacity=100):
    """
    createHashTable: NatNum? -> HashTable
    """
    # COMPLETE THIS FUNCTION
    lst = [[] for _ in range(capacity)]
    return HashTable(lst, 0, capacity, hash_func)


def resizeHashTable(hTable):
    """
    HashTableToStr: HashTable -> None
    
    Doubles the size of the table.
    """

    # COMPLETE THIS FUNCTION

    return None


def HashTableToStr(hashtable):
    """
    HashTableToStr: HashTable -> String
    """
    result = ""
    for i in range(len(hashtable.table)):
        e = hashtable.table[i]
        if not e == None:
            result += str(i) + ": "
            result += EntryToStr(e) + "\n"
    return result


class Entry(struct):
    """
       A class used to hold key/value pairs.
    """

    _slots = ((object, "key"), (object, "value"))


def EntryToStr(entry):
    """
    EntryToStr: Entry -> String
    return the string representation of the entry.
    """
    return "(" + str(entry.key) + ", " + str(entry.value) + ")"


def imbalance(hTable):
    """
    keys: HashTable(K, V) -> Num
    
    Computes the imbalance of the hashtable.
    """

    # COMPLETE THIS FUNCTION
    nChain = 0
    sum = 0
    for i in range(len(hTable.table)):
        l = len(hTable.table[i])
        sum += l
        nChain += int(l != 0)
    if nChain == 0:
        return 0
    return (sum / nChain) - 1


def keys(hTable):
    """
    keys: HashTable(K, V) -> List(K)
    Return a list of keys in the given hashTable.
    """
    result = []
    for entry in hTable.table:
        if entry != None:
            result.append(entry.key)
    return result


def has(hTable, key):
    """
    has: HashTable(K, V) K -> Boolean
    Return True iff hTable has an entry with the given key.
    """

    # THIS IS OPEN-ADDRESSING has(). REWRITE THIS FUNCTION FOR CHAINING.

    index = hTable.hash_func(key) % hTable.capacity
    startIndex = index  # We must make sure we don't go in circles.
    while hTable.table[index] != None and hTable.table[index].key != key:
        index = (index + 1) % len(hTable.table)
        if index == startIndex:
            return False
    return hTable.table[index] != None


def put(hTable, key, value):
    """
    put: HashTable(K, V) K V -> Boolean

    Using the given hash table, set the given key to the
    given value. If the key already exists, the given value
    will replace the previous one already in the table.
    If the table is full, an Exception is raised.
    """

    # COMPLETE THIS FUNCTION

    return True


def get(hTable, key):
    """
    get: HashTable(K, V) K -> V

    Return the value associated with the given key in
    the given hash table.

    Precondition: has(hTable, key)
    """
    # COMPLETE THIS FUNCTION

    return None


def hash_function(str):
    sum = 0
    for i in range(len(str)):
        sum += ord(str[i]) * (31 ** i)
    return sum
