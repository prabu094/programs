'''input=5
   array_element=[1,1,2,3,5]
   Output=8(next element of fibo series)'''



def is_arithmetic(l):
    delta = l[1] - l[0]
    for index in range(len(l) - 1):
        if not (l[index + 1] - l[index] == delta):
            return False
    return True


def is_geometric(l):
    if len(l) <= 1:
        return True
    ratio = l[1] / float(l[0])
    for i in range(1, len(l)):
        if l[i] / float(l[i - 1]) != ratio:
            return False
    return True


def is_fibbo(l):
    if l[0] + l[1] == l[2]:
        return True
    return False

def AP(l):
    delta = l[1] - l[0]
    return l[-1] + delta

def FIBBO(l):
    return l[-1] + l[-2]

def GP(l):
    ratio = l[1] / float(l[0])
    return l[-1] / ratio
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
if (is_fibbo(l)):
    print(l[-1] + l[-2])
elif(is_geometric(l)):
  print(AP(l))
else:
  print(GP(l))
