import turtle as t

from rit_lib import *


class Place(struct):
    _slots = ((str, 'name'), (float, 'x'), (float, 'y'))


def readFile(filename):
    places = []
    for lines in open(filename):
        lst = lines.split(',')
        for i in range(len(lst)):
            lst[i] = lst[i].strip()
        places.append(Place(lst[0], float(lst[1]), float(lst[2])))
    return places


def initCanvas():
    t.setup(600, 600)
    t.setworldcoordinates(-10, -10, 1010, 1010)
    t.goto(0, 0)
    t.up()


def putPlaces(places):
    for place in places:
        t.goto(place.x, place.y)
        t.dot()
        info_str = place.name + '(' + '{:.2f}'.format(place.x) + ', ' + '{:.2f}'.format(place.y) + ')'
        t.write(info_str)


def main():
    filename = input("Please input filename: ")
    places = readFile(filename)
    initCanvas()
    putPlaces(places)
    t.done()

# main()
