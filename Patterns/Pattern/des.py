

class DescriptorValue:
    def __set_name__(self, owner, name):
        self.__name = name


class Point:
    X = DescriptorValue()
    Y = DescriptorValue()
    Z = DescriptorValue()

    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z


if __name__ == '__main__':
     p = Point(1, 2, 3)
     p.Z