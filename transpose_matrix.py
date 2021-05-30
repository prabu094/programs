m=int(input())
n=int(input())
def transpose(b):
    matrix = [[0]*len(a) for x in range(len(a[0]))]
    for i in range(len(a[0])):
        for j in range(len(a)):
            matrix[i][j] = a[j][i]
    return matrix
a=[]
for i in range(n):
    a.append([])
    for j in range(m):
        k=int(input())
        a[i].append(k)

result=transpose(a)
for i in range(len(result)):
    for j in range(len(result[0])):
        print(result[i][j],end=" ")
    print("")
