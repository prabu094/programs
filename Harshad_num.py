'''
Ex– Number is 21

it is divisible by own sum (1+2) of its digit(2,1)

So it is harshad number

Some other harshad number are 156,54,120 et

'''


n=input()
k=[int(i) for i in n]
k=sum(k)
if(int(n) % k==0):
    print("Harshad num")
else:print("not Harshad  num")
