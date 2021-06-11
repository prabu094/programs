row = int(input())
col = int(input())

A = [[0 for _ in range(col)] for _ in range(row)]

for i in range(col):
    for j in range(row):
        A[i][j] = int(input())

ll = []
for i in A:
    a = sum(i)
    ll.append(a)

for i in A:
    if sum(i) == max(ll):
        print(i)
