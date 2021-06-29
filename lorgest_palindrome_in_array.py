a=[1,6,7,43,2,54,121,33333,441144,676676]
k=sorted([i for i in a if str(i)==str(i)[::-1]],reverse=True)
print(k[0])
