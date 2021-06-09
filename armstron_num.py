sum=0
a=int(input())
num = [int(d) for d in str(a)]
for i in num:
    sum+=i**len(num)
print(sum==a)
