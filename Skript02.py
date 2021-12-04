from functools import reduce
import hashlib


def f01():
    l = [1, 2, 3, 4, 5]
    m = lambda x: x * x
    f = lambda x: x % 2 != 0
    r = lambda m, x: m * x
    res1 = list(map(m, l))  # -> [1, 4, 9, 16, 25]
    res2 = list(filter(f, l))  # -> [1, 3, 5]
    res3 = reduce(r, l)  # -> 120
    print(res1)
    print(res2)
    print(res3)


def f02():
    """ Verketten """
    m = lambda x: x * x
    f = lambda x: x % 2 != 0
    r = lambda m, x: m * x

    l = list(filter(f, range(1, 10)))  # -> [1, 3, 5, 7, 9]
    l = list(map(m, l))  # -> [1, 9, 25, 49, 81]
    reduce(r, l)  # -> 893025
    reduce(r, map(m, filter(f, range(1, 10))))  # -> 893025


def f03():
    m = hashlib.sha1(b"ABCD")
    print(m.hexdigest())


if __name__ == '__main__':
    f03()
