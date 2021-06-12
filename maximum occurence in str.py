from collections import Counter
string=input()
count=Counter(string)
print(count)
count=max(count,key=count.get)
print(count)
