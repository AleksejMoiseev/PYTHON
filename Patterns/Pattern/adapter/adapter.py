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


class Adapter(USASockInterface):
    def __init__(self, sock: Socket):
        self.sock = sock

    def voltage(self):
        voltage = self.sock.voltage()
        return voltage/2 - 10

    def live(self):
        return self.sock.live()

    def neutral(self):
        return self.sock.neutral()



# тостер
class Toaster:
    __power = None

    def __init__(self, power):
        self.__power = power

    def do_toast(self):
        if self.__power.voltage() > 110:
            print("Toaster is dead!")
        else:
            if self.__power.live() == 1 and self.__power.neutral() == -1:
                print("That's your toast!")
            else:
                print("No power.")


if __name__ == "__main__":
    sock = Socket()
    power = Adapter(sock=sock)
    t = Toaster(power=power)
    t.do_toast()