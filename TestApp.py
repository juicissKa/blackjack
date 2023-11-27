import tkinter.messagebox
import unittest
from main import App, Deck, Card, Player, Dealer
from unittest.mock import patch, Mock
import tkinter

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.table = self.app.table
        self.player = self.app.table.player
        self.dealer = self.app.table.dealer
        self.deck = self.app.table.deck

    # integration
    def test_table_hit(self):
        hand = self.player.hand.copy()
        hand.append(self.deck.card_list[0])

        result = self.table.hit(player=self.player)
        self.assertEqual(result[0], hand[0])
        self.assertEqual(result[1], hand[1])
        self.assertEqual(result[2], hand[2])

    def test_table_hold(self):
        self.player.card_count = 21
        self.dealer.card_count = 21
        self.assertEqual(self.table.hold(), 'draw')
        self.player.card_count = 23
        self.dealer.card_count = 21
        self.assertEqual(self.table.hold(), 'lose')
        self.player.card_count = 23
        self.dealer.card_count = 23
        self.assertEqual(self.table.hold(), 'lose')
        self.player.card_count = 21
        self.dealer.card_count = 20
        self.assertEqual(self.table.hold(), 'win')

    def test_start_game(self):
        self.player.reset()
        self.dealer.reset()
        self.deck.reset()

        self.table._Table__start_game()
        self.assertEqual(len(self.player.hand), 2)
        self.assertEqual(len(self.dealer.hand), 2)
        self.assertEqual(len(self.deck.popped_cards), 4)
        self.assertEqual(self.player.hand[0], self.deck.popped_cards[0])
        self.assertEqual(self.player.hand[1], self.deck.popped_cards[1])
        self.assertEqual(self.dealer.hand[0], self.deck.popped_cards[2])
        self.assertEqual(self.dealer.hand[1], self.deck.popped_cards[3])

        self.assertEqual(len(self.deck.card_list), 48)


    def test_restart(self):
        self.table._Table__restart()
        self.assertEqual(len(self.player.hand), 2)
        self.assertEqual(len(self.dealer.hand), 2)
        self.assertEqual(len(self.deck.popped_cards), 4)
        self.assertEqual(self.player.hand[0], self.deck.popped_cards[0])
        self.assertEqual(self.player.hand[1], self.deck.popped_cards[1])
        self.assertEqual(self.dealer.hand[0], self.deck.popped_cards[2])
        self.assertEqual(self.dealer.hand[1], self.deck.popped_cards[3])

        self.assertEqual(len(self.deck.card_list), 48)


class TestPlayer(unittest.TestCase):
        def setUp(self):
            self.player = Player('Игрок')

        def test_get_card_default(self):
            self.player.get_card(Card(suit='Буби', value=2))
            self.assertEqual(self.player.hand, [Card(suit='Буби', value=2)])
            self.assertEqual(self.player.card_count, 2)
            self.assertEqual(self.player.ace_count, 0)

        def test_get_card_ace(self):
            self.player.get_card(Card(suit='Буби', value='Туз'))
            self.assertEqual(self.player.hand, [Card(suit='Буби', value='Туз')])
            self.assertEqual(self.player.card_count, 11)
            self.assertEqual(self.player.ace_count, 1)
            self.assertEqual(self.player.hand_str.get(), "Туз Буби")

        def test_get_card_double_ace(self):
            self.player.get_card(Card(suit='Буби', value='Туз'))
            self.player.get_card(Card(suit='Вини', value='Туз'))
            self.assertEqual(self.player.hand, [Card(suit='Буби', value='Туз'), Card(suit='Вини', value='Туз')])
            self.assertEqual(self.player.card_count, 12)
            self.assertEqual(self.player.ace_count, 1)
            self.assertEqual(self.player.hand_str.get(), "Туз Буби, Туз Вини")

        def test_reset(self):
            self.player.reset()
            self.assertEqual(self.player.hand, [])
            self.assertEqual(self.player.card_count, 0)
            self.assertEqual(self.player.ace_count, 0)
            self.assertEqual(self.player.hand_str.get(), "")

        def test_str(self):
            self.player.get_card(Card(suit='Буби', value='Туз'))

            self.assertEqual(self.player.__str__(), f"Имя: Игрок, Рука: Туз Буби, Счёт: 11")


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_initialize_card_list(self):
        self.assertEqual(self.deck.initialize_card_list(), [Card(value=v, suit=s)
                          for s in ['Черви', 'Вини', 'Крести', 'Буби']
                          for v in [2, 3, 4, 5, 6, 7, 8, 9, 10,
                                    'Валет', 'Дама', 'Король', 'Туз']])

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
        self.card = Card('Туз', 'Буби')

    def test_str(self):
        self.assertEqual(self.card.__str__(), 'Туз Буби')

if __name__ == "__main__":
    unittest.main()