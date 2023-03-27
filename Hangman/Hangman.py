import tkinter as tk
from tkinter import ttk
import random
from string import ascii_uppercase as ascii


def take_word(file):
    with open(file, "r") as f:
        words = f.read().split()
        return random.choice(words)


def images():
    image_list = []
    for i in range(7):
        image_list.append(tk.PhotoImage(file=f"assets/{i}.png"))
    return image_list

def start_letters():
    global word
    global guessed

    first_letter = word[0]
    last_letter = word[-1]

    check_letter(first_letter)
    check_letter(last_letter)

def new_game():
    global updated_word
    global mistakes
    global img_index
    global word

    mistakes = 0
    img_index = 0
    imglbl.config(image=img[img_index])

    for button in button_dict.values():
        button.config(state="normal")

    word = take_word("assets/words.txt")
    word = word.upper()
    updated_word = " ".join(word)
    lblword.set(" ".join("_"*len(word)))
    endlbl.config(text="")

    start_letters()

def check_letter(letter):
    global mistakes
    global img_index
    global guessed
    global word

    word_letters = list(updated_word)
    guessed = list(lblword.get())
    if updated_word.count(letter) > 0:
        for i in range(len(word_letters)):
            if word_letters[i] == letter:
                guessed[i] = letter
            lblword.set("".join(guessed))
            if lblword.get() == updated_word:
                endlbl.config(text="You\nWin",foreground="#4E9F3D")
                for button in button_dict.values():
                    button.config(state="disabled")
    else:
        mistakes+=1
        img_index += 1
        imglbl.config(image=img[img_index])

        if img_index == 6:
            endlbl.config(text="Game\nOver",foreground="#FF0000")
            for button in button_dict.values():
                button.config(state="disable")
            lblword.set(word)
    button_dict[letter].config(state="disabled")


WINDOW_WIDTH = 500
WINDOW_HEIGHT = 650

root = tk.Tk()

root.title("Hangman")

root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

main_frame = ttk.Frame(
    root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT
)
main_frame.pack(fill=tk.BOTH, expand=True)

ttk.Label(main_frame, text="Welcome to Hangman",font=("Pristina",20)).place(relx=0.3,rely=0.02)


img= images()
imglbl = ttk.Label(main_frame,image=img[0])
imglbl.place(relx=0.2,rely= 0.1)

lblword = tk.StringVar()
ttk.Label(main_frame,textvariable=lblword, font=("Arial", 40, "bold")).place(relx=0.1, rely=0.5)

button_dict = {}
n = 0
for letter in ascii:
    button = ttk.Button(main_frame, text=letter, command=lambda l=letter: check_letter(l))
    button.place(relx=0.05 + (n%9)*0.09, rely=0.62 + (n//9)*0.1, relwidth=0.09, relheight=0.09)
    button_dict[letter] = button
    n += 1

ttk.Button(main_frame,text="New\nGame",command=new_game).place(relx=0.77,rely=0.82, relwidth=0.09,relheight= 0.09)

endlbl = ttk.Label(main_frame, font = ("Arial", 85, "bold"))
endlbl.place(relx=0.2,rely= 0.1)

new_game()
root.mainloop()
