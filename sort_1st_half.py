# Sort first half in ascending order and second half in descending :
a=[1,6,7,43,2,54,1]
print(sorted(a[:len(a)//2]) + sorted(a[len(a)//2:],reverse=True))
