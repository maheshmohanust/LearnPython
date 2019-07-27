def find_longest_substring(s1, s2):
    sub_str = ""
    for i in range(len(s1)):
        match = ""
        for j in range(len(s2)):
            if i + j < len(s1) and s1[i + j] == s2[j]:
                if s1[i + j] != ' ':
                    match += s2[j]
                else:
                    match = ""
            elif len(match) > len(sub_str):
                    sub_str = match
                    match = ""
    if len(sub_str) > 0:
        return sub_str
    else:
        return None


a = 'Americans are rich and healthy'
b = 'America is a beautiful country'

str1 = find_longest_substring(a, b)
print('Longest common substring is:', str1)
print('Length of longest common substring is:', len(str1))
