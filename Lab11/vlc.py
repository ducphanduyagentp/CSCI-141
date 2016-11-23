"""
file: vlc.py
language: python 3
author: Duc Phan - ddp3945@rit.edu
description: Implementation for Lab 11 - CSCI-141
"""

from array_heap import *
import math


class Symbol(struct):
    _slots = ((str, 'name'), (int, 'freq'), (str, 'codeword'))


class Node(struct):
    _slots = ((int, 'aFreq'), (list, 'symbols'))


def createSymbol(name, freq, codeword):
    """Create an instance of class Symbol"""
    return Symbol(name, freq, codeword)


def createNode(aFreq, symbols):
    """Create an instance of class Node"""
    return Node(aFreq, symbols)


def readSymbols(filename):
    """
    - Read and store the symbols from the provided file
    - Store the symbols with their frequencies in a python dictionary
    str -> dict
    """
    symbols = dict()
    for line in open(filename):
        line = line.strip()
        for s in line:
            if s in symbols:
                symbols[s] += 1
            else:
                symbols[s] = 1
    return symbols


def compareFunc(node1, node2):
    """
    A comparing function used for heap
    Node * Node -> boolean
    """
    return node1.aFreq < node2.aFreq


def buildHeap(symbols):
    """
    Build a heap for a dictionary of symbols and their frequencies
    dict -> Heap
    """
    heap = createEmptyHeap(len(symbols), compareFunc)
    for s in symbols:
        symbol = createSymbol(s, symbols[s], '')
        node = createNode(symbol.freq, [symbol])
        add(heap, node)
    return heap


def generateCodeword(heap):
    """
    Implementation of Variable Length Code Algorithm
    Heap -> NoneType
    """
    while heap.size > 1:
        n1 = removeMin(heap)
        n2 = removeMin(heap)
        newFreq = n1.aFreq + n2.aFreq
        for i in range(len(n1.symbols)):
            symbol = n1.symbols[i]
            symbol.codeword = '0' + symbol.codeword
        for i in range(len(n2.symbols)):
            symbol = n2.symbols[i]
            symbol.codeword = '1' + symbol.codeword
        newSymbols = n1.symbols + n2.symbols
        node = createNode(newFreq, newSymbols)
        add(heap, node)


def printSummary(heap):
    """
    - Print a summary of symbols and their codewords
    - Calculate and print the average length of codewords when using
    VLC and Fixed codewords
    Heap -> NoneType
    """
    header = 'Variable Length Code Output'
    print(header)
    print('-' * len(header))
    root = peek(heap)

    a1 = 0
    a2 = math.ceil(math.log2(len(root.symbols)))

    for s in root.symbols:
        a1 += len(s.codeword) * s.freq
        line = 'Symbol: {:2s}  '.format(s.name)
        line += 'Codeword: {:>8}  '.format(s.codeword)
        line += 'Frequency: {:5d}'.format(s.freq)
        print(line)

    a1 /= float(root.aFreq)
    print('Average VLC codeword length: {} bits per symbol'.format(a1))
    print('Average Fixed length codeword length: {} bits per symbol'.format(a2))


def main():
    """
    - Prompt user for a filename
    - Read the symbols from the file
    - Generate codewords for the symbols using Variable Length Code algorithm
    - Print a summary of the symbols, their codewords and frequencies
    - Print the average length of the codewords that use different algorithms
    """
    filename = input('Please enter symbol filename: ')
    symbols = readSymbols(filename)
    symbolHeap = buildHeap(symbols)
    generateCodeword(symbolHeap)
    printSummary(symbolHeap)


main()
