import math

l1 = list(map(int, input("Enter Array").split()))


ll = {}
a = math.ceil(len(l1) / 2)
for i in range(len(l1) + 1):
    ll[sum(l1[i:i + a])] = l1[i: i + a]

i, j = max(ll.items())
print(i)
print(j)
