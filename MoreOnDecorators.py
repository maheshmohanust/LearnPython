def call_counter(func):
    def helper(*args, **kwargs):
        helper.fn_calls += 1
        return func(*args, **kwargs)

    helper.fn_calls = 0
    return helper


@call_counter
def succ(x):
    return x + 1


@call_counter
def mul(x, y=1):
    return x * y + 1


print('First Time :', succ.fn_calls)
for i in range(10):
    succ(i)
mul(3, 4)
mul(4)
mul(y=3, x=2)

print(succ.fn_calls)
print(mul.fn_calls)


# #  Using a decorator function to ensure that the argument passed to the function factorial is a positive integer


def argument_test_natural_number(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not an integer")
    return helper


@argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


for i in range(1, 10):
    print(i, factorial(i))

# print(factorial(-1))


def our_decorator(func):
    def function_wrapper(x):
        return func(x)
    return function_wrapper


@our_decorator
def succ(n):
    return n + 1


print(succ(10))


def our_decorator(func):
    def function_wrapper(x):
        return func(x)
    return function_wrapper


@our_decorator
def succ(n):
    return n + 1


print(succ(10))


class Decorator2:

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Decorating", self.f.__name__)
        self.f()


@Decorator2
def foo():
    print("inside foo()")


foo()


def outer(func):
    def inner():
        print("Decorating", func.__name__)
        func()
    return inner


@outer
def sample():
    print("inside sample()")


sample()
