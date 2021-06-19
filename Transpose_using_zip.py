a = [[1, 2, 3],
     [5, 6, 7],
     [9, 10, 11]
     ]

res = []

a = [list(x) for x in zip(*a)]

print(a)
