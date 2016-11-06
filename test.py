"""
file: hashtable.py
description: open addressing Hash Table for CS 141 Lecture
language: python3
author: RIT CS Instructors
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
    createHashTable: (Func : KT -> NatNum) NatNum? -> HashTable
    """
    if capacity < 2:
        capacity = 2
    aHashTable = HashTable([None for _ in range(capacity)], 0,
                           capacity, hash_func)
    return aHashTable


def HashTableToStr(hashtable):
    """
    HashTableToStr: HashTable -> String
    """
    result = ""
    for i in range(hashtable.capacity):
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
    index = hTable.hash_func(key) % hTable.capacity
    startIndex = index  # We must make sure we don't go in circles.
    while hTable.table[index] != None and hTable.table[index].key != key:
        index = (index + 1) % hTable.capacity
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

    index = hTable.hash_func(key) % hTable.capacity
    startIndex = index  # We must make sure we don't go in circles.
    while hTable.table[index] != None and hTable.table[index].key != key:
        index = (index + 1) % hTable.capacity
        if index == startIndex:
            raise Exception("Hash table is full.")
    if hTable.table[index] == None:
        hTable.table[index] = Entry(key, value)
        hTable.size += 1
    else:
        hTable.table[index].value = value
    return True


def get(hTable, key):
    """
    get: HashTable(K, V) K -> V

    Return the value associated with the given key in
    the given hash table.

    Precondition: has(hTable, key)
    """
    index = hTable.hash_func(key) % hTable.capacity
    startIndex = index  # We must make sure we don't go in circles.
    while hTable.table[index] != None and hTable.table[index].key != key:
        index = (index + 1) % hTable.capacity
        if index == startIndex:
            raise Exception("Hash table does not contain key.")
    if hTable.table[index] == None:
        raise Exception("Hash table does not contain key:", key)
    else:
        return hTable.table[index].value


def main():
    raise Exception('Hash table does not contain key: {}'.format(1))
    print('gg')


main()
