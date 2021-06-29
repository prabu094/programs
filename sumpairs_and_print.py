'''
25 45 30
70 30
100
'''


def pairwiseSum(lst, n):
    s = []
    for i in range(0, n + 1, 2):
        try:
            res = lst[i] + lst[i + 1]
            s.append(res)
        except:
            s.append(lst[i])
    print(*s)
    if len(s) > 2:
        pairwiseSum(s, len(s))
    else:
        print(sum(s))

arr = [10,15,20,25,30]
size = len(arr)
pairwiseSum(arr, size)
