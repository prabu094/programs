"""
Input: N = 45
Output: 3
Explanation:
Below are the prime numbers up to 45 that can be expressed as sum of consecutive prime numbers:

5 = 2 + 3
17 = 2 + 3 + 5 + 7
41 = 2 + 3 + 5 + 7 + 11 + 13
Therefore, the count is 3. 

Input: N = 4
Output: 0 


"""num = int(input())
arr = []
sum = 0
count = 0
if num > 1:
    for i in range(2, num + 2):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            arr.append(i)
def is_prime(sum):
    for i in range(2, (sum // 2) +2):
        if sum % i == 0:
            return False
        else:
            return True
for i in range(0, len(arr)):
    sum = sum + arr[i]
    if sum <= num:
        if is_prime(sum):
            count = count + 1

print(count)
