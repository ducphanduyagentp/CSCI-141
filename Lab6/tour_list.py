"""
file: tour_list.py
language: python 3
author: Duc Duy Phan - ddp3945@rit.edu
description: List Order Strategy implementation - Lab 6 - CSCI-141
"""

import tour_utils


def runListOrderStrategy(places):
    tour_utils.printTour(places)
    tour_utils.printTourDistance(places)
    tour_utils.drawTour(places)


def main():
    tour_utils.printWelcomeMessage()
    places = tour_utils.readData()
    runListOrderStrategy(places)


main()
