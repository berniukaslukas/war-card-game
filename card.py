class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    values = {rank: index for index, rank in enumerate(ranks, start=2)}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"
