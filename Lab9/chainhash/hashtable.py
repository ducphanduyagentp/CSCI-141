"""
file: hashtable.py
language: python3
author: Duc Phan - ddp3945@rit.edu
description: chaining Hash Table - CSCI-141 Lab 9
"""

from rit_lib import *


class HashTable(struct):
    """
    table: python list of python list - holding the hash table
    size: int - number of unique keys in the hash table
    nEntries: int - number of non-empty chain in the hash table
    capacity: int
    hash_func: object
    """
    _slots = ((list, 'table'), (int, 'size'), (int, 'nEntries'),
              (int, 'capacity'), (object, 'hash_func'))


def createHashTable(hash_func, capacity=100):
    """
    createHashTable: Function NatNum -> HashTable
    Create a hash table that uses chaining.
    """
    # COMPLETE THIS FUNCTION
    lst = [[] for _ in range(capacity)]
    return HashTable(lst, 0, 0, capacity, hash_func)


def resizeHashTable(hTable):
    """
    resizeHashTable: HashTable -> None
    - Change the hash table of capacity N to a hash table of capacity 2N + 1
    - Rehash the entries in the hash table
    """
    # COMPLETE THIS FUNCTION
    newCapacity = 2 * hTable.capacity + 1
    newNEntries = 0
    lst = [[] for _ in range(newCapacity)]
    for chain in hTable.table:
        for e in chain:
            index = hTable.hash_func(e.key) % newCapacity
            if len(lst[index]) == 0:
                newNEntries += 1
            lst[index].append(e)
    hTable.table = lst
    hTable.capacity = newCapacity
    hTable.nEntries = newNEntries
    return None


def HashTableToStr(hashtable):
    """
    HashTableToStr: HashTable -> String
    Represent the content of the hash table into string
    """
    result = ""
    for i in range(len(hashtable.table)):
        lst = hashtable.table[i]
        result += str(i) + ": ["
        for j in range(len(lst)):
            if j > 0:
                result += ', '
            result += EntryToStr(lst[j])
        result += ']\n'
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
    for lst in hTable.table:
        for entry in lst:
            result.append(entry.key)
    return result


def has(hTable, key):
    """
    has: HashTable(K, V) K -> Boolean
    Determine if hTable has an entry with the given key.
    """
    # THIS IS OPEN-ADDRESSING has(). REWRITE THIS FUNCTION FOR CHAINING.

    index = hTable.hash_func(key) % hTable.capacity
    for e in hTable.table[index]:
        if e.key == key:
            return True
    return False


def put(hTable, key, value):
    """
    put: HashTable(K, V) K V -> Boolean

    Using the given hash table, set the given key to the
    given value. If the key already exists, the given value
    will replace the previous one already in the table.
    If the table is full, an Exception is raised.
    """

    # COMPLETE THIS FUNCTION
    load = hTable.nEntries / hTable.capacity
    if load >= 0.75:
        resizeHashTable(hTable)

    index = hTable.hash_func(key) % hTable.capacity
    if has(hTable, key):
        lst = hTable.table[index]
        for i in range(len(lst)):
            if lst[i].key == key:
                lst[i].value = value
    else:
        lst = hTable.table[index]
        if len(lst) == 0:
            hTable.nEntries += 1
        hTable.table[index].append(Entry(key, value))
        hTable.size += 1
    return True


def remove(hTable, key):
    """
    remove: HashTable(K, V) K -> None
    Remove the entry that has the corresponding key from the hash table.
    Precondition: has(hTable, key)
    """
    if not has(hTable, key):
        raise Exception('Hash table does not contain key: {}'.format(key))

    index = hTable.hash_func(key) % hTable.capacity
    lst = hTable.table[index]
    for i in range(len(lst)):
        if lst[i].key == key:
            del lst[i]
            hTable.size -= 1
            if len(lst) == 0:
                hTable.nEntries -= 1
            break


def get(hTable, key):
    """
    get: HashTable(K, V) K -> V
    Return the value associated with the given key in
    the given hash table.
    Precondition: has(hTable, key)
    """
    # COMPLETE THIS FUNCTION
    if not has(hTable, key):
        raise Exception('Hash table does not contain key: {}'.format(key))

    index = hTable.hash_func(key) % hTable.capacity
    lst = hTable.table[index]
    for e in lst:
        if e.key == key:
            return e.value
    return None


def hash_function_1(str):
    """
    hash_function_1: str -> NatNum
    Implementation of hash function in question 1 of problem solving
    """
    sum = 0
    for c in str:
        sum += ord(c) - ord('a')
    return sum


def hash_function_2(str):
    """
    hash_function_2: str -> NatNum
    Implementation of hash function in question 2 of problem solving
    """
    sum = 0
    for i in range(len(str)):
        sum += ord(str[i]) * (31 ** i)
    return sum
