import itertools


def find_combination_using_combination(str_array):
    for pair in itertools.combinations(str_array, 2):
        if pair[0] + pair[1] in str_array:
            return str(pair[0]) + ' + ' + str(pair[1]) + ' = ' + str(pair[0]) + str(pair[1])
    return None


def find_combination_using_loops(str_array):
    for i in range(len(str_array)):
        for j in range(i+1, len(str_array)):
            if str_array[i] + str_array[j] in str_array:
                return str_array[i] + ' + ' + str_array[j] + ' = ' + str_array[i] + str_array[j]
    return None


li = ['aru', 'chitti', 'eswar', 'revanth', 'arueswar']
print(find_combination_using_combination(li))
print(find_combination_using_loops(li))
print(id(find_combination_using_loops))
