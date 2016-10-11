"""
file: tour_list.py
language: python 3
author: Duc Duy Phan - ddp3945@rit.edu
description: List Order Strategy implementation - Lab 6 - CSCI-141
"""

import tour_utils


def runListOrderStrategy(places):
    """
    - Using the provided list of place to form a tour
    - Print the tour in the provided order
    - Print the total distance travelled in the tour
    - Draw the path of the tour and mark every place in the tour on a drawing canvas
    :param places: list
    :return: NoneType
    """
    tour_utils.printTour(places)
    tour_utils.printTourDistance(places)
    tour_utils.drawTour(places)


def main():
    """
    - Print a banner with a welcome message
    - Prompt users for a filename
    - Read data about places in the provided file
    - Run the List Order Strategy Algorithm to find out the order of the places in the tour
    - Draw the path of the tour and mark every place in the list on a drawing canvas
    - Wait for the users to respond the the program
    :return: NoneType
    """
    tour_utils.printWelcomeMessage()
    places = tour_utils.readData()
    runListOrderStrategy(places)


main()
