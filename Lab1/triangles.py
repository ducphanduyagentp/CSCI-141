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
    t.setup(1200, 80)
    t.setworldcoordinates(-5, -5, 680, 35)
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
    """Draw the required phrase: TURTLE <Username>@RIT.EDU"""
    drawTURTLE()
    t.forward(20)
    drawUsername()
    drawAtSymbol()
    drawRIT()
    drawDot()
    drawEDU()


def testFunction():
    pass


def main():
    initBannerCanvas()
    drawName()
    input("Press ENTER to finish the program...")


main()
