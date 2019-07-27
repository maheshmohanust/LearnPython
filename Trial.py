# import random
# import string
#
#
# sample_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(4))
# server = sample_str + '-esa00.perf'
# print(server)
#
# my_list = []
# alphabet_string = string.ascii_uppercase
# for i, j in enumerate(alphabet_string, 1):
#     my_list.append((i,j))
# for index, item in my_list:
#     print("Position of " + item + " in alphabetical order is " + str(index))
#
# for i in range(97, 123):
#     print(chr(i))
#
# for i in range(65, 91):
#     print(chr(i))

li = list(range(10))
for i in reversed(range(0, len(li))):
    num = li[i]
    if i != 0:
        print(num, end=",")
    else:
        print(i)