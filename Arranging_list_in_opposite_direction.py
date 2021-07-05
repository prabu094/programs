l=[1,2,3,80,4,5,6,8,9]
l.sort()
n=len(l)//2
k=l[n:]
k=l[:n] + k[::-1]
print(k)
print("".join(map(str,k)))
