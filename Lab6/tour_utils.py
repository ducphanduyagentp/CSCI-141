"""
file: tour_utils.py
language: python 3
author: Duc Duy Phan - ddp3945@rit.edu
description: Utility functions and classes - Lab 6 - CSCI-141
"""

import math
import turtle as t

from rit_lib import *


class Place(struct):
    _slots = ((str, 'name'), (float, 'x'), (float, 'y'))


def WELCOME_MESSAGE():
    return 'Welcome to the Dippy Hippie Tour. Get on the bus!'


def DATA_PREFIX():
    return 'data/'


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
    places.append(places[0])
    for i in range(len(places)):
        place = places[i]
        t.goto(place.x, place.y)
        if i < len(places) - 1:
            t.dot()
            info_str = place.name + '(' + '{:.2f}'.format(place.x) + ', ' + '{:.2f}'.format(place.y) + ')'
            t.write(info_str)
        t.down()
    t.up()


def calculatePointsDistance(A, B):
    return math.sqrt((A.x - B.x) ** 2 + (A.y - B.y) ** 2)


def calculateTourDistance(places):
    sum = 0
    for i in range(1, len(places)):
        sum += calculatePointsDistance(places[i], places[i - 1])
    return sum


def printWelcomeMessage():
    print('+' * len(WELCOME_MESSAGE()))
    print(WELCOME_MESSAGE())
    print('+' * len(WELCOME_MESSAGE()))


def readData():
    filename = input('Enter filename: ')
    places = readFile(DATA_PREFIX() + filename)
    infoString = 'Reading ' + filename + ' ... ' + str(len(places)) + ' place'
    if len(places) < 2:
        infoString += '.'
    else:
        infoString += 's.'
    print(infoString)
    return places


def printTour(places):
    places.append(places[0])
    for i in range(len(places)):
        if i > 0:
            print(' => ', end='')
        print(places[i].name, end='')
    print()


def printTourDistance(places):
    places.append(places[0])
    print('Distance: ', calculateTourDistance(places))


def drawTour(places):
    initCanvas()
    putPlaces(places)
    print('Close the canvas window to quit.')
    t.done()
