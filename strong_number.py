def fact(n):
    if n==1:
        return 1 
    else:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
    return fact
n=int(input())
l=[int(x) for x in str(n)]
k=[]
for i in l:
    k.append(fact(i))
print(sum(k))
