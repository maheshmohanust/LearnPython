import os
import json


class Hello(object):
    def __init__(self):
        pass

    def print_current_path(self):
        print(os.getcwd())

    def add_nums(self, a, b):
        c = a + b
        return c

    def write_to_file(self, filename):
        f = open("C:\\Users\\mmohan2\\Test Data\\"+filename, "wt")
        f.write("Hello World")
        f.close()

    def print_json(self):
        x = '{ "name":"John", "age":30, "city":"New York"}'
        y = json.loads(x)
        print(y["age"])

    x = lambda self, n: n * n


h = Hello()
h.print_current_path()
val = h.add_nums(5, 10)
print(val)
h.write_to_file("sample.txt")
h.print_json()
lam = h.x(10)
print(lam)


def outer(x):
    result = 0

    def inner(n):
        nonlocal result
        while n > 0:
            result += x * n
            n -= 1
        return result
    return inner


myfunc = outer(7)
print(myfunc(5))
