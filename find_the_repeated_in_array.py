a=[1,6,7,43,2,54,121,33333,441144,676676,4,2,44,55,44,55,6]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            print(a[j])
            
#another method
import collections

arr = [4, 5, 66, 23, 4, 72]
count = collections.defaultdict(int)

for i in arr:
  count[i] += 1
for i in count: 
  if count[i] > 1:
    print(i)
