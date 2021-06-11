s = 'ABCDCDC'
n = 'AB'

count = 0
for i in range(len(s)):
    if n in s[i: i + len(n)]:
        count += 1

print(count)
