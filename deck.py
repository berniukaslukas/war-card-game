import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_players=2):
        return [self.cards[i::num_players] for i in range(num_players)]
