import math 
def isPrime(num): 
    if(num==2 or num==3 or num==5 or num==7):	 
        prime=True 
    elif(num%2==0 or num%3==0 or num%5==0 or num%7==0): 
    	prime=False	 
    elif(math.ceil(math.sqrt(num))-math.floor(math.sqrt(num))==0): 
        prime=False 
    else:	 
        prime=True 
 
    return(prime) 
 
n=[43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,6,8,24,56,87,88,26,97]
n1=[]
for i in n: 
    if(isPrime(i)): 
        n1.append(i)
print(n1)
print(max(set(n1)))
print(min(set(n1)))
