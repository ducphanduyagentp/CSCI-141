"""
file: derp.py
description: csci141 Lab - Derp the Compiler - Version 3.0

Derp is a simple, just-in-time compiler that parses an integral expression
into an expression tree (see parse function), compiles the tree into
a stack of instructions (see compile_tree), and executes those instructions
(see execute function).

An expression contains the basic arithmetic operators (*,//,-,+).
Derp performs arithmetic only with operands that are either integral
numeric literals or variables read from a symbol table.

Derp prints the symbol table (see the displayTable function),
produces the expression in infix form with parentheses to denote order
of operation (see infix function), and executes the expression,
which returns the result of the expression so that the main function
can print the result of execution.

author: ben k steele (bks@cs.rit.edu)
author: duc d phan (ddp3945@rit.edu)
"""

from stack_machine import *


##############################################################################
# structure definitions for parse tree
# DO NOT CHANGE THIS CODE.
#
# These operations on numbers are dyadic operations -- they have 2 operands.
# Each has a left and right operand, which may in turn be other operations.
# To generally represent the fact that the operands may be other operations,
# the types of the left and right need to be of a common, shared type.
# We call this an abstract super type.
# Since we have designed our classes around rit_lib.struct, we already have
# a common super type: struct.
# The Node classes below inherit from struct and use rit_lib.struct as the
# type of their left and right slots.
##############################################################################

class MultiplyNode(struct):
    """
    Represents the multiply operation, *.
    """

    _slots = ((struct, 'left'), (struct, 'right'))


class DivideNode(struct):
    """
    Represents the integer divide operation, //.
    """

    _slots = ((struct, 'left'), (struct, 'right'))


class AddNode(struct):
    """
    Represents the addition operation, +.
    """

    _slots = ((struct, 'left'), (struct, 'right'))


class SubtractNode(struct):
    """
    Represents the addition operation, -.
    """

    _slots = ((struct, 'left'), (struct, 'right'))


class LiteralNode(struct):
    """
    Represents an integral operand node for an operation.
    """

    _slots = ((int, 'val'))


class VariableNode(struct):
    """
    Represents a variable node for an operation.
    """

    _slots = ((str, 'name'))


##############################################################################
# readTable
##############################################################################

def readTable(inFile):
    """
    readTable : str -> dict(key=str, value=int)
    Given an input file of the form:
        varName1 integerValue
        varName2 integerValue
        ...
    Construct and return a dictionary that maps the variable name to its
    integer value.
    """
    d = dict()
    for line in open(inFile):
        line = line.split()
        d[line[0]] = int(line[1])
    return d


##############################################################################
# displayTable
##############################################################################

def displayTable(symTbl):
    """
    displayTable : dict(key=str, value=int) -> NoneType
    Displays the symbol table mapping for variable name to integer value.
    """
    print("Derping the symbol table (variable name => integer value)...")
    for varName in symTbl:
        print(varName + ' => ' + str(symTbl[varName]))


##############################################################################
# parse
##############################################################################

def parse(tokens, i=0):
    """
    parse : tuple(str) * NatNum -> tuple(Node, NatNum) | TypeError

    From an infix stream of tokens, and the current index into the
    token stream, construct and return the tree, as a collection of Nodes,
    that represent the expression.
    If there is an incomplete statement or invalid token, raise a TypeError.

    NOTE: YOU ARE NOT ALLOWED TO MUTATE 'tokens' (e.g. tokens.pop())!!!
          YOU MUST USE 'i' TO GET THE CURRENT TOKEN OUT OF 'tokens'.
    """
    token = tokens[i]
    i += 1
    if token.isdigit():
        return LiteralNode(int(token)), i
    elif token.isidentifier():
        return VariableNode(token), i
    else:
        if token in ['+', '-', '*', '//']:
            left, i = parse(tokens, i)
            right, i = parse(tokens, i)
            if token == '+':
                return AddNode(left, right), i
            if token == '-':
                return SubtractNode(left, right), i
            if token == '*':
                return MultiplyNode(left, right), i
            if token == '//':
                return DivideNode(left, right), i
        else:
            raise TypeError()


