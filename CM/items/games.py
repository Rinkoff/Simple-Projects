from CM_App.items.item import Items

class Games:

    @staticmethod
    def read_games():
        games = Items.read_items("data/Games.txt")
        return games

    @staticmethod
    def create_game(game):
        Items.create_item("data/Games.txt", game)

    @staticmethod
    def read_game_by_title(title):
        data = Items.read_item_by_title("data/Games.txt", title)
        return data

    @staticmethod
    def update_game_by_title(title, **kwargs):
        Items.update_items_by_title("data/Games.txt", title, "creator", "mode", **kwargs)

    @staticmethod
    def delete_game_by_title(title):
        Items.delete_item_by_title("data/Games.txt", title)

    @staticmethod
    def search_in_games(text):
        founded = Items.search_in_items(text, Games.read_games())
        return founded
