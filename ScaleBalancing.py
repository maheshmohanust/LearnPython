import itertools


class ScaleBalancing(object):

    def __init__(self):
        pass

    def find_balanced_scale(self, array):
        x = list(int(i) for i in array[0][1:-1].split(','))
        y = list(int(i) for i in array[1][1:-1].split(','))
        for a in y:
            if x[0] + a == x[1] or x[1] + a == x[0]:
                return str(a)
        for pair in itertools.combinations(y, 2):
            if pair[0]+x[0] == x[1]+pair[1] or pair[0]+x[1] == pair[1]+x[0] or pair[0]+pair[1]+x[0] == x[1] or pair[0]+pair[1]+x[1] == x[0]:
                a, b = min(pair), max(pair)
                return ','.join([str(a), str(b)])
        return 'Not possible'


sb = ScaleBalancing()
li = sb.find_balanced_scale(["[13, 4]", "[1, 2, 3, 6, 14]"])
print(li)
