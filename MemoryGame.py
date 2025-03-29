import tkinter as tk
import random

# Създаване на основния прозорец
root = tk.Tk()
root.title("Memory Game")


# Списък с двойки числа (представящи картите)
cards = list(range(1, 9)) * 2
random.shuffle(cards)

# Глобални променливи за играта
first_card = None
buttons = {}
revealed_cards = {}

# Функция за откриване на карта
def reveal_card(index):
    global first_card
    if index in revealed_cards or len(revealed_cards) >= 2:
        return

    buttons[index]["text"] = cards[index]
    revealed_cards[index] = cards[index]

    # Проверка дали вече има отворена карта
    if first_card is None:
        first_card = index
    else:
        check_match(index)

# Проверка за съвпадение на двойките карти
def check_match(second_card):
    global first_card, revealed_cards

    if cards[first_card] == cards[second_card]:
        # Съвпадение! Оставяме картите отворени
        revealed_cards.clear()
        first_card = None
    else:
        # Няма съвпадение - затваряне на картите след малко време
        root.after(1000, close_cards, first_card, second_card)
        first_card = None

# Функция за затваряне на картите
def close_cards(card1, card2):
    buttons[card1]["text"] = ""
    buttons[card2]["text"] = ""
    revealed_cards.clear()

# Създаване на бутоните за картите
for i in range(16):
    button = tk.Button(root, text="", width=10, height=4, command=lambda i=i: reveal_card(i))
    button.grid(row=i//4, column=i%4)
    buttons[i] = button

# Стартиране на приложението
root.mainloop()
