g = {}
slov = {'a': 1, 'b': 2, 'c': 5, 'd': 3}
zz = sorted(slov.values(), reverse=True)
zz.reverse()

for f in map(lambda x: x, zz):
    for k, v in slov.items():
        if slov.get(k) == f:
            g[k] = f

print(g)


def sort_of_dictionary(dic={}, flag = True):
    g = {}
    zz = sorted(dic.values(), reverse=flag)
    for f in map(lambda x: x, zz):
        for k, v in slov.items():
            if slov.get(k) == f:
                g[k] = f
    return g

print(sort_of_dictionary(dic=slov, flag=False))