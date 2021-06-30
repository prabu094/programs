s='abc'
k=[(x,y,z) for x in s for y in s for z in s if x!=y and x!=z and y!=z and y!=x and z!=x and z!=y]
print(k)
