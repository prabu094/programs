a = [0, 0]
n = int(input())
for i in range(n + 1):
    a.append(a[-2] + 2)
    a.append(a[-1] // 2)
print(*a[:n + 2])
