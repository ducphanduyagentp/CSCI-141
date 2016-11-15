"""
file: stack_machine.py
description: stack machine for csci141 Lab - Derp the Compiler - Version 3.0

author: ben k steele (bks@cs.rit.edu)
"""

from rit_lib import *

##############################################################################
# byte-code, stack machine functions
# DO NOT CHANGE THIS CODE.
##############################################################################

def execute( stackCode):
    """
    execute : list( StackOp) -> int
    Each StackOp is a function of the form Function : Stack -> NoneType
    and its action occurs as a side effect changing the stack argument
    to the function. The Stack implementation is a python list.
    """
    TheStack = list()
    for func in stackCode:
        func( TheStack)
    return TheStack[-1]

def emitPush( n):
    """
    emitPush : int -> StackOp
    """
    def push( TheStack):
        TheStack.append( n)
    return push

def emitAdd():
    """
    emitAdd : Void -> StackOp
    """
    def add( TheStack):
        n2 = TheStack.pop()
        n1 = TheStack.pop()
        TheStack.append( n1 + n2)
    return add

def emitSub():
    """
    emitSub : Void -> StackOp
    """
    def sub( TheStack):
        n2 = TheStack.pop()
        n1 = TheStack.pop()
        TheStack.append( n1 - n2)
    return sub

def emitMul():
    """
    emitMul : Void -> StackOp
    """
    def mul( TheStack):
        n2 = TheStack.pop()
        n1 = TheStack.pop()
        TheStack.append( n1 * n2)
    return mul

def emitDiv():
    """
    emitDiv : Void -> StackOp
    """
    def div( TheStack):
        n2 = TheStack.pop()
        n1 = TheStack.pop()
        TheStack.append( n1 // n2)
    return div

