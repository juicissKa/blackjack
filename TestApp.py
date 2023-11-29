import tkinter.messagebox
import unittest
from main import App, Deck, Card, Player, Dealer, Table
from unittest.mock import patch, Mock
import tkinter
import os

class TestApp(unittest.TestCase):
    def setUp(self):
        self.table = Table()
        self.player = self.table.player
        self.dealer = self.table.dealer
        self.deck = self.table.deck

        self.deck.card_list = self.deck.reset()
        self.deck.card_list = self.deck.initialize_card_list()
        print([card.__str__() for card in self.deck.card_list])
        self.player.reset()
        self.dealer.reset()


    # integration
    def test_table_hit(self):
        self.table.hit()
        self.assertEqual(len(self.player.hand), 1)
        self.assertEqual(self.deck.popped_cards[0], self.player.hand[0])

    def test_table_hold(self):
        self.table.hold()
        self.assertGreaterEqual(self.dealer.card_count, 17)
        self.assertEqual(len(self.dealer.hand), len(self.deck.popped_cards))

    def test_table_draw(self):
        self.player.get_card(self.deck.pop_card())
        self.player.get_card(self.deck.pop_card())
        self.deck.pop_card()
        self.dealer.get_card(self.deck.pop_card())
        result = self.table.get_result()

        self.assertEqual(result, 'draw')

class TestTable(unittest.TestCase):
    def setUp(self):
        self.table = Table()
        self.player = self.table.player
        self.dealer = self.table.dealer

    def test_get_result(self):
        self.player.card_count = 21
        self.dealer.card_count = 21
        self.assertEqual(self.table.get_result(), 'draw')

        self.player.card_count = 21
        self.dealer.card_count = 20
        self.assertEqual(self.table.get_result(), 'win')

        self.player.card_count = 20
        self.dealer.card_count = 21
        self.assertEqual(self.table.get_result(), 'lose')

        self.player.card_count = 22
        self.dealer.card_count = 22
        self.assertEqual(self.table.get_result(), 'lose')

    def test_start_game(self):
        self.player.reset()
        self.dealer.reset()

        self.table._Table__start_game()
        self.assertEqual(len(self.player.hand), 2)
        self.assertEqual(len(self.dealer.hand), 2)

    def test_restart(self):
        self.table.restart()

        self.assertEqual(len(self.player.hand), 2)
        self.assertEqual(len(self.dealer.hand), 2)

class TestPlayer(unittest.TestCase):
        def setUp(self):
            self.player = Player('Игрок')

        def test_get_card_default(self):
            self.player.get_card(Card(suit='♦', value=2))
            self.assertEqual(self.player.hand, [Card(suit='♦', value=2)])
            self.assertEqual(self.player.card_count, 2)
            self.assertEqual(self.player.ace_count, 0)

        def test_get_card_ace(self):
            self.player.get_card(Card(suit='♦', value='A'))
            self.assertEqual(self.player.hand, [Card(suit='♦', value='A')])
            self.assertEqual(self.player.card_count, 11)
            self.assertEqual(self.player.ace_count, 1)

        def test_get_card_double_ace(self):
            self.player.get_card(Card(suit='♦', value='A'))
            self.player.get_card(Card(suit='♠', value='A'))
            self.assertEqual(self.player.hand, [Card(suit='♦', value='A'), Card(suit='♠', value='A')])
            self.assertEqual(self.player.card_count, 12)
            self.assertEqual(self.player.ace_count, 1)

        def test_reset(self):
            self.player.reset()
            self.assertEqual(self.player.hand, [])
            self.assertEqual(self.player.card_count, 0)
            self.assertEqual(self.player.ace_count, 0)

        def test_str(self):
            self.player.get_card(Card(suit='♦', value='A'))

            self.assertEqual(self.player.__str__(), f"Имя: Игрок, Рука: A ♦, Счёт: 11")


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_initialize_card_list(self):
        self.assertEqual(self.deck.initialize_card_list(), [Card(value=v, suit=s)
                          for s in ['♥', '♠', '♣', '♦']
                          for v in [2, 3, 4, 5, 6, 7, 8, 9, 10,
                                    'J', 'Q', 'K', 'A']])

    def test_shuffle(self):
        before_shuffle = self.deck.card_list.copy()
        self.deck.shuffle()
        self.assertEqual(len(self.deck.card_list), len(before_shuffle))
        self.assertNotEqual(self.deck.card_list, before_shuffle)

    def test_pop_card(self):
        pop_card = self.deck.card_list[0]
        before_popped = self.deck.popped_cards.copy()
        self.assertEqual(self.deck.pop_card(), pop_card)
        before_popped.append(pop_card)
        self.assertEqual(self.deck.popped_cards, before_popped)

    def test_reset(self):
        self.deck.reset()
        self.assertEqual(len(self.deck.card_list), 52)
        self.assertEqual(len(self.deck.popped_cards), 0)

    def test_str(self):
        self.assertEqual(self.deck.__str__(), str([card.__str__() for card in self.deck.card_list]))


class CardTest(unittest.TestCase):
    def setUp(self):
        self.card = Card('A', '♦')

    def test_str(self):
        self.assertEqual(self.card.__str__(), 'A ♦')

if __name__ == "__main__":
    unittest.main()