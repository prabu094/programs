'''
i/p:24,-14
o/p:4th quadrant

'''

n1,n2=input().split(",")
n1=int(n1)
n2=int(n2)
if(n1>0 and n2>0):print("1st quadrant")
elif(n1<0 and n2>0):print("2nd quadrant")
elif(n1 <0 and n2<0):print("3rd quadrant")
elif(n1>0 and n2<0):print("4th quadrant")
