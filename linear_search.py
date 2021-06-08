n=[2,45,56,23,67,1,9]
n1=909
flag=0
for i in range(len(n)):
    if n1 == n[i]:
        flag=i
        break
    else:
        flag=0
if (flag > 0):
    print("element found in:",flag)
else:
    print("not found")
