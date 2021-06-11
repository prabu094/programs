'''
10
1 1 2 3 4 9 8 27 16 81 32 243
'''
a = [1, 1]
n = int(input())
for i in range(n + 1):
    a.append(a[-2] * 2)
    a.append(a[-2] * 3)
print(*a[:n + 2])
