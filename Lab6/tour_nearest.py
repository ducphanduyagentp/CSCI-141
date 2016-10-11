"""
file: tour_nearest.py
language: python 3
author: Duc Duy Phan - ddp3945@rit.edu
description: Nearest Neighbor Order implementation - Lab 6 - CSCI-141
"""

import tour_utils


def findNearestNeighbor(point, places, start):
    """
    Find in the list, starting from the specified index to the end of the list,
    the nearest place to the provided point
    :param point: Place
    :param places: list
    :param start: int
    :return: int
    """
    min_distance = tour_utils.calculatePointsDistance(point, places[start])
    min_index = start
    for i in range(start, len(places)):
        current_distance = tour_utils.calculatePointsDistance(point, places[i])
        if current_distance < min_distance:
            min_distance = current_distance
            min_index = i
    return min_index


def runNearestNeighbor(places):
    """
    - Find the order of the tour based on provided criteria (going to the closest next place at every point
    on the tour)
    - Print the tour in the found order
    - Print the total distance travelled in the tour
    - Draw the path of the tour and mark every place in the tour on a drawing canvas
    :param places: list
    :param places: list
    :return: NoneType
    """
    for i in range(1, len(places) - 1):
        min_index = findNearestNeighbor(places[i - 1], places, i)
        places[i], places[min_index] = places[min_index], places[i]

    tour_utils.printTour(places)
    tour_utils.printTourDistance(places)
    tour_utils.drawTour(places)


def main():
    """
    - Print a banner with a welcome message
    - Prompt users for a filename
    - Read data about places in the provided file
    - Run the Nearest Neighbor Order Algorithm to find out the order of the places in the tour
    - Draw the path of the tour and mark every place in the list on a drawing canvas
    - Wait for the users to respond the the program
    :return: NoneType
    """
    tour_utils.printWelcomeMessage()
    places = tour_utils.readData()
    runNearestNeighbor(places)


main()
