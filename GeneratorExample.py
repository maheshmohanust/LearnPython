def simple_generator():
    yield "Mahesh"
    yield "Meenu"
    yield "Adithi"
    yield "Avni"


def number_generator():
    for j in range(101):
        yield j


x = simple_generator()
for i in x:
    print(i)

for value in number_generator():
    print(value)

# print(x.__next__()); # In Python 3, __next__()
