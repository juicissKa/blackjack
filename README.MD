[![Coverage Status](https://coveralls.io/repos/github/juicissKa/blackjack/badge.svg?branch=main)](https://coveralls.io/github/juicissKa/blackjack?branch=main)
[![CI/CD Pipeline](https://github.com/juicissKa/blackjack/actions/workflows/github_actions.yml/badge.svg)](https://github.com/juicissKa/blackjack/actions/workflows/github_actions.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=Scrooge2727_python-test&metric=alert_status)](https://sonarcloud.io/dashboard?id=juicissKa_blackjack)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Scrooge2727_python-test&metric=bugs)](https://sonarcloud.io/summary/new_code?id=juicissKa_blackjack)
[![Code smells](https://sonarcloud.io/api/project_badges/measure?project=Scrooge2727_python-test&metric=code_smells)](https://sonarcloud.io/dashboard?id=juicissKa_blackjack)
# План тестирования:

# Аттестационное тестирование
  - Тест А1 (положительный)
    - Начальное состояние: Рабочий стол
    - Действие: Пользователь запускает программу
    - Ожидаемый результат:
        ```
        Окно приложения. Дилер имеет 2 карты, игрок имеет 2 карты.
        ```               
  - Тест А2 (положительный)
    - Начальное состояние: Открытое приложение
    - Действие: Пользователь нажимает на кнопку "Hit", сумма очков пользователя становится < 21
    - Ожидаемый результат: 
      ```                  
     	У пользователя становится на одну карту больше
      ```                         
  - Тест А3 (положительный)
    - Начальное состояние: Открытое приложение
    - Действие: Пользователь нажимает на кнопку "Hit", у него становится > 21 очка
    - Ожидаемый результат: 
        ```
        У дилера появляются карты, пока сумма его очков не станет >= 17
        Определяется результат игры (проигрыш игрока)
        ```                      
  - Тест А4 (положительный)
    - Начальное состояние: Открытое приложение
    - Действие: Пользователь нажимает на кнопку "Hold"
    - Ожидаемый результат: 
        ```                           
        У дилера появляются карты, пока сумма его очков не станет >= 17
        Выводится окно с результатом игры
        ```                            

# Блочное тестирование
## Класс Card
<ol>
  <li>
    <h3>Метод __str__()</h3>
    <ol>
    	<li>
    	  <h4>Тест Б1.1 (положительный)</h4>
    	  <ul>
    	    <li>Входные данные: Card(suit='♦', value='A')</li>
    	    <li>Ожидаемый результат: 'A ♦'</li>
    	  </ul>
    	</li>
    </ol>
  </li>
  <li>
    <h3>Метод __eq__()</h3>
    <ol>
    	<li>
    	  <h4>Тест Б1.2 (положительный)</h4>
    	  <ul>
    	    <li>Входные данные: Card(suit='♦', value='A'), Card(suit='♦', value='A')</li>
    	    <li>Ожидаемый результат: True</li>
    	  </ul>
    	</li>
        <li>
    	  <h4>Тест Б1.3 (негативный)</h4>
    	  <ul>
    	    <li>Входные данные: Card(suit='♦', value='A'), Card(suit='♠', value='A')</li>
    	    <li>Ожидаемый результат: False</li>
    	  </ul>
    	</li>
        <li>
    	  <h4>Тест Б1.3 (негативный)</h4>
    	  <ul>
    	    <li>Входные данные: Card(suit='♦', value='A'), Card(suit='♦', value='K')</li>
    	    <li>Ожидаемый результат: False</li>
    	  </ul>
    	</li>
    </ol>
  </li>
</ol>

## Класс Deck

<ol>
  <li>
    <h3>Метод initialize_deck()</h3>
    <ol>
    	<li>
    	  <h4>Тест Б2.1 (положительный)</h4>
    	  <ul>
    	    <li>Ожидаемый результат: < Массив из 52 объектов класса Card ></li>
    	  </ul>
    	</li>
    </ol>
  </li>
  <li>
    <h3>Метод shuffle()</h3>
    <ol>
    	<li>
    	  <h4>Тест Б2.2 (положительный)</h4>
    	  <ul>
    	    <li>Входные данные: < Массив из 52 объектов класса Card ></li>
    	    <li>Ожидаемый результат: < входной массив с изменённым порядком ></li>
    	  </ul>
    	</li>
    </ol>
  </li>
  <li>
    <h3>Метод pop_card()</h3>
    <ol>
    	<li>
    	  <h4>Тест Б2.3 (положительный)</h4>
    	  <ul>
    	    <li>Входные данные: self.card_list = < Массив из 52 объектов класса Card ></li>
    	    <li>Ожидаемый результат: self.card_list = < входной массив без первого элемент >, self.popped_cards = < первый элемент входного массива ></li>
    	  </ul>
    	</li>
    </ol>
  </li>
  <li>
    <h3>Метод reset()</h3>
    <ol>
    	<li>
    	  <h4>Тест Б2.4 (положительный)</h4>
    	  <ul>
    	    <li>Ожидаемый результат: self.card_list = < Массив из 52 объектов класса Card >, self.popped_cards = [] </li>
    	  </ul>
    	</li>
    </ol>
  </li>
  <li>
    <h3>Метод __str__()</h3>
    <ol>
    	<li>
    	  <h4>Тест Б2.5 (положительный)</h4>
    	  <ul>
    	    <li>Ожидаемый результат: ['Масть Карта', 'Масть Карта', ...] </li>
    	  </ul>
    	</li>
    </ol>
  </li>
</ol>

## Класс Player

<ol>
  <li>
    <h3>Метод get_card(Card card)</h3>
    <ol>
    	<li>
    	  <h4>Тест Б3.1 (положительный)</h4>
    	  <ul>
            <li>Входные данные: self.hand = [], self.hand_str.get() = "", self.card_count = 0, self.ace_count = 0, card = Card(suit='♦', value='A')</li>
    	    <li>Ожидаемый результат: self.hand = [Card(suit='♦', value='A')], self.hand_str.get() = "A ♦", self.card_count = 11, self.ace_count = 1</li>
    	  </ul>
    	</li>
    	<li>
    	  <h4>Тест Б3.2 (положительный)</h4>
    	  <ul>
            <li>Входные данные: self.hand = [Card(suit='♦', value='A')], self.hand_str.get() = "A ♦", self.card_count = 11, self.ace_count = 1, card = Card(suit='♠', value='A')</li>
    	    <li>Ожидаемый результат: self.hand = [Card(suit='♦', value='A')], self.hand_str.get() = "A ♦, A ♠", self.card_count = 12, self.ace_count = 1</li>
    	  </ul>
    	</li>
    	<li>
    	  <h4>Тест Б3.3 (положительный)</h4>
    	  <ul>
            <li>Входные данные: self.hand = [Card(suit='♦', value='A'), Card(suit='♦', value='K')], self.hand_str.get() = "A ♦, K ♦", self.card_count = 21, self.ace_count = 1, card = Card(suit='♠', value='A')</li>
    	    <li>Ожидаемый результат: self.hand = [Card(suit='♦', value='A'), Card(suit='♦', value='K'), Card(suit='♠', value='A'], self.hand_str.get() = "A ♦, K ♦, A ♠", self.card_count = 12, self.ace_count = 0</li>
    	  </ul>
    	</li>
    </ol>
  </li>
  <li>
    <h3>Метод reset()</h3>
    <ol>
    	<li>
    	  <h4>Тест Б3.4 (положительный)</h4>
    	  <ul>
    	    <li>Ожидаемый результат: self.hand = [], self.card_count = 0, self.ace_count = 0</li>
    	  </ul>
    	</li>
    </ol>
  </li>
  <li>
    <h3>Метод __str__()</h3>
    <ol>
    	<li>
    	  <h4>Тест Б1.1 (положительный)</h4>
    	  <ul>
    	    <li>Входные данные: self.card_list = [Card(suit='♦', value='A')], self.name = 'Игрок', self.card_count = 11</li>
    	    <li>Ожидаемый результат: "Имя: Игрок, Рука: A ♦, Счёт: 11" </li>
    	  </ul>
    	</li>
    </ol>
  </li>
</ol>

# Интеграционное тестирование
<ol>
  <li>
    <h3>Тест И1</h3>
    <ul>
      <li>Методы: Table.hit(), Player.get_card(Card card), Table.hold(), Table.get_result(), Table.__restart(), Table.__start()</li>
      <li>Описание: Перебор карт при нажатии на кнопку "Hit" </li>
      <li>Входные данные: 
            player = Player(),
            player.hand = [Card(suit='♦', value='Q'),
            Card(suit='♦', value='J')],
            card = Card(suit='♦', value='K'),
            card_count = 20
      </li>
      <li>Ожидаемый результат: 'lose'</li>
    </ul>	
  </li>
    <li>
    <h3>Тест И2</h3>
    <ul>
      <li>Методы: Table.hold(), Dealer.get_card(Card card), Table.hold(), Table.get_result(), Table.__restart(), Table.__start()</li>
      <li>Описание: Нажатие на кнопку 'Hold' с 21 очком </li>
      <li>Входные данные: dealer = Dealer([Card(suit='♦', value='Q'), Card(suit='♦', value='Семь')]), dealer.hand = [] player = Player(), player.hand = [Card(suit='♦', value='Q'), Card(suit='♦', value='A')], player.card_count = 21</li>
      <li>Ожидаемый результат: 'win'</li>
    </ul>	
  </li>
</ol>


