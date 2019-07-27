class MyMath:

    def check_palindrome(self, string):
        string1 = ""
        for s in reversed(string):
            string1 += s
        if string == string1:
            print("Given string is a palindrome")
        else:
            print("Given string is not a palindrome")



mym = MyMath()
mym.check_palindrome('malayalam')