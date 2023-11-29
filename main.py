import os
import random
from tkinter import *
from tkinter.messagebox import showinfo


class MyModal(Tk):
    def __init__(self, text, dealer_hand, hand): # pragma: no cover
        super().__init__()
        Label(self, text=text).grid()
        Label(self, text='Дилер').grid()
        Label(self, text=dealer_hand).grid()
        Label(self, text='Игрок').grid()
        Label(self, text=hand).grid()
        Button(self, text='OK', command=self.destroy).grid()

class Table:
    def __init__(self): # pragma: no cover
        self.deck = Deck()
        self.player = Player('Игрок 1')
        self.dealer = Dealer()
        self.deck.shuffle()
        self.__start_game()

    def get_result(self):
        if (self.player.card_count > 21
                or (self.dealer.card_count < 22
                 and self.player.card_count < self.dealer.card_count)):
            return 'lose'
        elif self.dealer.card_count == self.player.card_count:
            return 'draw'
        else:
            return 'win'

    def __start_game(self):
        self.player.get_card(self.deck.pop_card())
        self.player.get_card(self.deck.pop_card())
        self.dealer.get_card(self.deck.pop_card())
        self.dealer.get_card(self.deck.pop_card())

    def restart(self):
        self.deck.reset()
        self.player.reset()
        self.dealer.reset()

        self.__start_game()

    def hit(self):
        self.player.get_card(self.deck.pop_card())

    def hold(self):
        while self.dealer.card_count < 17:
            self.dealer.get_card(self.deck.pop_card())

        return self.get_result()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.card_count = 0
        self.ace_count = 0

    def get_card(self, card):
        if card.value in ['J', 'Q', 'K']:
            self.card_count += 10
        elif card.value == 'A':
            self.ace_count += 1
            self.card_count += 11
        else:
            self.card_count += card.value

        if self.card_count > 21 and self.ace_count > 0:
            self.ace_count -= 1
            self.card_count -= 10

        self.hand.append(card)

    def reset(self):
        self.hand = []
        self.card_count = 0
        self.ace_count = 0



    def __str__(self):
        return f"Имя: {self.name}, Рука: {', '.join([card.__str__() for card in self.hand])}, Счёт: {self.card_count}"
    

class Dealer(Player):
    def __init__(self): # pragma: no cover
        super().__init__('Дилер')


class Card:
    def __init__(self, value, suit): # pragma: no cover
        self.value = value
        self.suit = suit

    def __str__(self):
        return str(self.value) + " " + str(self.suit)

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit


class Deck:

    def __init__(self): # pragma: no cover
        self.popped_cards = []
        self.card_list = self.initialize_card_list()

    def initialize_card_list(self):
        return [Card(value=v, suit=s)
                          for s in ['♥', '♠', '♣', '♦']
                          for v in [2, 3, 4, 5, 6, 7, 8, 9, 10,
                                    'J', 'Q', 'K', 'A']]


    def shuffle(self):
        random.shuffle(self.card_list)
        return self.card_list

    def pop_card(self):
        self.popped_cards.append(self.card_list[0])
        return self.card_list.pop(0)

    def reset(self):
        self.card_list = self.card_list + self.popped_cards
        self.popped_cards = []
        self.shuffle()
        return self.card_list

    def __str__(self):
        return str([card.__str__() for card in self.card_list])

    def __eq__(self, other):
        return self.card_list == other.card_list


class App(Tk):

    def __init__(self): # pragma: no cover
        super().__init__()
        self.table = Table()
        self.player_hand_str = StringVar()
        self.dealer_hand_str = StringVar()
        self.player_hand_str.set(", ".join([card.__str__() for card in self.table.player.hand]))
        self.dealer_hand_str.set(", ".join([card.__str__() for card in self.table.dealer.hand]))
        Label(text="Дилер").grid()
        Label(textvariable=self.dealer_hand_str).grid()
        Label(text="Игрок").grid()
        Label(textvariable=self.player_hand_str).grid()

        self.hit_btn = Button(text="Hit", command=lambda: self.hit())
        self.hit_btn.grid()
        self.hold_btn = Button(text="Hold", command=lambda: self.hold())
        self.hold_btn.grid()

    def hit(self): # pragma: no cover
        self.table.hit()
        self.player_hand_str.set(", ".join([card.__str__() for card in self.table.player.hand]))
        if self.table.player.card_count >= 21:
            self.hold()


    def hold(self): # pragma: no cover
        result = self.table.hold()
        self.dealer_hand_str.set(", ".join([card.__str__() for card in self.table.dealer.hand]))

        if result == 'lose':
            MyModal('Вы проиграли!', self.dealer_hand_str.get(), self.player_hand_str.get())
        elif result == 'draw':
            MyModal('Ничья!', self.dealer_hand_str.get(), self.player_hand_str.get())
        else:
            MyModal('Вы победили!', self.dealer_hand_str.get(), self.player_hand_str.get())
        self.table.restart()
        self.player_hand_str.set(", ".join([card.__str__() for card in self.table.player.hand]))
        self.dealer_hand_str.set(", ".join([card.__str__() for card in self.table.dealer.hand]))


if __name__ == '__main__': # pragma: no cover
    app = App()
    app.mainloop()