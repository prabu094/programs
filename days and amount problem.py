def validate(n,s,m):
    try:
        l=n*m
        if(s//l !=0):
            return 1
        else:
            return 0
    except:
        return 2
def times(n,s,m):
    l=n*m
    if(s//l !=0):
        return 1
        
n=int(input())
s=int(input())
m=int(input())
flag=validate(n,s,m)
if(flag == 1):
    print("spend on", times(n,s,m) ,"times")
elif(flag==0):
    print("not possible")
else:
    print("invalid")
    
