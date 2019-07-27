def fact_tab(num):
    lookup = list(range(num + 1))
    lookup[0] = 1

    for i in range(1, num + 1):
        lookup[i] = lookup[i - 1] * i

    print(lookup[num])


n = 3
fact_tab(n)
