def solve(s):
    for x in s[:].split():
         s= s.replace(x, x.capitalize())
    return s
s="hello world guy"
print(solve(s))
