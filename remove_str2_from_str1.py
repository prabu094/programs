n=input()
a=input()
for i in n:
    for j in a:
        if i == j:
            n=n.replace(i,"")
print(n)
