
class EUSockInterface:
    def voltage(self):
        pass

    def live(self):
        pass

    def neutral(self):
        pass

    def zero(self):
        pass


# класс которому нужен адаптер к целевому интерфейсу
class Socket(EUSockInterface):
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def zero(self):
        return 0





# Целевой интерфейс
class USASockInterface:
    def voltage(self):
        pass

    def live(self):
        pass

    def neutral(self):
        pass


class Adapter(Socket, USASo1111ckInterface):

    def voltage(self):
        voltage = super().voltage()
        return voltage/2 - 10

    def live(self):
        return super().live()

    def neutral(self):
        return super().neutral()

    def zero(self):
        return super().zero()




# тостер
class Toaster:
    __power = None

    def __init__(self, power):
        self.__power = power

    def do_toast(self):
        if self.__power.voltage() > 110:
            print("Toaster is dead!")
        else:
            if self.__power.live() == 1 and self.__power.neutral() == -1 and self.__power.zero() == 0:
                print("That's your toast!")
            else:
                print("No power.")


if __name__ == "__main__":
    pow = Adapter()
    t = Toaster(power=pow)
    t.do_toast()