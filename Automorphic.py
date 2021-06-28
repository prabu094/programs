'''
input=5
output=auto..
exp: 5**2=25
last digit =5


'''
n=int(input())
n1=n**2
n=str(n)
k=len(n)
n1=str(n1)
if (n == n1[-len(n):]):
    print("Automorphic")
else:print("non-automorphic")
