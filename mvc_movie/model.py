import yaml

from mvc_movie import Actor, Movie


class Model:

    def __init__(self):
        self._dump_filename = "./movies.dump"
        self.load()
        self._list_movie = list()

    def add_movie(self, movie_obj):
        self._list_movie.append(movie_obj)
        self.show_all()

    def dump_to_yml(self):
        with open(self._dump_filename, "at") as file:
            for line in self._list_movie:
                data_to_dump = {'title': 'Firs Peter', 'date_realized': "2020", 'actor': line.actor}
                yaml.dump(data_to_dump, file)
                return data_to_dump

    def load(self):
        """ load all movie"""
        try:
            with open(self._dump_filename, "rt") as file:
                data_movie = yaml.safe_load(file)
                print(type(data_movie))
                self._list_movie = data_movie
        except FileNotFoundError:
            f = open(self._dump_filename, "wt")
            f.close()

    def get_all_movie(self):
        if not self._list_movie:
            return ("Список пуст", )
        return self._list_movie

    def show_all(self):
        movies = self.get_all_movie()
        for movie in movies:
            print(movie)
        return movies


if __name__ == '__main__':
    mod = Model()
    actors = [
        Actor(name="Peter", last_name="First", role="main_Hero"),
        Actor(name="Kira", last_name="Knightley", role="Joan Clarke"),
        Actor(name="Benedict", last_name="Cumberbatch", role="Alan Turing")
    ]
    movie_obj = Movie(title="Firs Peter", date_realized=2020, actor=actors)
    mod.add_movie(movie_obj=movie_obj)
    print(mod.dump_to_yml())

