"""
file: bowties.py
language: python 3
author: Duc Duy Phan - ddp3945@rit.edu
description: Lab 2 - CSCI-141 - Bow Ties
"""

import turtle as t


def initialize():
    """
    Set up a square drawing canvas of 720 x 720 units
    Initialize the turtle's pen size.
    """
    t.setup(720, 720)
    t.up()
    t.pensize(3)


def drawOneBowtie(len):
    """
    Description: The function draws a bowtie including 2 equilateral triangles with the size length of len
    and one circle with the radius of len/4.
    The outline is black and the circle is filled with red color.
    Pre-conditions: turtle is facing east (relatively to the bowtie that the turtle
                    is going to draw), pen up
    Post-condition: turtle is facing east (relatively to the bowtie that the turtle
                    has just drawn), pen up
    """
    t.down()
    t.right(30)
    t.backward(len)
    t.right(60)
    t.forward(len)
    t.left(120)
    t.forward(2 * len)
    t.right(120)
    t.forward(len)
    t.right(120)
    t.forward(len)
    t.right(150)
    t.up()
    t.forward(len / 4)
    t.left(90)
    t.pencolor("black")
    t.fillcolor("red")
    t.down()
    t.begin_fill()
    t.circle(len / 4)
    t.end_fill()
    t.up()
    t.right(90)
    t.backward(len / 4)


def drawBowties(depth, len):
    """
    Description: Draw the required figure with the largest bowtie has the side of length len.
    For each successive level, the bowties decrease in size by a factor of 3.
    The circle has the radius equal to 1/4 the length of the side of the triangle.
    Pre-conditions: turtle is at the origin, facing east, pen up.
    Post-conditions: turtle is at the origin, facing east, pen up.
    """
    if depth == 0:
        pass
    else:
        drawOneBowtie(len)
        t.right(30)
        t.backward(2 * len)
        drawBowties(depth - 1, len / 3)
        t.forward(4 * len)
        drawBowties(depth - 1, len / 3)
        t.backward(2 * len)
        t.left(60)
        t.forward(2 * len)
        drawBowties(depth - 1, len / 3)
        t.backward(4 * len)
        drawBowties(depth - 1, len / 3)
        t.forward(2 * len)
        t.right(30)


def main():
    """
    - Set up a square drawing canvas of 720 x 720 units
    - Prompt for recursive depth
    - Use recursion to draw the required figure with recursive depth of the input
    - Wait for users to respond to the program
    """
    initialize()
    depth = int(input("Please input recursive depth: "))
    drawBowties(depth, 120)
    t.done()


main()
