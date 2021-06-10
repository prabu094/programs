'''
input:10
output:[0, 0, 2, 1, 4, 2, 6, 3, 8, 4, 10, 5]'''
n=int(input())
l=[0]
a=0
for i in range(n+1):
    if(i==0 and i==1):
        l.append(0)
        break
    
    elif(i%2!=0):
        a=a+2
        l.append(a)
    else:
        b=0
        b=a/2
        l.append(int(b))
print(l)
