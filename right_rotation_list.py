def rotright(a, d):
    # Write your code here
    alist = list(a)
    b = alist[-d:]+alist[:-d]
    return b
a=[1,2,3,4]
d=4
print(rotright(a,d))
