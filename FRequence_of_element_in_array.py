# Finding the frequency of elements in an array
import collections

arr = [4, 3, 99, 3, 99]

count = collections.defaultdict(int)

for i in res:
  count[i] += 1
  if count[i] == 1:
    print(i, ":", arr.count(i))
