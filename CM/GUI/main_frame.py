import tkinter as tk
from tkinter import ttk

class MainFrame(tk.Frame):
    def __init__(self,master):
        super().__init__(master)

        self.collection_lbl = ttk.Label(self,font=("Arial",40, "bold"))
        self.collection_lbl.pack()

        self.search = ttk.Entry(self,font=20,foreground="#808080",validate="key")
        self.search.place(relx=0.1,rely=0.1,relwidth=0.7,relheight=0.07)
        self.search.insert(0,"Search...")
        self.search.bind("<FocusIn>",self.on_entry_click)
        self.search.bind("<FocusOut>",self.on_focusout)

        self.search_button = ttk.Button(self,text="Search")
        self.search_button.place(relx=0.82,rely=0.1,relwidth=0.08,relheight=0.07)

        self.listbox_search = tk.Listbox(self,selectmode="SINGLE")
        self.listbox_search.place(relx=0.1,rely=0.2,relwidth=0.5,relheight=0.6)

        self.scrollbar = ttk.Scrollbar(self.listbox_search,orient=tk.VERTICAL)
        self.scrollbar.pack(side="right",fill="y")
        self.listbox_search.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox_search.yview)

        self.show_lbl = ttk.Label(self,text = "",background="#FFFFFF",anchor="nw")
        self.show_lbl.place(relx=0.62,rely=0.2,relwidth=0.28,relheight=0.6)


    def on_entry_click(self,event):
        if self.search.get() == "Search...":
            self.search.delete(0, "end")
            self.search.insert(0, "")
            self.search.config(foreground="#000000")

    def on_focusout(self,event):
        if self.search.get() == "":
            self.search.insert(0, "Search...")
            self.search.config(foreground="#808080")

    def add_window(self):
        self.add_button_root = tk.Tk()

        add_window_width = 600
        add_window_height = 700

        self.add_button_root.geometry(f"{add_window_width}x{add_window_height}")
        self.add_button_root.attributes("-fullscreen",False)
        self.add_button_root.minsize(600,700)
        self.add_button_root.maxsize(600,700)

        self.add_object_lbl = ttk.Label(self.add_button_root,font=("Arial",20, "bold"))
        self.add_object_lbl.pack()

        self.title = ttk.Label(self.add_button_root,font=("Arial",13))
        self.title.place(relx=0.25,rely=0.1)

        self.title_entry = ttk.Entry(self.add_button_root)
        self.title_entry.place(relx=0.15, rely=0.14,relwidth=0.32,relheight=0.07)

        self.author = ttk.Label(self.add_button_root, font=("Arial", 13))
        self.author.place(relx=0.6, rely=0.1)

        self.author_entry = ttk.Entry(self.add_button_root)
        self.author_entry.place(relx=0.55, rely=0.14, relwidth=0.32, relheight=0.07)

        self.genre = ttk.Label(self.add_button_root, text="Genre", font=("Arial", 13))
        self.genre.place(relx=0.25, rely=0.3)

        self.genre_entry = ttk.Entry(self.add_button_root)
        self.genre_entry.place(relx=0.15, rely=0.34, relwidth=0.32, relheight=0.07)

        self.year = ttk.Label(self.add_button_root, text="Year", font=("Arial", 13))
        self.year.place(relx=0.6, rely=0.3)

        self.year_entry = ttk.Entry(self.add_button_root)
        self.year_entry.place(relx=0.55, rely=0.34, relwidth=0.32, relheight=0.07)

        self.addition = ttk.Label(self.add_button_root,font=("Arial", 13))
        self.addition.place(relx=0.45, rely=0.5)

        self.addition_entry = ttk.Entry(self.add_button_root)
        self.addition_entry.place(relx=0.33, rely=0.54, relwidth=0.32, relheight=0.07)

        ttk.Button(self.add_button_root, text="Cancel",command=self.add_button_root.destroy).place(
            relx= 0.55,rely=0.85,relwidth=0.25,relheight=0.05)

    def submit_info(self,func):
        title_value = self.title_entry.get().capitalize()
        author_value = self.author_entry.get().capitalize()
        genre_value = self.genre_entry.get().capitalize()
        year_value = self.year_entry.get()
        addition_value = self.addition_entry.get().capitalize()
        result = [title_value,author_value,genre_value,year_value,addition_value]
        func(result)
        self.add_button_root.destroy()

    def insert_data(self,data):
        self.listbox_search.delete(0, "end")
        titles = [char[0] for char in data]
        num = 0
        for title in titles:
            self.listbox_search.insert(num,title)
            num += 1

    def show_by_filter(self,func,func2):
        if self.search.get() == "Search..." or self.search.get() == "":
            self.insert_data(func())
        else:
            filtered = func2(self.search.get().capitalize())
            self.insert_data(filtered)
