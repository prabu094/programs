a = list(map(int,input("Enter Array Elements").split()))
n = int(input("No. of rotation : "))
for i in range(n):
    first = a[0]
    for j in range(len(a) - 1):
        a[j] = a[j+1]
    a[len(a) - 1] = first

print(a)


#To remove time complexity issues!


def rotLeft(a, d):
    # Write your code here
    alist = list(a)
    b = alist[d:]+alist[:d]
    return b
print(rotLeft(a,n-1))
