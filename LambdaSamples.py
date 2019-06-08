def lambda_func(n):
    return lambda a: a * n


triple = lambda_func(3)

print(triple(5))


def f(x):
    return x * x


def modify_list(a, fn):
    for i, v in enumerate(a):
        a[i] = fn(v)


L = [1, 3, 2]
modify_list(L, f)
print(L)


def fill_values(m):
    a = list(range(m))
    for i in range(0, m):
        if i == 0:
            j = 1
        else:
            j = i + 1
        val = j * 10
        a[i] = val
    print(a)


fill_values(10)
