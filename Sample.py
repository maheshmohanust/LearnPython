import re


e = re.search(r'[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$', 'ayushi123@gmail.com')
print(e.group())


def extend_list(val, li=[]):
    li.append(val)
    return li


list1 = extend_list(10)
list2 = extend_list(123, [])
list3 = extend_list('a')
print(list1, list2, list3)


def switch(case):
    default = 'Sunday'
    switcher = {
        'M': 'Monday',
        'T': 'Tuesday',
        'W': 'Wednesday'
        }
    return switcher.get(case, default)


print(switch('M'))
print(switch('S'))

#  https://data-flair.training/blogs/python-programming-interview-questions/
#  https://hackaday.com/2018/08/15/stop-using-python-2-what-you-need-to-know-about-python-3/
