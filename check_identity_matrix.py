n = int(input())

m = int(input())

A = [ [ 0 for i in range(m) ] for j in range(n) ]

for i in range(n):
    for j in range(m):
        A[i][j]=int(input())

Flag = []
for i in range(n):
    for j in range(m):
        if i == j:
            Flag.append(A[i][j])

if Flag.count(A[0][0]) == n:
    print("Identity")
else:
    print("Not Identity")
