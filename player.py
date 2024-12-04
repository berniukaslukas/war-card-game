class Player:
    def __init__(self, name):
        self.name = name
        self.deck = []

    def draw_card(self):
        return self.deck.pop(0) if self.deck else None

    def add_cards(self, cards):
        self.deck.extend(cards)

    def __str__(self):
        return f"{self.name} has {len(self.deck)} cards."
