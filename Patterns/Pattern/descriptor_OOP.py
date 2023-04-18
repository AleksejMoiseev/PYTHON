import os
class DescriptorValue:
    def __set_name__(self, owner, name):
        self.__name = name

    def __set__(self, instance, value):
        print('The __set__ data - descriptor  was called')
        instance.__dict__[self.__name] = value

    def __get__(self, instance, owner):
        print('The __get__ data - descriptor  was called')
        return instance.__dict__[self.__name]



class FileCount:
    def __get__(self, instance, owner):
        print('The __get__ was called')
        return len(os.listdir(instance.path))


class Folder:
    count = FileCount()

    def __init__(self, path):
        self.path = path

class B(Folder):
    pass


class Point:
    X = DescriptorValue()
    Y = DescriptorValue()
    Z = DescriptorValue()

    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z

class P(Point):
    pass

 #    def non_data(self):
 #        return self.X
 # print(p.X, p.Y, p.Z)

if __name__ == '__main__':
    # p = Point(1, 2, 3)
    # print(p.X, p.Y, p.Z)
    # print(p.__dict__)
    # # print(Point.__dict__['non_data'])
    # # print(Point.non_data)
    # # print(p.non_data)
    # p.X = 1111
    # print(p.X, p.Y, p.Z)
    folder = Folder(path='/home/alex/Documents/Projects/Proba/OOP')
    print('folder', folder.count, folder.__dict__)
    folder.count = 100
    print('folder', folder.count, folder.__dict__)
    b= B(path='/home/alex/Documents/Projects/Proba/OOP')
    print(b.count)
    b.count = 100
    print(b.count)

    p = P(1, 2, 3)
    print(p.X, p.Y, p.Z)

    p.X = 1000
    print(p.X, p.Y, p.Z)






