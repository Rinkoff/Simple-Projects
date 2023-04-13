import tkinter as tk
from tkinter import ttk
from GUI.main_frame import MainFrame
from items.movies import Movies
from items.books import Books
from items.games import Games


class MoviesFrame(MainFrame):
    def __init__(self, master):
        super().__init__(master)

        self.collection_lbl.config(text="My Movies")

        swipe_button_style = ttk.Style()
        swipe_button_style.configure("ChangePage.TButton", padding=10)

        self.left_button = ttk.Button(
            self,
            text="〈 Books",
            style="ChangePage.TButton",
            width=10,
            command=lambda: switch_frame(BooksFrame),
        ).pack(side="left", anchor="center")
        self.right_button = ttk.Button(
            self,
            text="Games 〉",
            style="ChangePage.TButton",
            width=10,
            command=lambda: switch_frame(GamesFrame),
        ).pack(side="right", anchor="center")

        self.insert_data(Movies.read_movies())

        self.search_button.config(
            command=lambda: self.show_by_filter(Movies.read_movies,Movies.search_in_movies)
        )

        self.listbox_search.bind("<<ListboxSelect>>", self.show_movie_info)

        style = ttk.Style()
        style.configure("Add.TButton", padding=20, font=("Ariel", 16, "bold"))

        self.add_button = ttk.Button(
            self,
            text="Add Movie",
            style="Add.TButton",
            width=30,
            command=self.add_movie,
        )
        self.add_button.pack(side="bottom", anchor="center", pady=30)

    def add_movie(self):
        self.add_window()
        self.add_button_root.title("Add Movie")

        self.add_object_lbl.config(text="Add Movie")
        self.title.config(text="Movie Title")
        self.author.config(text="Director")
        self.addition.config(text="Actors")

        self.addition_info = ttk.Label(
            self.add_button_root,
            text="Separate with ','",
            foreground="#ff0000",
            font=14,
        )
        self.addition_info.place(relx=0.4, rely=0.61)

        ttk.Button(
            self.add_button_root,
            text="Submit",
            command=lambda: self.submit_info(Movies.create_movie),
        ).place(relx=0.15, rely=0.85, relwidth=0.25, relheight=0.05)

    def show_movie_info(self, event):
        movie_name = event.widget.get(event.widget.curselection())
        movie = Movies.read_movie_by_title(movie_name)
        separator = 70 * "-"
        actor_list = []
        actors = list(movie[4].split(","))
        for actor in actors:
            actor_list.append(actor)

        actors_sep = "\n".join(actor_list)
        self.show_lbl.config(
            text=f"Title:{movie[0]}\n"
            f"{separator}\n"
            f"Director:{movie[1]}\n"
            f"{separator}\n"
            f"Genre:{movie[2]}\n"
            f"{separator}\n"
            f"Year:{movie[3]}\n"
            f"{separator}\n"
            f"Actors:\n{actors_sep}"
        )


