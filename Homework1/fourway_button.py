"""
file: fourway_button.py
language: python3
author: Duc Duy Phan - ddp3945@rit.edu
description: Homework 1 - Use turtle graphics to draw a four-way button
"""

import turtle as t


def initialize():
    """Initialize the turtle so that it is facing North with the pen up"""
    t.up()
    t.left(90)


def drawBorder():
    """Draw a square with sides of 180 units for the outline of the figure"""
    t.forward(90)
    t.right(90)
    t.down()
    t.forward(90)
    t.right(90)
    t.forward(180)
    t.right(90)
    t.forward(180)
    t.right(90)
    t.forward(180)
    t.right(90)
    t.forward(90)
    t.left(90)
    t.up()
    t.backward(90)


def drawButton():
    """Draw a circle with the radius of 20 units"""
    t.right(90)
    t.forward(20)
    t.left(90)
    t.down()
    t.circle(20)
    t.up()
    t.left(90)
    t.forward(20)
    t.right(90)


def drawTriangle():
    """Draw an equilateral triangle with sides of 40 units"""
    t.forward(60)
    t.down()
    t.left(90)
    t.forward(20)
    t.right(120)
    t.forward(40)
    t.right(120)
    t.forward(40)
    t.right(120)
    t.forward(20)
    t.right(90)
    t.up()
    t.backward(60)


def drawTriangles():
    """Draw 4 equilateral triangles with sides of 40 units in each corner of the square"""
    t.left(45)
    drawTriangle()
    t.left(90)
    drawTriangle()
    t.left(90)
    drawTriangle()
    t.left(90)
    drawTriangle()
    t.left(45)


def drawFourwayButton():
    """Draw a four-way button"""
    drawBorder()
    drawTriangles()
    drawButton()


def main():
    """The program creates a picture canvas, draws a four-way button including
       a circle, a square and four equilateral triangles, and
       waits for the user to respond before terminating.
    """
    initialize()
    drawFourwayButton()
    t.done()


# Call the main function to run the program
main()
