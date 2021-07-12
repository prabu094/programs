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
n=144
fibo=[0,1]
for i in range(20):
    fibo.append(fibo[-1] + fibo[-2])
    

i=0

while (fibo[i] < 145):
    if(isPrime(fibo[i])):
        print(fibo[i])
    i +=1
