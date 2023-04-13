from CM_App.items.item import Items

class Movies:
    @staticmethod
    def read_movies():
        movies = Items.read_items("data/Movies.txt")
        return movies

    @staticmethod
    def create_movie(movie):
        Items.create_item("data/Movies.txt",movie)

    @staticmethod
    def read_movie_by_title(title):
        data = Items.read_item_by_title("data/Movies.txt",title)
        return data

    @staticmethod
    def update_movie_by_title(title, **kwargs):
        Items.update_items_by_title("data/Movies.txt",title,"director","actors",**kwargs)

    @staticmethod
    def delete_movie_by_title(title):
        Items.delete_item_by_title("data/Movies.txt",title)


    @staticmethod
    def search_in_movies(text):
        founded = Items.search_in_items(text,Movies.read_movies())
        return founded
