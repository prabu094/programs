def subArrayExists(arr, n):
    n_sum = 0
    s = set()
 
    for i in range(n):
        n_sum += arr[i]
        if n_sum == 0 or n_sum in s:
            return True
        s.add(n_sum)
    return False
arr = []
n = int(input())
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
n = len(arr)
if subArrayExists(arr, n) == True:
    print("1")
else:
    print("0")
