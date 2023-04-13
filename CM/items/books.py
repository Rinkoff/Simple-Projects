from CM_App.items.item import Items

class Books:

    @staticmethod
    def read_books():
        books = Items.read_items("data/Books.txt")
        return books

    @staticmethod
    def create_book(book):
        Items.create_item("data/Books.txt", book)

    @staticmethod
    def read_book_by_title(title):
        data = Items.read_item_by_title("data/Books.txt", title)
        return data

    @staticmethod
    def update_book_by_title(title, **kwargs):
        Items.update_items_by_title("data/Books.txt", title, "author", "pages", **kwargs)

    @staticmethod
    def delete_book_by_title(title):
        Items.delete_item_by_title("data/Books.txt", title)

    @staticmethod
    def search_in_books(text):
        founded = Items.search_in_items(text, Books.read_books())
        return founded
