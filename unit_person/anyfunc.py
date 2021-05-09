




def check_conditions(a, b, c):
    m = map(lambda p: isinstance(p, (int,  float)), [a, b, c])
    if not all(m):
        raise TypeError("Not valid param")
    print("Types ok")






if __name__ == '__main__':
    check_conditions('', 1.0, 2.0)