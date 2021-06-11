a=[1]
n=int(input())
for i in range(2,n+1):
    a.append(a[-1] * i)
print(*a)
