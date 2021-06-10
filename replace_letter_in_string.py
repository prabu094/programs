a,b,c=input().split()
k="aeiouAEIOU"
f='#'
g='%'
for i in k:
    a=a.replace(i,f)
for i in b:
    if(i not in k):
        b=b.replace(i,g)
print(a+b+c.capitalize())
