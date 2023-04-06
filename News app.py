import tkinter as tk
from tkinter import ttk
from urllib import request
import re

URL = "https://slashdot.org/slashdot.rss"


def explore_file(url):
    titles = []
    descriptions = []
    response = request.urlopen(url)
    rss = response.read().decode("utf-8")
    items = re.findall(r"<item(.*?)</item>", rss, re.DOTALL)
    for item in items:
        title = re.search(r"<title>(.*?)</title>", item, re.DOTALL)
        titles.append(title.group(1))
        description = re.search(r"<description>(.*?)&", item, re.DOTALL)
        descriptions.append(description.group(1))
    return titles, descriptions


class App:
    def __init__(self):

        WINDOW_WIDTH = 800
        WINDOW_HEIGHT = 500

        self.titles, self.descriptions = explore_file(URL)

        self.root = tk.Tk()
        self.root.title("News")

        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        ttk.Label(self.root, text="Title", font=20).place(relx=0.1, rely=0.06)

        self.title_lb = tk.Listbox(self.root, selectmode="SINGLE")
        self.title_lb.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.3)

        self.scrollbar_title = ttk.Scrollbar(self.title_lb, orient=tk.VERTICAL)
        self.scrollbar_title.pack(side="right", fill="y")
        self.title_lb.config(yscrollcommand=self.scrollbar_title.set)
        self.scrollbar_title.config(command=self.title_lb.yview)

        self.insert_title(self.titles)

        ttk.Label(self.root, text="Description", font=20).place(relx=0.1, rely=0.45)

        self.description = tk.Text(self.root, wrap="word")
        self.description.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.3)

        self.title_lb.bind("<<ListboxSelect>>", self.insert_description)

        button_style = ttk.Style()
        button_style.configure("Clear.TButton", padding=10)

        ttk.Button(
            self.root,
            text="Clear",
            style="Clear.TButton",
            command=self.clear_description,
        ).pack(side="bottom", pady=20)

        self.root.mainloop()

    def insert_title(self, titles):
        self.title_lb.delete(0, "end")
        num = 0
        for title in titles:
            self.title_lb.insert(num, title)
            num += 1

    def insert_description(self, event):
        title = event.widget.get(event.widget.curselection())
        index = self.titles.index(title)
        self.description.delete("1.0", tk.END)
        self.description.insert("1.0", self.descriptions[index])

    def clear_description(self):
        self.description.delete("1.0", tk.END)


if __name__ == "__main__":
    App()
