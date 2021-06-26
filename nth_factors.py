# This function computes the factor of the argument passed
'''
input:12,3
output:4
'''
l=[]
n,n2=[int(i) for i in input().split(",")]
for i in range(1, n + 1):
    if n % i == 0:
        l.append(i)
k=len(l)
if(n2 > k):
    print(1)
else:
    print(l[n2])
