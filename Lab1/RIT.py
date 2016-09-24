import math
import turtle as t


def initBannerCanvas():
    t.setup(1200, 80)
    t.setworldcoordinates(-5, -5, 455, 35)
    t.reset()
    t.up()
    t.pensize(2)
    t.speed(5)


def drawR():
    # The function draws letter R
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


def drawI():
    # The function draws letter I
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


def drawT():
    # The function draws letter T
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


def drawRIT():
    # The function spells the word RIT
    drawR()
    drawI()
    drawT()


def main():
    initBannerCanvas()
    drawRIT()
    input("Press ENTER to finish the program...")


main()
