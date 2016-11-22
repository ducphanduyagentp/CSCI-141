"""
file: vlc.py
language: python 3
author: Duc Phan - ddp3945@rit.edu
description: Implementation for Lab 11 - CSCI-141
"""

from array_heap import *


class Symbol(struct):
    _slots = ((str, 'name'), (int, 'freq'), (str, 'codeword'))


class Node(struct):
    _slots = ((int, 'aFreq'), (list, 'symbols'))


def createSymbol(name, freq, codeword):
    return Symbol(name, freq, codeword)


def createNode(aFreq, symbols):
    return Node(aFreq, symbols)


def readSymbols(filename):
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
    return node1.aFreq < node2.aFreq


def buildHeap(symbols):
    heap = createEmptyHeap(len(symbols), compareFunc)
    for s in symbols:
        symbol = createSymbol(s, symbols[s], '')
        node = createNode(symbol.freq, [symbol])
        add(heap, node)
    displayHeap(heap)
    return heap


def generateCodeword(heap):
    pass

def printSummary(symbols, heap):
    pass


def main():
    filename = input('Please enter symbol filename: ')
    symbols = readSymbols(filename)
    symbolHeap = buildHeap(symbols)
    printSummary(symbols, symbolHeap)

main()
