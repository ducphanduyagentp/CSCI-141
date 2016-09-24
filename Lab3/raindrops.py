"""
file: raindrops.py
language: python 3
author: Duc Phan - ddp3945@rit.edu
description: Lab 3 - Raindrops
"""

import math
import random
import turtle as t


def PEN_SIZE():
    """Return the turtle's pen size"""
    return 1


def BOX_SIZE():
    """Return the size of the bounding box"""
    return 540


def MAX_COORDINATE():
    """Return the maximum x and y coordinate of the turtle"""
    return BOX_SIZE() / 2


def MAX_RAINDROPS():
    """Return the maximum number of raindrops"""
    return 100


def MAX_RADIUS():
    """Return the maximum radius of the raindrops"""
    return 20


def MIN_RIPPLES():
    """Return the minimum number of ripples"""
    return 3


def MAX_RIPPLES():
    """Return the maximum number of ripples"""
    return 8


def initialize():
    """Set up the pen size and orientation of the turtle before drawing"""
    t.reset()
    t.up()
    t.pensize(PEN_SIZE())
    t.left(90)


def drawBorder():
    """Draw a square bounding box with size of BOX_SIZE() units for the raindrops"""
    t.forward(BOX_SIZE() / 2)
    t.down()
    t.right(90)
    t.forward(BOX_SIZE() / 2)
    t.right(90)
    t.forward(BOX_SIZE())
    t.right(90)
    t.forward(BOX_SIZE())
    t.right(90)
    t.forward(BOX_SIZE())
    t.right(90)
    t.forward(BOX_SIZE() / 2)
    t.up()
    t.left(90)
    t.backward(BOX_SIZE() / 2)


def genRaindropRadius():
    """Generate a random number between 1 and MAX_RADIUS() that represents the raindrop's radius"""
    return random.randint(1, MAX_RADIUS())


def genRaindropPos(r):
    """
    Generate random position of the center of the raindrop with radius r
    so that the raindrop fits in the bounding box
    """
    pos_x = random.randint(-MAX_COORDINATE() + PEN_SIZE() + r, MAX_COORDINATE() - PEN_SIZE() - r)
    pos_y = random.randint(-MAX_COORDINATE() + PEN_SIZE() + r, MAX_COORDINATE() - PEN_SIZE() - r)
    return pos_x, pos_y


def setRandomColor():
    """Set a random fillcolor for the turtle"""
    rand_r = random.random()
    rand_g = random.random()
    rand_b = random.random()
    t.fillcolor(rand_r, rand_g, rand_b)


def genNRipples():
    """
    Generate a random number between MIN_RIPPLES() and MAX_RIPPLES() inclusive
    that represents the number of ripples to be drawn for the raindrop
    """
    return random.randint(MIN_RIPPLES(), MAX_RIPPLES())


def isRippleInside(x, y, r):
    """Determine if the ripple with center of (x, y) and radius of r fits in the drawn bounding box"""
    return -MAX_COORDINATE() < x - r and x + r < MAX_COORDINATE() and -MAX_COORDINATE() < y - r and y + r < MAX_COORDINATE()


def drawOneRaindrop(x, y, r, n):
    """
    Draw a full raindrop including the following components:
        - A circle filled with a random color, the center is at (x, y) and its radius equals to r
        - At most n ripples if all of them completely fits in the bounding box.
          Stop at the last ripples that completely fits in the bounding box.
          All ripples have the same center as the circle.
          The first ripple has the radius of 2 * r
          The distance from one ripple to the next one equals to r
    Pre-conditions:  - pen up
                     - turtle is facing north
                     - turtle is at the center of the last drawn raindrop or at the origin if no raindrop has been drawn
    Post-conditions: - pen up
                     - turtle is facing north
                     - turtle is at position (x, y)
    """
    t.setpos(x, y)
    setRandomColor()
    t.right(90)
    t.forward(r)
    t.left(90)
    t.down()
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.up()
    t.right(90)
    t.backward(r)
    t.left(90)
    currentRippleRadius = 2 * r
    while isRippleInside(x, y, currentRippleRadius) and n > 0:
        t.right(90)
        t.forward(currentRippleRadius)
        t.left(90)
        t.down()
        t.circle(currentRippleRadius)
        t.up()
        t.right(90)
        t.backward(currentRippleRadius)
        t.left(90)
        currentRippleRadius = currentRippleRadius + r
        n = n - 1


def drawRaindrops(numRaindrops):
    """
    - The function uses recursion to draw numRaindrops raindrops
      with random centers, radius, fillcolors and number of ripples, all fit in the bounding box
    - The recursive function returns the area of all the drawn raindrops.
    """
    if numRaindrops == 0:
        return 0
    else:
        r = genRaindropRadius()
        x, y = genRaindropPos(r)
        nRipples = genNRipples()
        drawOneRaindrop(x, y, r, nRipples)
        return math.pi * r * r + drawRaindrops(numRaindrops - 1)


def main():
    """
    - Prompt user for the number of raindrops
    - Validate the input. If the input is not in the range [1-100] inclusive, inform the user and exit the program
    - Setup the pen size and the orientation of the turtle
    - Draw a bounding box of size BOX_SIZE() for the raindrops
    - Draw the required number of raindrops
    - Print the total area of the drawn raindrops
    - Bring the turtle to (0, 0), facing north
    - Wait for the user to respond
    """
    nRaindrops = int(input("Please input number of raindrops [1 - 100]: "))
    if not 1 <= nRaindrops <= MAX_RAINDROPS():
        print("The number of raindrops must be between 1 and 100 inclusive")
    else:
        initialize()
        drawBorder()
        sum = drawRaindrops(nRaindrops)
        t.setpos(0, 0)
        print("The total area of the raindrops is", sum, "square units", sep=' ')
        t.done()


main()
