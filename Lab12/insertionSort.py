"""
file: insertionSort.py
language: python3
author: Arthur Nunes-Harwitt
purpose: Implementation of insertion sort algorithm
"""


def insertionSort( lst ):
   """
   insertionSort: List( A ) -> NoneType
      where A is totally ordered
      effect: modifies lst so that the elements are in order
   """
   for mark in range( len( lst )-1 ):
      insert( lst, mark )


def insert( lst, mark ):
   """
   insert: List( A ) * NatNum -> NoneType
      where A is totally ordered
      effect: moves the value just past the mark to its sorted position
   """
   for index in range( mark, -1, -1 ):
      if lst[index] > lst[index+1]:
         swap( lst, index, index+1 )
      else:
         return


def swap( lst, i, j ): 
   """
   swap: List( A ) * NatNum * NatNum -> NoneType
      where A is totally ordered
      effect: swaps the values in lst at positions i and j
   """
   ( lst[i], lst[j] ) = ( lst[j], lst[i] )


L = [1,5,3,4,2,2,7,5,3,4,9,0,1,2,5,4,76,6]
insertionSort( L )
print( L )

