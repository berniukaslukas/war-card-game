from deck import Deck
from player import Player

class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player("Player 1"), Player("Player 2")]
        self.round = 1

    def setup(self):
        print("Shuffling and dealing the deck...")
        self.deck.shuffle()
        player_hands = self.deck.deal()
        for i, player in enumerate(self.players):
            player.deck = player_hands[i]
        print("Game setup complete!")

    def play_round(self):
        print(f"\n--- Round {self.round} ---")
        cards_on_table = []

        for player in self.players:
            card = player.draw_card()
            if card:
                print(f"{player.name} plays {card}")
                cards_on_table.append((card, player))
            else:
                print(f"{player.name} has no more cards!")
                return None

        card1, player1 = cards_on_table[0]
        card2, player2 = cards_on_table[1]

        if card1.value > card2.value:
            print(f"{player1.name} wins this round!")
            player1.add_cards([card1, card2])
        elif card2.value > card1.value:
            print(f"{player2.name} wins this round!")
            player2.add_cards([card1, card2])
        else:
            print("War!")
            self.handle_war(cards_on_table)

        self.round += 1

    def handle_war(self, cards_on_table):
        war_cards = cards_on_table[:]

        for player in self.players:
            for _ in range(4):
                card = player.draw_card()
                if card:
                    war_cards.append((card, player))
                else:
                    print(f"{player.name} doesn't have enough cards for war!")
                    return

        # Compare the final cards
        final_card1, player1 = war_cards[-2]
        final_card2, player2 = war_cards[-1]

        if final_card1.value > final_card2.value:
            print(f"{player1.name} wins the war!")
            player1.add_cards([card for card, _ in war_cards])
        elif final_card2.value > final_card1.value:
            print(f"{player2.name} wins the war!")
            player2.add_cards([card for card, _ in war_cards])
        else:
            print("Another tie! War continues...")
            self.handle_war(war_cards)

    def play_game(self):
        self.setup()
        while all(player.deck for player in self.players):
            self.play_round()
            if self.round > 1000:
                print("The game is taking too long. Declaring a draw!")
                break


        player1, player2 = self.players
        if len(player1.deck) > len(player2.deck):
            print(f"{player1.name} wins the game!")
        elif len(player2.deck) > len(player1.deck):
            print(f"{player2.name} wins the game!")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    game = Game()
    game.play_game()