class GamesFrame(MainFrame):
    def __init__(self, master):
        super().__init__(master)

        self.collection_lbl.config(text="My Games")

        swipe_button_style = ttk.Style()
        swipe_button_style.configure("ChangePage.TButton", padding=10)

        self.left_button = ttk.Button(
            self,
            text="〈 Movies",
            style="ChangePage.TButton",
            width=10,
            command=lambda: switch_frame(MoviesFrame),
        ).pack(side="left", anchor="center")
        self.right_button = ttk.Button(
            self,
            text="Books 〉",
            style="ChangePage.TButton",
            width=10,
            command=lambda: switch_frame(BooksFrame),
        ).pack(side="right", anchor="center")

        self.insert_data(Games.read_games())

        self.search_button.config(
            command=lambda: self.show_by_filter(Games.read_games,Games.search_in_games)
        )

        self.listbox_search.bind("<<ListboxSelect>>", self.show_game_info)

        style = ttk.Style()
        style.configure("Add.TButton", padding=20, font=("Ariel", 16, "bold"))

        self.add_button = ttk.Button(
            self, text="Add Game", style="Add.TButton", width=30, command=self.add_game
        )
        self.add_button.pack(side="bottom", anchor="center", pady=30)

    def add_game(self):
        self.add_window()
        self.add_button_root.title("Add Game")

        self.add_object_lbl.config(text="Add Game")
        self.title.config(text="Game Title")
        self.author.config(text="Creator")
        self.addition.config(text="Mode")
        ttk.Button(
            self.add_button_root,
            text="Submit",
            command=lambda: self.submit_info(Games.create_game),
        ).place(relx=0.15, rely=0.85, relwidth=0.25, relheight=0.05)

    def show_game_info(self, event):
        game_name = event.widget.get(event.widget.curselection())
        game = Games.read_game_by_title(game_name)
        separator = 70 * "-"
        self.show_lbl.config(
            text=f"Title:{game[0]}\n"
            f"{separator}\n"
            f"Creator:{game[1]}\n"
            f"{separator}\n"
            f"Genre:{game[2]}\n"
            f"{separator}\n"
            f"Year:{game[3]}\n"
            f"{separator}\n"
            f"Mode:\n{game[4]}"
        )


class BooksFrame(MainFrame):
    def __init__(self, master):
        super().__init__(master)

        self.collection_lbl.config(text="My Books")

        swipe_button_style = ttk.Style()
        swipe_button_style.configure("ChangePage.TButton", padding=10)

        self.left_button = ttk.Button(
            self,
            text="〈 Games",
            style="ChangePage.TButton",
            width=10,
            command=lambda: switch_frame(GamesFrame),
        ).pack(side="left", anchor="center")
        self.right_button = ttk.Button(
            self,
            text="Movies 〉",
            style="ChangePage.TButton",
            width=10,
            command=lambda: switch_frame(MoviesFrame),
        ).pack(side="right", anchor="center")

        self.insert_data(Books.read_books())

        self.search_button.config(
            command=lambda: self.show_by_filter(Books.read_books,Books.search_in_books)
        )

        self.listbox_search.bind("<<ListboxSelect>>", self.show_book_info)

        style = ttk.Style()
        style.configure("Add.TButton", padding=20, font=("Ariel", 16, "bold"))

        self.add_button = ttk.Button(
            self, text="Add Book", style="Add.TButton", width=30, command=self.add_book
        )
        self.add_button.pack(side="bottom", anchor="center", pady=30)

    def add_book(self):
        self.add_window()
        self.add_button_root.title("Add Book")

        self.add_object_lbl.config(text="Add Book")
        self.title.config(text="Book Title")
        self.author.config(text="Author")
        self.addition.config(text="Pages")

        ttk.Button(
            self.add_button_root,
            text="Submit",
            command=lambda: self.submit_info(Books.create_book),
        ).place(relx=0.15, rely=0.85, relwidth=0.25, relheight=0.05)

    def show_book_info(self, event):
        book_name = event.widget.get(event.widget.curselection())
        book = Books.read_book_by_title(book_name)
        separator = 70 * "-"
        self.show_lbl.config(
            text=f"Title:{book[0]}\n"
            f"{separator}\n"
            f"Author:{book[1]}\n"
            f"{separator}\n"
            f"Genre:{book[2]}\n"
            f"{separator}\n"
            f"Year:{book[3]}\n"
            f"{separator}\n"
            f"Pages:\n{book[4]}"
        )


def switch_frame(selected_frame):
    global main_frame
    main_frame.destroy()
    main_frame = selected_frame(root)
    main_frame.pack(fill="both", expand=True)
    main_frame.tkraise()


if __name__ == "__main__":
    root = tk.Tk()

    main_frame = MoviesFrame(root)
    main_frame.pack(fill="both", expand=True)

    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 700

    root.title("Hobbies Collector")

    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    root.minsize(1200, 700)

    root.mainloop()