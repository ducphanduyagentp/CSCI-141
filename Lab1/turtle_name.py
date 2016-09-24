"""
File: turtle_name.py
Language: python3
Author: Duc Phan - ddp3945@rit.edu
Description: Lab 1 - CSCI-141 - Typography

Design description:
   - Each character is fitted in a 20 x 20 square
   - Initial orientation of the turtle: Facing East
   - The turtle always starts from the bottom-left corner of the 20 x 20 square
     that contains the character with the pen up and facing East.
   - After drawing a character, the turtle is 10 units from the bottom-right corner
     of the square that contains the last character with the pen up and facing East,
     ready to draw the next character.
"""

import math
import turtle as t


def initBannerCanvas():
    """
    Set up the drawing canvas to draw a banner of 22 characters
    Set a window to fit 1 line for the number of characters
    """
    # The setup function makes the drawing canvas wide and short
    t.setup(1200, 80)

    # Set the world coordinates to start turtle in lower left and match the number of characters.
    # The function setworldcoordinates moves the origin to the lower left
    # with 5 units of margin around where the characters will go
    # setworldcoordinates( -5, -5, 30 * 22 + 5, 30 + 5)
    t.setworldcoordinates(-5, -5, 665, 35)
    t.reset()
    t.up()
    t.pensize(2)
    t.speed(5)


def drawDot():
    """Draw a dot of the turtle's pen size"""
    t.forward(10)
    t.dot()
    t.forward(20)


def drawAtSymbol():
    """Draw the '@' symbol"""
    t.forward(5)
    t.down()
    t.left(135)
    length_1 = math.sqrt(50)
    t.forward(length_1)
    t.right(45)
    t.forward(10)
    t.right(45)
    t.forward(length_1)
    t.right(45)
    t.forward(10)
    t.right(45)
    t.forward(length_1)
    t.right(45)
    t.forward(10)
    t.right(45)
    t.forward(length_1)
    t.right(45)
    t.forward(5 + 2.5)
    t.right(45)
    length_2 = math.sqrt(2 * 2.5 * 2.5)
    t.forward(length_2)
    t.right(45)
    t.forward(5)
    t.right(45)
    t.forward(length_2)
    t.right(45)
    t.forward(5)
    t.right(45)
    t.forward(length_2)
    t.right(45)
    t.forward(5)
    t.right(45)
    t.forward(length_2)
    t.left(135)
    t.up()
    t.forward(17.5)


def draw3():
    """Draw number 3"""
    t.down()
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.backward(10)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(20)
    t.up()
    t.backward(30)
    t.left(90)
    t.forward(20)
    t.left(90)


def draw4():
    """Draw number 4"""
    t.forward(20)
    t.left(90)
    t.down()
    t.forward(20)
    t.backward(10)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(10)
    t.up()
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.left(90)


def draw5():
    """Draw number 5"""
    t.down()
    t.forward(20)
    t.left(90)
    t.forward(5)
    t.left(45)
    t.forward(math.sqrt(50))
    t.left(45)
    t.forward(15)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(20)
    t.up()
    t.forward(10)
    t.right(90)
    t.forward(20)
    t.left(90)


def draw9():
    """Draw number 9"""
    t.down()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(20)
    t.up()
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.left(90)


def drawD():
    """Draw letter D"""
    t.down()
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(15)
    t.right(45)
    t.forward(math.sqrt(50))
    t.right(45)
    t.forward(10)
    t.right(45)
    t.forward(math.sqrt(50))
    t.right(45)
    t.forward(15)
    t.up()
    t.left(180)
    t.forward(30)


def drawE():
    """Draw letter E"""
    t.down()
    t.forward(20)
    t.backward(20)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.backward(10)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.forward(20)
    t.up()
    t.forward(10)
    t.right(90)
    t.forward(20)
    t.left(90)


def drawI():
    """Draw letter I"""
    t.down()
    t.forward(20)
    t.backward(10)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.backward(20)
    t.up()
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(10)


def drawL():
    """Draw letter L"""
    t.down()
    t.left(90)
    t.forward(20)
    t.backward(20)
    t.right(90)
    t.forward(20)
    t.up()
    t.forward(10)


def drawP():
    """Draw letter P"""
    t.down()
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(20)
    t.up()
    t.backward(30)
    t.left(90)
    t.forward(10)
    t.left(90)


def drawR():
    """Draw letter R"""
    t.down()
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(20)
    t.left(90)
    angle_r = math.degrees(math.atan(2))
    t.left(angle_r)
    t.forward(math.sqrt(500))
    t.left(90 - angle_r)
    t.up()
    t.forward(10)


def drawT():
    """Draw letter T"""
    t.forward(10)
    t.left(90)
    t.down()
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.backward(20)
    t.up()
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(10)


def drawU():
    """Draw letter U"""
    t.left(90)
    t.down()
    t.forward(20)
    t.backward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.up()
    t.backward(20)
    t.right(90)
    t.forward(10)


def drawTURTLE():
    """Draw the word 'TURTLE'"""
    drawT()
    drawU()
    drawR()
    drawT()
    drawL()
    drawE()


def drawRIT():
    """Draw the word 'RIT'"""
    drawR()
    drawI()
    drawT()


def drawEDU():
    """Draw the word 'EDU'"""
    drawE()
    drawD()
    drawU()


def drawUsername():
    """Draw the username 'DDP3945'"""
    drawD()
    drawD()
    drawP()
    draw3()
    draw9()
    draw4()
    draw5()


def drawName():
    """
    Draw the required phrase: TURTLE <Username>@RIT.EDU
    There is space character between the phrase 'TURTLE' and the username
    """
    drawTURTLE()
    t.forward(20)
    drawUsername()
    drawAtSymbol()
    drawRIT()
    drawDot()
    drawEDU()


def testFunction():
    """
    - The test function sets the turtle's speed to 2,
    prints the initial position of the turtle and then draws random letters or phrases.
    - The test function resets the turtle's position to (0.0, 0.0) and
    clears the canvas after 1 - 3 drawing function call.
    - After each drawing function call, the test function prints the current position of the turtle
    for the user to assure that the turtle is in the right position to draw next letter/phrase.
    - If the turtle is in the right position, the x-cooridinates of the printed positions
    should be divisible by 30.
    """
    t.speed(2)
    initBannerCanvas()
    print(t.position())
    drawU()
    print(t.position())
    drawI()
    print(t.position())
    drawE()
    print(t.position())
    t.clear()
    t.setposition(0.0, 0.0)
    draw3()
    print(t.position())
    drawUsername()
    print(t.position())
    t.clear()
    t.setposition(0.0, 0.0)
    drawAtSymbol()
    print(t.position())
    drawRIT()
    print(t.position())
    t.clear()
    t.setposition(0.0, 0.0)
    drawTURTLE()
    print(t.position())
    drawDot()
    print(t.position())
    draw4()
    print(t.position())
    t.clear()
    t.setposition(0.0, 0.0)
    drawP()
    print(t.position())
    drawR()
    print(t.position())
    t.clear()
    t.setposition(0.0, 0.0)
    input("Press ENTER to finish the test...")


def main():
    """
    The program creates a wide and short drawing canvas, draws the required phrase
    and wait for the user to respond
    """
    initBannerCanvas()
    drawName()
    input("Press ENTER to finish the program...")


main()
