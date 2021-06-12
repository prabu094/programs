intr = int(input())
extr = int(input())


i_l=[float(input()) for _ in range(intr)]
e_l=[float(input()) for _ in range(extr)]

cost = (sum(i_l) * 18) + (sum(e_l) * 12)
print(cost," INR")
