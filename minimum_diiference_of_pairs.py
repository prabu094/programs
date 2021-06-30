a = [1, 99, 22, 44, 1001]
minvalue = 1e13
a.sort()

for i in range(1, len(a)):
    k = abs(a[i] - a[i - 1])
    if minvalue > k:
        minvalue = min(minvalue, k)

print(minvalue)
res = []
for i in range(len(a) - 1, -1, -1):
    k = abs(a[i] - a[i - 1])
    if k == minvalue:
        res.extend([a[i], a[i - 1]])

print(*sorted(res))
