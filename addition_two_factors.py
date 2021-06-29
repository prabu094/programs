n1=int(input())
d1=int(input())
n2=int(input())
d2=int(input())
if(d1 == d2):
    fraction = n1 + n2
    print("additions of factors:",fraction,"/",d1)
else:
    fraction=(n1*d2) + (n2 * d1)
    print("additions of factors:",fraction,"/",d1 * d2)
