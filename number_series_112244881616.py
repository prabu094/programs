n=int(input())
n1=int(input())
n2=int(input())
l=[1,1]
for i in range(1,n//2):
    l.append(l[-2]*n1)
    l.append(l[-2]*n2)
print(l)
