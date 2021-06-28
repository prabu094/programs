'''6=1+2+3=6
sum of its factors equals to the given num
'''
n=int(input())
sum1=0
for i in range(1,n):
    if(n%i==0):
        sum1=sum1 + i
if(sum1 == n):
    print("perfect number")
else:print("not")
