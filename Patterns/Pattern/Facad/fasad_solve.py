from abc import ABC, abstractmethod


class StartHomeTheater(ABC):
    @abstractmethod
    def turn_on_toaster(self):
        pass

    @abstractmethod
    def turn_on_light(self):
        pass

    @abstractmethod
    def open_screen(self):
        pass

    @abstractmethod
    def turn_on_amplifier(self):
        pass

    def run_prepare_watch_move(self):
        self.turn_on_light()
        self.turn_on_toaster()
        self.open_screen()
        self.turn_on_amplifier()


class MiddleHomeTheater(ABC):
    @abstractmethod
    def connect_projector_and_screen(self):
        pass

    @abstractmethod
    def turn_off_toaster(self):
        pass

    @abstractmethod
    def make_toast(self):
        pass

    @abstractmethod
    def turn_on_projector(self):
        pass

    @abstractmethod
    def turn_on_amplifier(self):
        pass

    def run_equipment(self):
        self.make_toast()
        self.turn_on_amplifier()
        self.turn_on_projector()
        self.turn_off_toaster()
        self.connect_projector_and_screen()


class StartStopFilm(ABC):
    @abstractmethod
    def projector_start_film(self):
        pass

    @abstractmethod
    def projector_stop_film(self):
        pass

    @abstractmethod
    def turn_off_light(self):
        pass

    @abstractmethod
    def insert_film_in_projector(self):
        pass

    @abstractmethod
    def amplifier_setup_volume(self):
        pass


class EndedSeeFilm(ABC):
    @abstractmethod
    def take_off_film_of_projector(self):
        pass

    @abstractmethod
    def turn_off_amplifier(self):
        pass

    @abstractmethod
    def disconnect_projector_and_screen(self):
        pass

    @abstractmethod
    def turn_off_projector(self):
        pass

    @abstractmethod
    def close_screen(self):
        pass


class Facade:
    def __init__(
            self,
            preparing_to_watch: StartHomeTheater,
            watching_a_movie: StartStopFilm,
            end_of_movie: EndedSeeFilm,
            preparing_to_equipment: MiddleHomeTheater

    ):
        self.preparing_to_watch = preparing_to_watch
        self.watching_a_movie = watching_a_movie
        self.end_of_movie = end_of_movie
        self.preparing_to_equipment = preparing_to_equipment

    def preparing_to_watch_move(self):
        self.preparing_to_watch.run_prepare_watch_move()

    def preparing_equipment(self):
        self.preparing_to_equipment.run_equipment()

    def watch_film(self):
        self.watching_a_movie.insert_film_in_projector()
        self.watching_a_movie.projector_start_film()
        self.watching_a_movie.turn_off_light()
        self.watching_a_movie.amplifier_setup_volume()

    def end_watched_movie(self):
        self.watching_a_movie.projector_stop_film()
        self.preparing_to_watch.turn_on_light()
        self.end_of_movie.take_off_film_of_projector()
        self.end_of_movie.close_screen()
        self.end_of_movie.turn_off_projector()
        self.end_of_movie.turn_off_amplifier()
