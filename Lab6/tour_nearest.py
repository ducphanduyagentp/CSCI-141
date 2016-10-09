"""
file: tour_nearest.py
language: python 3
author: Duc Duy Phan - ddp3945@rit.edu
description: Nearest Neighbor Order implementation - Lab 6 - CSCI-141
"""

import tour_utils


def findNearestNeighbor(point, places, start):
    min_distance = tour_utils.calculatePointsDistance(point, places[start])
    min_index = start
    for i in range(start, len(places)):
        current_distance = tour_utils.calculatePointsDistance(point, places[i])
        if current_distance < min_distance:
            min_distance = current_distance
            min_index = i
    return min_index


def runNearestNeighbor(places):
    for i in range(1, len(places) - 1):
        min_index = findNearestNeighbor(places[i - 1], places, i)
        places[i], places[min_index] = places[min_index], places[i]

    tour_utils.printTour(places)
    tour_utils.printTourDistance(places)
    tour_utils.drawTour(places)


def main():
    tour_utils.printWelcomeMessage()
    places = tour_utils.readData()
    runNearestNeighbor(places)


main()
