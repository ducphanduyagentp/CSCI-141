import turtle as t


def drawSquare(depth, length):
    if depth <= 0:
        pass
    else:
        t.forward(length)
        t.left(90)

        drawSquare(depth - 1, length / 3)
        t.forward(length)
        t.left(90)
        t.forward(length)
        t.left(90)
        drawSquare(depth - 1, length / 3)
        t.forward(length)
        t.left(90)


maxsize = 100
depth = int(input())
drawSquare(depth, maxsize)
t.done()
