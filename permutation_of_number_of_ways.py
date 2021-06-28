import math
n=int(input("no.of students:"))
r=int(input("no.of seats:"))
num=math.factorial(n)
den=math.factorial(n-r)
k=num//den
print("toal permutations:",k)
