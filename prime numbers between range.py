
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
 
n1=int(input("Enter the start number:")) 
n2=int(input("Enter the ensd number:")) 
for i in range(n1,n2): 
    if(isPrime(i)): 
        snear=i
        print(snear)
