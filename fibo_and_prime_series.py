'''20
[1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17, 21, 19, 34, 23, 55, 29]
'''

import math

num = int(input())


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


prime = []
for i in range(2, num * 2):
    if isPrime(i):
        prime.append(i)

fibo = [0, 1]
for i in range(2, (num // 2) + 1):
    fibo.append(fibo[-1] + fibo[-2])
fibo.remove(0)


prime = prime[:num//2]


def merge_lists(list1, list2):
    list3 = []
    while True:
        try:
            list3.append(list1.pop(0))
            list3.append(list2.pop(0))
        except IndexError:
            break
    return list3

print(merge_lists(fibo, prime))
