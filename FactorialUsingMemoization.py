lookup = {}


def fact_memo(n):
    if n in lookup:
        return lookup[n]
    elif n == 0:
        return 1
    else:
        lookup[n] = fact_memo(n-1) * n
        return lookup[n]


a = fact_memo(1)
print(a)
