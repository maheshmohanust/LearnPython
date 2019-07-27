def longest_substring(x, y, m, n):

    # lookup = [[0]*(n+1)]*(m+1)
    lookup = [[0 for k in range(n + 1)] for l in range(m + 1)]
    result = 0
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lookup[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
                result = max(result, lookup[i][j])
            else:
                lookup[i][j] = 0
    return result


a = 'OldSite:GeeksforGeeks.org'
b = 'NewSite:GeeksQuiz.com'

p = len(a)
q = len(b)

print('Length of longest common substring is:', longest_substring(a, b, p, q))
