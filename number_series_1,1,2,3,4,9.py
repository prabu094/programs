n = int(input())
ll = [1,1]
for i in range(n//2):
    ll.append(ll[-2] * 2)
    ll.append(ll[-2] * 3)
print(ll[n])
