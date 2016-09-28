"""
file: shapy_turtle.py
language: python 3
author: Duc Duy Phan - ddp3945@rit.edu
description: Lab 4 - ShapyTurtle - Strings Lab
"""

import turtle as t


def extract_num(s):
    """
    Extract the number from a string that begins with digits
    :param s: string
    :return: (int, int) or (None, None)
    """
    if len(s) == 0 or not s[0].isdigit():
        return (None, None)
    for i in range(len(s)):
        if not s[i].isdigit():
            return int(s[:i]), i
    return (int(s), len(s))


def processLeft(s):
    """
    Process ShapyTurtle command '<'
    :param s: string
    :return: int or None
    """
    num, lnum = extract_num(s[1:])
    if num == None:
        return None
    t.left(num)
    return lnum


def processRight(s):
    """
    Process ShapyTurtle command '>'
    :param s: string
    :return: int or None
    """
    num, lnum = extract_num(s[1:])
    if num == None:
        return None
    t.right(num)
    return lnum


def processS(s):
    """
    Process ShapyTurtle command 'S'
    :param s: string
    :return: int or None
    """
    num, lnum = extract_num(s[1:])
    if num == None:
        return None
    for i in range(4):
        t.left(90)
        t.forward(num)
    return lnum


def processT(s):
    """
    Process ShapyTurtle command 'T'
    :param s: string
    :return: int or None
    """
    num, lnum = extract_num(s[1:])
    if num == None:
        return None
    for i in range(3):
        t.left(120)
        t.forward(num)
    return lnum


def processC(s):
    """
    Process ShapyTurtle command 'C'
    :param s: string
    :return: int or None
    """
    num, lnum = extract_num(s[1:])
    if num == None:
        return None
    t.circle(num)
    return lnum


def processF(s):
    """
    Process ShapyTurtle command 'F'
    :param s: string
    :return: int or None
    """
    num, lnum = extract_num(s[1:])
    if num == None:
        return None
    t.forward(num)
    return lnum


def processB(s):
    """
    Process ShapyTurtle command 'B'
    :param s: string
    :return: int or None
    """
    num, lnum = extract_num(s[1:])
    if num == None:
        return None
    t.backward(num)
    return lnum


def processU():
    """
    Process ShapyTurtle command 'U'
    :return: None
    """
    t.up()


def processD():
    """
    Process ShapyTurtle command 'D'
    :return: None
    """
    t.down()


def processZ(s):
    """
    Process ShapyTurtle command 'Z'
    :param s: string
    :return: int or None
    """
    num, lnum = extract_num(s[1:])
    if num == None:
        return None
    if num == 0:
        t.color('red')
    elif num == 1:
        t.color('blue')
    elif num == 2:
        t.color('green')
    elif num == 3:
        t.color('yellow')
    elif num == 4:
        t.color('brown')
    else:
        t.color('black')
    return lnum


def processR(s):
    """
    Process ShapyTurtle command 'R'
    :param s: string
    :return: int or None
    """
    length, lnum1 = extract_num(s[1:])
    if length == None:
        return None
    width, lnum2 = extract_num(s[2 + lnum1:])
    if width == None:
        return None
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(width)
    return lnum1 + lnum2 + 1


def processP(s):
    """
    Process ShapyTurtle command 'P'
    :param s: string
    :return: int or None
    """
    num1, lnum1 = extract_num(s[1:])
    if num1 == None or num1 < 3:
        return None
    num2, lnum2 = extract_num(s[2 + lnum1:])
    if num2 == None:
        return None
    angle = 180 - 180 * (num1 - 2) / num1
    for i in range(num1):
        t.left(angle)
        t.forward(num2)
    return lnum1 + lnum2 + 1


def processG(s):
    num1, lnum1 = extract_num(s[1:])
    if num1 == None:
        return None
    num2, lnum2 = extract_num(s[2 + lnum1:])
    if num2 == None:
        return None
    t.goto(num1, num2)
    return lnum1 + lnum2 + 1


def processShapyTurtle(s):
    """
    Process ShapyTurtle commands
    :param s: string
    :return: int or None
    """
    i = 0
    while i < len(s):
        flag = 0
        if s[i] == '<':
            flag = processLeft(s[i:])
        elif s[i] == '>':
            flag = processRight(s[i:])
        elif s[i] == 'S':
            flag = processS(s[i:])
        elif s[i] == 'T':
            flag = processT(s[i:])
        elif s[i] == 'C':
            flag = processC(s[i:])
        elif s[i] == 'F':
            flag = processF(s[i:])
        elif s[i] == 'B':
            flag = processB(s[i:])
        elif s[i] == 'U':
            processU()
        elif s[i] == 'D':
            processD()
        elif s[i] == 'R':
            flag = processR(s[i:])
        elif s[i] == 'P':
            flag = processP(s[i:])
        elif s[i] == 'G':
            flag = processG(s[i:])
        elif s[i] == 'Z':
            flag = processZ(s[i:])
        else:
            print('Error while processing this command:', s[i:], sep=' ')
            return None
        if flag == None:
            print('Error while processing this command:', s[i:], sep=' ')
            return None
        i = i + flag + 1
    return 0


def main():
    """
    Prompt users for a string of ShapyTurtle commands and process it
    :return: None
    """
    s = input('Please input ShapyTurtle command: ')
    flag = processShapyTurtle(s)
    if flag == None:
        return
    t.done()


main()
