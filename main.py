import os
import random
from tkinter import *
from tkinter.messagebox import showinfo


class MyModal(Tk):
    def __init__(self, text, dealer_hand, hand):
        super().__init__()
        Label(self, text=text).grid()
        Label(self, text='Дилер').grid()
        Label(self, text=dealer_hand).grid()
        Label(self, text='Игрок').grid()
        Label(self, text=hand).grid()
        Button(self, text='OK', command=self.destroy).grid()

class Table:
    def __init__(self):
        self.deck = Deck()
        self.player = Player('Игрок 1')
        self.dealer = Dealer()
        self.deck.shuffle()
        print(self.deck)
        self.__start_game()

    def hit(self):
        self.player.get_card(self.deck.pop_card())
        if self.player.card_count >= 21:
            self.hold()
        return self.player.hand

    def hold(self):
        while self.dealer.card_count < 17:
            self.dealer.get_card(self.deck.pop_card())

        result = self.get_result()
        self.__restart()
        return result

    def get_result(self):
        if (self.player.card_count > 21
                or (self.dealer.card_count < 22
                 and self.player.card_count < self.dealer.card_count)):
            MyModal('Вы проиграли!', self.dealer.hand_str.get(), self.player.hand_str.get())
            return 'lose'
        elif self.dealer.card_count == self.player.card_count:
            MyModal('Ничья!', self.dealer.hand_str.get(), self.player.hand_str.get())
            return 'draw'
        else:
            MyModal('Вы выиграли!', self.dealer.hand_str.get(), self.player.hand_str.get())
            return 'win'

    def __start_game(self):
        self.player.get_card(self.deck.pop_card())
        self.player.get_card(self.deck.pop_card())
        self.dealer.get_card(self.deck.pop_card())
        self.dealer.get_card(self.deck.pop_card())

    def __restart(self):
        self.deck.reset()
        self.player.reset()
        self.dealer.reset()

        self.__start_game()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.card_count = 0
        self.ace_count = 0

        self.hand_str = StringVar()

    def get_card(self, card):
        if card.value in ['Валет', 'Дама', 'Король']:
            self.card_count += 10
        elif card.value == 'Туз':
            self.ace_count += 1
            self.card_count += 11
        else:
            self.card_count += card.value

        if self.card_count > 21 and self.ace_count > 0:
            self.ace_count -= 1
            self.card_count -= 10

        self.hand.append(card)
        self.hand_str.set(", ".join([card.__str__() for card in self.hand]))

    def reset(self):
        self.hand = []
        self.hand_str.set("")
        self.card_count = 0
        self.ace_count = 0

    def _protected(self):
        return 2+2


    def __str__(self):
        return f"Имя: {self.name}, Рука: {self.hand_str.get()}, Счёт: {self.card_count}"

    def __eq__(self, other):
        return self.name == other.name and self.hand == other.hand


class Dealer(Player):
    def __init__(self):
        super().__init__('Дилер')


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return str(self.value) + " " + str(self.suit)

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit


class Deck:

    def __init__(self):
        self.popped_cards = []
        self.card_list = self.initialize_card_list()

    def initialize_card_list(self):
        return [Card(value=v, suit=s)
                          for s in ['Черви', 'Вини', 'Крести', 'Буби']
                          for v in [2, 3, 4, 5, 6, 7, 8, 9, 10,
                                    'Валет', 'Дама', 'Король', 'Туз']]

    def set_card_list(self, card_list):
        self.card_list = card_list

    def get_card_list(self):
        return self.card_list

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
    def __init__(self):
        super().__init__()
        self.table = Table()

        Label(text="Дилер").grid()
        Label(textvariable=self.table.dealer.hand_str).grid()
        Label(text="Игрок").grid()
        Label(textvariable=self.table.player.hand_str).grid()

        self.hit_btn = Button(text="Hit", command=lambda: self.table.hit())
        self.hit_btn.grid()
        self.hold_btn = Button(text="Hold", command=lambda: self.table.hold())
        self.hold_btn.grid()


if __name__ == '__main__':
    if os.name != "nt" and os.getenv("GITHUB_ACTIONS"):
        os.system('Xvfb :1 -screen 0 1600x1200x16 &')
        os.environ["DISPLAY"] = ":1.0"
    app = App()
    app.mainloop()