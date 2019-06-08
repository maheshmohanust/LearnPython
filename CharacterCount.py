def find_count(string):
    # my_dict = {}
    my_dict = dict()
    for s in string:
        if not s.isspace():
            k = s.lower()
            if k not in my_dict:
                my_dict[k] = 1
            else:
                my_dict[k] = my_dict[k] + 1
    return my_dict


count = find_count("India is my country")
for key, value in count.items():
    print(str(key) + " = " + str(value))
