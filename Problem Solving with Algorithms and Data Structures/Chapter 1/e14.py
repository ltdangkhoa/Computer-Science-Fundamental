
from e14_b import MyDeck, MyCard

def demo_a():
    card_2_heart = MyCard(2, '❤')
    print(card_2_heart)
    card_3_diamond = MyCard(3, '♦')
    print(card_3_diamond)
    card_13_spade = MyCard(13, '♠')
    print(card_13_spade)

def demo_b():
    cards_deck = MyDeck(num_of_deck=1)
    cards_deck.shuffle_deck()
    print(cards_deck.get_length())

    num_of_player = 3
    num_of_card = 2
    players = cards_deck.dist_cards(num_of_player, num_of_card)
    print(players)

    for player_cards in players:
        sum_cards = sum(card.rank for card in player_cards)
        while sum_cards < 18 and len(player_cards) < 5:
            card_hit = cards_deck.hit_card()
            player_cards.append(card_hit)
            sum_cards = sum(card.rank for card in player_cards)

    print(players)

# demo_a()
demo_b()
