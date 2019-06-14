import math

print("The contents of random library are ::")


print(dir(math))

geeks = ["Hello", "Hi", "Computer Science",
         "Data Structures", "Algorithms"]

# dir() will also list out common
# attributes of the dictionary
d = {}  # empty dictionary

# dir() will return all the available
# list methods in current local scope
print(dir(geeks))

# Call dir() with the dictionary
# name "d" as parameter. Return all
# the available dict methods in the
# current local scope
print(dir(d))


class Supermarket:

    # Function __dir()___ which list all
    # the base attributes to be used.
    def __dir__(self):
        return ['customer_name', 'product',
                'quantity', 'price', 'date']


my_cart = Supermarket()
print(dir(my_cart))


def outer_func():
    c_num = 12

    def inner_func():
        d_num = 13
        print(d_num)
        print(dir(), ' - names in inner_func')

    e_num = 14
    inner_func()
    print(e_num)
    print(dir(), ' - names in outer_func')


outer_func()