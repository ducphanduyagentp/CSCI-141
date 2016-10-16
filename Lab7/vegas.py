"""
file: vegas.py
language: python 3
author: Duc Phan - ddp3945@rit.edu
description: Implementation and simulation for Lab #7 - CSCI-141
"""

import random

from myQueue import *
from myStack import *


def shuffle(deck):
    """
    Return a random card from the given deck
    :param deck: Queue
    :return: int
    """
    nShuffle = random.randint(0, deck.size - 1)
    for i in range(nShuffle):
        enqueue(deck, front(deck))
        dequeue(deck)
    frontCard = front(deck)
    dequeue(deck)
    return frontCard


def createShuffledDeck(nCard):
    """
    Create a random shuffled deck of nCard cards and store it in a queue
    :param nCard: int
    :return: Queue
    """
    deck = createQueue()
    for i in range(1, nCard + 1):
        enqueue(deck, i)
    shuffled_deck = createQueue()
    for i in range(nCard):
        enqueue(shuffled_deck, shuffle(deck))
    return shuffled_deck


def simulateGame(deck):
    """
    - Simulate a game with a given deck
    - Return the size of the victory pile in the current simulation
    - The idea of this strategy is to maintain the discard_pile1 as the discard pile
    with the smallest card on top at every point of the game. For every round, try to take the cards
    from tops of the discard piles and put it onto the victory pile before putting the next card
    in the deck onto one of the discard piles or the victory pile.
    :param deck: Queue
    :return: int
    """
    victory_pile = createStack()
    discard_pile1 = createStack()
    discard_pile2 = createStack()
    next_card = 1
    notgameOver = True
    while notgameOver:
        while True:  # Check if any of the cards on both discard piles can be put in the victory pile
            takeFromDiscardPile = False
            if not emptyStack(discard_pile1):
                if top(discard_pile1) == next_card:
                    push(victory_pile, top(discard_pile1))
                    pop(discard_pile1)
                    next_card += 1
                    takeFromDiscardPile = True
            if not emptyStack(discard_pile2):
                if top(discard_pile2) == next_card:
                    push(victory_pile, top(discard_pile2))
                    pop(discard_pile2)
                    next_card += 1
                    takeFromDiscardPile = True
            if not takeFromDiscardPile:
                break

        if not emptyQueue(deck):
            card = front(deck)
            dequeue(deck)
            if card == next_card:  # Put the top card of the deck onto the victory pile if possible
                push(victory_pile, card)
                next_card += 1
                continue
            if emptyStack(discard_pile1):
                push(discard_pile1, card)
            elif card < top(discard_pile1):
                # Maintain the discard_pile1 with the smallest possible card on top
                push(discard_pile1, card)
            else:
                push(discard_pile2, card)
        else:
            notgameOver = takeFromDiscardPile
    return victory_pile.size


def main():
    """
    - Prompt users for the number of cards in the deck
    - Prompt users for the number of games to simulation
    - Create a random deck in every simulation and play the game with the given rules
    - Print the average victory pile size
    - Print the maximum victory pile size
    - Print the minimum victory pile size
    :return: NoneType
    """
    nCard = int(input('Enter number of cards to use: '))
    nGame = int(input('Enter number of games to simulate: '))
    min_num = nCard
    max_num = 0
    sum = 0
    for i in range(nGame):
        deck = createShuffledDeck(nCard)
        n_victory = simulateGame(deck)
        if n_victory < min_num:
            min_num = n_victory
        if n_victory > max_num:
            max_num = n_victory
        sum += n_victory

    print('Average victory pile size: ', sum / nGame)
    print('Max victory pile size: ', max_num)
    print('Min victory pile size: ', min_num)


main()
