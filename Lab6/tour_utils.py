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
    """
    Return the welcome message
    :return: str
    """
    return 'Welcome to the Dippy Hippie Tour. Get on the bus!'


def DATA_PREFIX():
    """
    Return the prefix of data directory
    :return: str
    """
    return 'data/'


def readFile(filename):
    """
    Read data about places in the provided file, including names and coordinates of places
    :param filename: str
    :return: list
    """
    places = []
    for lines in open(filename):
        lst = lines.split(',')
        for i in range(len(lst)):
            lst[i] = lst[i].strip()
        places.append(Place(lst[0], float(lst[1]), float(lst[2])))
    return places


def initCanvas():
    """
    - Init a drawing canvas of size 600 x 600 and set up a 1000 x 1000 coordinate system
    - Place the turtle in the origin with the pen up
    :return: NoneType
    """
    t.setup(600, 600)
    t.setworldcoordinates(-10, -10, 1010, 1010)
    t.goto(0, 0)
    t.up()


def drawPath(places):
    """
    - Draw the path of the tour in the order of the provided list
    - Mark each place with its name and coordinates of 2 decimal places
    :param places: list
    :return: NoneType
    """
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
    """
    Calculate the Euclidian distance between two points
    :param A: Place
    :param B: Place
    :return: float
    """
    return math.sqrt((A.x - B.x) ** 2 + (A.y - B.y) ** 2)


def calculateTourDistance(places):
    """
    Calculate the total distance travelled in the tour
    :param places: list
    :return: float
    """
    sum = 0
    for i in range(1, len(places)):
        sum += calculatePointsDistance(places[i], places[i - 1])
    return sum


def printWelcomeMessage():
    """
    Print a banner with a welcome message
    :return: NoneType
    """
    print('+' * len(WELCOME_MESSAGE()))
    print(WELCOME_MESSAGE())
    print('+' * len(WELCOME_MESSAGE()))


def readData():
    """
    - Prompt user for a filename
    - Read and store data about places in a list
    :return: list
    """
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
    """
    Print the places in the order of the tour
    :param places: list
    :return: NoneType
    """
    places.append(places[0])
    for i in range(len(places)):
        if i > 0:
            print(' => ', end='')
        print(places[i].name, end='')
    print()


def printTourDistance(places):
    """
    Print the total distance travelled of the tour
    :param places: list
    :return: NoneType
    """
    places.append(places[0])
    print('Distance: ', calculateTourDistance(places))


def drawTour(places):
    """
    - Set up a drawing canvas
    - Draw the path of the tour and mark every place in the tour
    :param places: list
    :return: NoneType
    """
    initCanvas()
    drawPath(places)
    print('Close the canvas window to quit.')
    t.done()
