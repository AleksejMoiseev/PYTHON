import yaml

from mvc_movie import Actor, Movie


class Model:

    def __init__(self):
        self._dump_filename = "./movies.dump"
        # self.load()
        self._list_movie = list()

    def add_movie(self, movie_obj):
        self._list_movie.append(movie_obj)
        self.show_all()

    def dump_to_yml(self):
        list_for_dump = []
        with open(self._dump_filename, "at") as file:
            for line in self._list_movie:
                list_for_dump.append(line.dict_for_to_yaml())
            yaml.dump(list_for_dump, file)
        return list_for_dump

    def load(self):
        """ load all movie"""
        i = 0
        list_movie = []
        try:
            with open(self._dump_filename, "rt") as file:
                str_obj = yaml.safe_load(file)
                for mov in str_obj:
                    list_movie.append(Movie.make_obj(dict_serilization=mov))
                return list_movie
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
    print(type(mod.load()))


