def com(x,y):
    while(y):
        x,y = y, x%y
    return x
x=int(input())
y=int(input())

hcf = com(x,y)
print(hcf)
