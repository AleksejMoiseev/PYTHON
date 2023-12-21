from abc import ABC, abstractmethod


class HomeTheater(ABC):
    @abstractmethod
    def turn_on_toaster(self):
        pass

    @abstractmethod
    def turn_off_toaster(self):
        pass

    @abstractmethod
    def make_toast(self):
        pass

    @abstractmethod
    def turn_on_light(self):
        pass

    @abstractmethod
    def turn_off_light(self):
        pass

    @abstractmethod
    def open_screen(self):
        pass

    @abstractmethod
    def close_screen(self):
        pass

    @abstractmethod
    def turn_on_projector(self):
        pass

    @abstractmethod
    def turn_off_projector(self):
        pass

    @abstractmethod
    def connect_projector_and_screen(self):
        pass

    @abstractmethod
    def disconnect_projector_and_screen(self):
        pass

    @abstractmethod
    def turn_on_amplifier(self):
        pass

    @abstractmethod
    def turn_off_amplifier(self):
        pass

    @abstractmethod
    def insert_film_in_projector(self):
        pass

    @abstractmethod
    def take_off_film_of_projector(self):
        pass

    @abstractmethod
    def amplifier_setup_volume(self):
        pass

    @abstractmethod
    def projector_start_film(self):
        pass

    @abstractmethod
    def projector_stop_film(self):
        pass