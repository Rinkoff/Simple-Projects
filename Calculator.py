import tkinter as tk
from tkinter import ttk


class Calculator:
    def __init__(self):
        self.equation = ""
        self.num = ""
        self.memory = ""

        WINDOW_WIDTH = 500
        WINDOW_HEIGHT = 300

        root = tk.Tk()
        root.title("Calculator")

        root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        # Divide window into 2 parts
        left_frame = ttk.Frame(root)
        right_frame = ttk.Frame(root)
        left_frame.pack(side="left", fill="y")
        right_frame.pack(
            side="left",
            fill="both",
            expand=True,
        )

        # Equation label
        self.equation_value = tk.StringVar()
        self.equation_value.set("")
        equation_lbl = ttk.Label(
            left_frame, textvariable=self.equation_value, foreground="#808080"
        )
        equation_lbl.pack(anchor="e")

        # Clicked number label
        self.num_value = tk.StringVar()
        self.num_value.set("0")
        clicked_number = ttk.Label(
            left_frame, textvariable=self.num_value, font=("Ariel", 20, "bold")
        )
        clicked_number.pack(anchor="e")

        # Button frame
        buttons_frame = ttk.Frame(left_frame)

        ttk.Button(
            buttons_frame,
            text=".",
            command=lambda: [self.display_num("."), self.add_to_equation(".")],
        ).grid(row=6, column=0)
        ttk.Button(
            buttons_frame,
            text="0",
            command=lambda: [self.display_num(0), self.add_to_equation(0)],
        ).grid(row=6, column=1)
        ttk.Button(buttons_frame, text="═", width=24, command=self.make_calc).grid(
            row=6, column=2, columnspan=2
        )
        ttk.Button(
            buttons_frame,
            text="1",
            command=lambda: [self.display_num(1), self.add_to_equation(1)],
        ).grid(row=5, column=0)
        ttk.Button(
            buttons_frame,
            text="2",
            command=lambda: [self.display_num(2), self.add_to_equation(2)],
        ).grid(row=5, column=1)
        ttk.Button(
            buttons_frame,
            text="3",
            command=lambda: [self.display_num(3), self.add_to_equation(3)],
        ).grid(row=5, column=2)
        ttk.Button(
            buttons_frame, text="+", command=lambda: self.add_to_equation("+")
        ).grid(row=5, column=3)
        ttk.Button(
            buttons_frame,
            text="4",
            command=lambda: [self.display_num(4), self.add_to_equation(4)],
        ).grid(row=4, column=0)
        ttk.Button(
            buttons_frame,
            text="5",
            command=lambda: [self.display_num(5), self.add_to_equation(5)],
        ).grid(row=4, column=1)
        ttk.Button(
            buttons_frame,
            text="6",
            command=lambda: [self.display_num(6), self.add_to_equation(6)],
        ).grid(row=4, column=2)
        ttk.Button(
            buttons_frame, text="-", command=lambda: self.add_to_equation("-")
        ).grid(row=4, column=3)
        ttk.Button(
            buttons_frame,
            text="7",
            command=lambda: [self.display_num(7), self.add_to_equation(7)],
        ).grid(row=3, column=0)
        ttk.Button(
            buttons_frame,
            text="8",
            command=lambda: [self.display_num(8), self.add_to_equation(8)],
        ).grid(row=3, column=1)
        ttk.Button(
            buttons_frame,
            text="9",
            command=lambda: [self.display_num(9), self.add_to_equation(9)],
        ).grid(row=3, column=2)
        ttk.Button(
            buttons_frame, text="✕", command=lambda: self.add_to_equation("*")
        ).grid(row=3, column=3)
        ttk.Button(buttons_frame, text="+/-", command=self.change_sign).grid(
            row=2, column=0
        )
        ttk.Button(
            buttons_frame, text="n²", command=lambda: self.add_to_equation("**")
        ).grid(row=2, column=1)
        ttk.Button(buttons_frame, text="n!", command=self.display_factorial).grid(
            row=2, column=2
        )
        ttk.Button(
            buttons_frame, text="÷", command=lambda: self.add_to_equation("/")
        ).grid(row=2, column=3)
        ttk.Button(buttons_frame, text="CE", width=24, command=self.clear_num).grid(
            row=1, column=0, columnspan=2
        )
        ttk.Button(buttons_frame, text="C", command=self.clear_equation).grid(
            row=1, column=2
        )
        ttk.Button(buttons_frame, text="⌫", command=self.remove_last_symbol).grid(
            row=1, column=3
        )
        ttk.Button(buttons_frame, text="MR", command=self.memory_recall).grid(
            row=0, column=0
        )
        ttk.Button(buttons_frame, text="MC", command=self.memory_clear).grid(
            row=0, column=1
        )
        ttk.Button(buttons_frame, text="M+", command=self.add_memory).grid(
            row=0, column=2
        )
        ttk.Button(buttons_frame, text="M-", command=self.memory_substaction).grid(
            row=0, column=3
        )

        buttons_frame.pack(side="bottom", fill="both")

        ttk.Label(right_frame, text="Memory").pack()

        self.memory_lbl = ttk.Label(right_frame, text="Empty memory")
        self.memory_lbl.pack(anchor="w", pady=12)

        root.mainloop()

    def display_num(self, button):
        self.num += str(button)
        self.num_value.set(self.num)

    def add_to_equation(self, button):
        self.equation += str(button)
        self.equation_value.set(self.equation)
        self.signs = ["+", "-", "*", "**", "/"]
        if button in self.signs:
            self.clear_num()

    def make_calc(self):
        try:
            self.clear_num()
            self.equation = str(eval(self.equation))
            if len(self.equation) > 13:
                self.num_value.set("Too large number")
            else:
                self.display_num(self.equation)
            self.num = ""
            self.equation = ""
        except:
            self.clear_num()
            self.clear_equation()
            self.display_num("Error")
            self.num = ""
            self.equation = ""

    def clear_num(self):
        self.num = ""
        self.num_value.set("0")

    def clear_equation(self):
        self.equation = ""
        self.equation_value.set("")
        self.num = ""
        self.num_value.set("0")

    def factorial(self, num):
        if num == 0:
            return 1
        else:
            return num * self.factorial(num - 1)

    def display_factorial(self):
        num = int(self.num_value.get())
        self.result = self.factorial(num)
        self.num_value.set(self.result)

    def remove_last_symbol(self):
        list_of_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if self.equation[-1] in list_of_numbers:
            self.num = self.num[:-1]
            self.num_value.set(self.num)
            self.equation = self.equation[:-1]
            self.equation_value.set(self.equation)
        else:
            self.equation = self.equation[:-1]
            self.equation_value.set(self.equation)

    def change_sign(self):
        find_sign = False
        if self.num:
            if self.num[0] == "-":
                self.num = self.num[1:]
                for i, char in enumerate(self.equation):
                    if char in self.signs:
                        if char == "-" and i + 1 == "-":
                            self.equation[i + 1] = "+"
                            find_sign = True
                if find_sign == False and self.equation[0] == "-":
                    self.equation[0] = "+"
            else:
                self.num = "-" + self.num
                for i, char in enumerate(self.equation):
                    if char in self.signs:
                        self.equation = self.equation[:i] + "-" + self.equation[i:]
                        find_sign = True

                if find_sign == False:
                    self.equation = "-" + self.equation

        self.num_value.set(self.num)
        self.equation_value.set(self.equation)

    def add_memory(self):
        if self.memory == "":
            self.memory += self.num
            self.memory_lbl.config(text=self.memory)
        else:
            self.memory = eval(f"{self.memory}+{self.num}")
            self.memory_lbl.config(text=self.memory)
        self.clear_num()
        self.clear_equation()

    def memory_substaction(self):
        if self.memory == "":
            self.memory = eval(f"0 - {self.num}")
            self.memory_lbl.config(text=self.memory)
        else:
            self.memory = eval(f"{self.memory}-{self.num}")
            self.memory_lbl.config(text=self.memory)
        self.clear_num()
        self.clear_equation()

    def memory_clear(self):
        self.memory = ""
        self.memory_lbl.config(text="Empty memory")

    def memory_recall(self):
        if self.memory != "":
            self.num = self.memory
            self.equation += self.memory
            self.num_value.set(self.num)
            self.equation_value.set(self.equation)


if __name__ == "__main__":
    Calculator()
