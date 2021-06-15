from collections import defaultdict
text = ['bob', 'alice', 'bob', 'alice', 'bob', 'alice']

data = defaultdict(int)

ll = []

for word in text:
    data[word] += 1
    a = data[word] - 1
    if a == 0:
        ll.append(str(word))
    else:
        ll.append(str(word) + str(a))

print(ll)
