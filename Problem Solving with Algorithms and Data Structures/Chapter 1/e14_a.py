"""
Design a class to represent a playing card
"""


class MyCard:  # pylint: disable=too-few-public-methods
    """
    Require for suite and rank for a card
    card = MyCard(2, '❤')
    card.rank
    card.suite
    """

    def __init__(self, _rank, _suite):
        ranks = [x for x in range(1, 14)]
        suites = ['❤', '♦', '♣', '♠']
        if _rank in ranks and _suite in suites:
            self.rank = _rank
            self.suite = _suite
        else:
            raise IOError("Invalid card")

    def __repr__(self):
        return str(self.rank) + str(self.suite)
