import math


def isPrime(num):
    if num == 2 or num == 3 or num == 5 or num == 7:
        prime = True
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        prime = False
    elif math.ceil(math.sqrt(num)) - math.floor(math.sqrt(num)) == 0:
        prime = False
    else:
        prime = True
    return prime


n = int(input())
ll = []
for i in range(2, n + 1):
    if isPrime(i):
        ll.append(i)
res = []
for i in ll:
    a = n - i
    if a in ll:
        print(i, a)
        ll.remove(i)
