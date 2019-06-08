from CustomException import *


class MyException:
    def gotta_throw_error(self, a):
        b = 0
        try:
            if a < 100:
                raise ValueTooSmallError('x should not exceed 5. The value of x was: {}'.format(a))
            elif a > 1000:
                raise ValueTooLargeError
            else:
                b = a * a
        except ValueTooSmallError:
            print("This value is too small, try again!")
        except ValueTooLargeError:
            print("This value is too large, try again!")
        return b


exc = MyException()
val = exc.gotta_throw_error(200)
print(val)
exc.gotta_throw_error(99)
exc.gotta_throw_error(1001)