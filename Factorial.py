import pdb


class FactorialSample:

    def find_fact(self, n):
        if n == 1:
            return 1
        else:
            return n * self.find_fact(n-1)

    def get_fib(self, n):
        a = list(range(n))
        a[0] = 0
        a[1] = 1
        pdb.set_trace()
        for i in range(2, n):
            a[i] = a[i-1] + a[i-2]
        return a


f = FactorialSample()
val = f.find_fact(3)
print(val)

fib_val = f.get_fib(5)
print(fib_val)



