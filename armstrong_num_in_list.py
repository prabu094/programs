n = input()

print(sum(list(map(lambda x : x ** 3, list(map(int, n))))) == int(n))
