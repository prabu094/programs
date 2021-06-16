n = int(input())
count=0
res = ''
for i in range(1, n//3):
    for j in range(i):
        res += chr(96 + i)
        count +=1
        if count > n:
            break

print(res[:n])
