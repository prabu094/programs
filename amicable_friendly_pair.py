n1=int(input())
n2=int(input())
sum1=0
sum2=0
for i in range(1,n1):
    if(n1%i==0):
        sum1 = sum1 + i
for i in range(1,n2):
    if(n2%i==0):
        sum2 = sum2 + i
if(sum1 == n2 and sum2 == n1):
    print("amicable num (friendly pair)")
else:
    print("non amicable num (non friendly pair)")
        
