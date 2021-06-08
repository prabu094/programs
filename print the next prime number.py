lower = int(input("Enter lower range: "))  
  
  
for num in range(lower,lower+20):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
            print(num)
            break;
