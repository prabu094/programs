# Find all Symmetric pairs in an array

arr = []

n = int(input())

def fun(a):
  x, y = a
  a = y, x 
  return list(a)

for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(1, (n // 2) + 1):
    if arr[i - 1] == fun(tuple(arr[- i])):
        print(arr[i - 1])


