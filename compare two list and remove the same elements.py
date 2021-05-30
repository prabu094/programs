n=input()
a=input()
l1=[]
l2=[]
for i in n:
    l1.append(i)
for j in a:
    l2.append(j)
for i in l1:
    if i in l2:
        l1.remove(i)
for i in l1:
    if i in l2:
        l1.remove(i)
for i in l1:
    if i in l2:
        l1.remove(i)
l3="".join(str(i) for i in l1)
print(l3)
