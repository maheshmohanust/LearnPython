# from GeneratorExample import Gen as Generator
#
#
# x = Generator()
# for value in x.number_generator():
#     print(value)

a = {'Mahesh': 'UST', 'Shyam': 'Comcast'}
b = {'Urkalan': 'TCS', 'Sada': 'TCS'}
c = {**a, **b}
print(c)

author = 'Guido van Rossum'    # Python2 string formatting
date = 1989
foo = '%s started Python in %d' % (author, date)
print(foo)

author = 'Guido van Rossum'    # f-strings - New string formatting in Python3
date = 1989
foo1 = f'{author} started Python in {date}'

foo2 = f'{author.split()[0]} started Python {2000 - date} years before the turn of the century'
print(foo1)
print(foo2)


def myfunc(h, i, j):
    print(h, i, j)


tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

# myfunc(**dict_vec)
myfunc(*tuple_vec)


# def add(r=0, s=0):
#     return r + s
#
#
# d = {'a': 2, 'b': 3}
# print(add(**d))

print((lambda u, v: u + v)(5, 3))

#           or

sum_val = lambda u, v: u + v
print(sum_val(5, 3))