##############################################################################
# infix
##############################################################################

def infix(node):
    """
    infix : Node -> str | TypeError
    Perform an infix traversal of the node and return a string that
    represents the infix expression.
    """
    if isinstance(node, LiteralNode):
        return str(node.val)
    elif isinstance(node, VariableNode):
        return node.name
    else:
        if isinstance(node, AddNode):
            return '(' + infix(node.left) + ' + ' + infix(node.right) + ')'
        elif isinstance(node, SubtractNode):
            return '(' + infix(node.left) + ' - ' + infix(node.right) + ')'
        elif isinstance(node, MultiplyNode):
            return '(' + infix(node.left) + ' * ' + infix(node.right) + ')'
        elif isinstance(node, DivideNode):
            return '(' + infix(node.left) + ' // ' + infix(node.right) + ')'


##############################################################################
# compile_tree compiles the expression tree to an executable stack machine.
##############################################################################

def compile_tree(node, symTbl):
    """
    compile_tree : Node * dict(key=str, value=int) -> list( StackOp)
    Given the expression at the node and the symbol table,
    return the list of functions necessary to evaluate the expression
    at some point in the future.
    Precondition: all variable names must exist in symTbl.
    """
    if isinstance(node, LiteralNode):
        return [emitPush(node.val)]
    elif isinstance(node, VariableNode):
        return [emitPush(symTbl[node.name])]
    else:
        if isinstance(node, AddNode):
            return compile_tree(node.left, symTbl) + compile_tree(node.right, symTbl) + [emitAdd()]
        elif isinstance(node, SubtractNode):
            return compile_tree(node.left, symTbl) + compile_tree(node.right, symTbl) + [emitSub()]
        elif isinstance(node, MultiplyNode):
            return compile_tree(node.left, symTbl) + compile_tree(node.right, symTbl) + [emitMul()]
        elif isinstance(node, DivideNode):
            return compile_tree(node.left, symTbl) + compile_tree(node.right, symTbl) + [emitDiv()]


##############################################################################
# main
##############################################################################


def main():
    """
    main : Void -> NoneType
    The main program prompts for the symbol table file, and a prefix
    expression.  It produces the infix expression, and the integer result of
    evaluating the expression.
    """

    print("Hello Herp, welcome to Derp v3.0 :)")

    # construct symbol table
    inFile = input("Herp, enter symbol table file: ")

    # STUDENT: CONSTRUCT AND DISPLAY THE SYMBOL TABLE HERE
    symTbl = readTable(inFile)
    displayTable(symTbl)

    print("Herp, enter prefix expressions, e.g.: + 10 20 (RETURN to quit).")

    # input loop prompts for prefix expressions and produces infix version
    # along with its evaluation
    while True:
        prefixExp = input("derp> ")
        if prefixExp == "":
            break

        # STUDENT: GENERATE A LIST OF TOKENS FROM THE PREFIX EXPRESSION
        tokens = prefixExp.split()

        # STUDENT: CALL parse WITH THE LIST OF TOKENS AND SAVE THE ROOT OF
        # THE PARSE TREE.

        tree, i = parse(tokens)  # replace with a call to your parse here

        # STUDENT: GENERATE THE INFIX EXPRESSION BY CALLING infix AND SAVING
        # THE STRING

        infixResult = infix(tree)  # replace with a call to your infix here

        print("Derping the infix expression: ", infixResult)

        print("JIT compiling the expression")

        # STUDENT: COMPILE THE PARSE TREE BY CALLING compile_tree AND SAVING THE
        # LIST OF BYTE-CODE INSTRUCTIONS

        byteCodes = compile_tree(tree, symTbl)  # replace with a call to your compile_tree here

        # STUDENT: CALL execute ON THE LIST OF BYTE-CODE INSTRUCTIONS
        # AND SAVING THE INTEGER RESULT
        result = execute(byteCodes)
        print("Executing the stack code: ", result)

    print("Goodbye Herp :(")


if __name__ == "__main__":
    main()
