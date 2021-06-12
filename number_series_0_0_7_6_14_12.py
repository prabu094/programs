n = int(input())
ll = [0,0]
for i in range(n//2):
    ll.append(ll[-2] + 7)
    ll.append(ll[-2] + 6)
print(*ll)
print(ll[n])
