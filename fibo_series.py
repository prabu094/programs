a = [0, 1]

n = int(input())

for i in range(2,n):
    a.append(a[-1] + a[-2])

print(*a)
