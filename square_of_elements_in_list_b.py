A = [1, 2, 3, 4]
B = [5, 6, 7, 8]


def fun(x):
    i, j = x
    return i ** j


print(list(map(lambda x: fun(x), list(zip(A, B)))))
