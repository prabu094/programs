n = int(input())

m = int(input())

A = [ [ 0 for i in range(m) ] for j in range(n) ]

for i in range(n):
    for j in range(m):
        A[i][j]=int(input())

sum1 = 0
sum2 = 0
for i in range(n):
    for j in range(m):
        if i == j:
            sum1 += A[i][j]

        if i + j == n - 1:
            sum2 += A[i][j]

print(sum1)
print(sum2)
