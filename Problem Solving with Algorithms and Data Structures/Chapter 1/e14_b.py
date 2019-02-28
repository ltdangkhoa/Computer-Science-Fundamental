"""
Now design a class to represent a deck of cards.
Using these two classes, implement a favorite card game.
"""
import itertools
from random import random
from math import floor

from e14_a import MyCard


class MyDeck:  # pylint: disable=too-few-public-methods
    """
    deck = MyDeck(num_of_deck=1)
    deck.shuffle_deck()
    deck.get_card(index=1)
    deck.get_length()
    deck.dist_cards(num_of_player, num_of_card)
    deck.hit_card()
    """

    def __init__(self, num_of_deck=1):
        ranks = [x for x in range(1, 14)]
        suites = ['❤', '♦', '♣', '♠']
        self.deck = [] * 52 * num_of_deck
        for suite in suites:
            for rank in ranks:
                for _ in itertools.repeat(None, num_of_deck):
                    self.deck.append(MyCard(rank, suite))


    def __repr__(self):
        return self.deck

    def shuffle_deck(self):
        """@shuffle_deck()"""
        k = len(self.deck)
        while k > 1:
            i = int(floor(random() * k))
            k -= 1
            self.deck[i], self.deck[k] = self.deck[k], self.deck[i]

    def get_card(self, index):
        """@get_card(index)"""
        return self.deck[index]

    def get_length(self):
        """@get_length()"""
        return len(self.deck)

    def dist_cards(self, num_of_player, num_of_card):
        """@dist_cards(num_of_player, num_of_card)"""
        players = [[] for x in range(num_of_player)]
        if num_of_card * num_of_player <= self.get_length():
            for _ in range(num_of_card):
                for player in players:
                    player.append(self.deck.pop())
        else:
            raise ValueError("Too much players or not valid")

        return players

    def hit_card(self):
        """@hit_card()"""
        return self.deck.pop() if self.get_length() > 0 else False
