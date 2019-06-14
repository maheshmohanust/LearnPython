class Gen:
    def simple_generator(self):
        yield "Mahesh"
        yield "Meenu"
        yield "Adithi"
        yield "Avni"

    def number_generator(self):
        for j in range(11):
            yield j


x = Gen()
k = x.simple_generator()
for i in k:
    print(i)

for value in x.number_generator():
    print(value)

# print(x.__next__()); # In Python 3, __next__()
