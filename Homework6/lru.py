"""
file: lru.py
language: python 3
author: Duc Duy Phan - ddp3945@rit.edu
description: Homework 6 - CSCI-141
"""

from rit_lib import *


class LRUEntry(struct):
    _slots = ((str, 'page'), (int, 'time'))


def put_in_cache(entry, cache):
    """
    Place the LRU Entry into the first empty slot in the cache list
    - pre-condition: The list cache is not full
    - post-condition: The entry is in the first
    :param entry: LRUEntry Class instance
    :param cache: list
    :return: int
    """
    for i in range(len(cache)):
        if cache[i] == None:
            cache[i] = entry
            return i


def position_in_cache(request, cache):
    """
    Find the index of the cache entry whose page matches the request
    :param request: string
    :param cache: list
    :return: int
    """
    for i in range(len(cache)):
        if cache[i] != None:
            if cache[i].page == request:
                return i
    return len(cache)


def find_LRU(cache):
    """
    Find the cache entry that is least recently used
    :param cache: list
    :return: tuple
    """
    if len(cache) == 0:
        return (None, None)
    if cache[0] == None:
        return (cache[0], 0)
    else:
        min_index = 0
        min_time = cache[0].time

    for i in range(len(cache)):
        if cache[i] == None:
            return (cache[i], i)
        if cache[i].time < min_time:
            min_time = cache[i].time
            min_index = i
    return (cache[min_index], min_index)


def run_LRU(cache, requests):
    """
    - Process the request
    - Output information in each request about the result, the victim and the current cache list
    - Count the number of cache MISS
    :param cache: list
    :param requests: string
    :return: int
    """
    missCount = 0
    for i in range(len(requests)):
        print('Time:', i, end=' ')
        print('Request:', requests[i], end=' ')

        position = position_in_cache(requests[i], cache)
        isMiss = position == len(cache)
        missCount += int(isMiss)

        if isMiss:
            print('MISS.', end=' ')
            victim = find_LRU(cache)
            isCacheFull = victim[0] != None

            if isCacheFull:
                cache[victim[1]] = LRUEntry(requests[i], i)
                print('Victim:', victim[0], end=' ')
                print('Cache:', end=' ')
                print(cache)
            else:
                put_in_cache(LRUEntry(requests[i], i), cache)
                print('Victim: _', end=' ')
                print('Cache:', end=' ')
                print(cache)

        else:
            print('HIT.')
            cache[position].time = i
    return missCount


def main():
    """
    - Prompt users for size of cache and memory request string
    - Process the request
    - Output the number of cache MISS
    :return:
    """
    cache_size = int(input('Enter the size of cache: '))
    requests = input('Enter the string of memory requests: ')
    print('Least Recently Used (LRU) Algorithm')
    print('Cache size: ', cache_size)
    print('Memory request string: ', requests)

    cache = []
    for i in range(cache_size):
        cache.append(None)

    n_misses = run_LRU(cache, requests)
    print('Miss count: ', n_misses)


main()
