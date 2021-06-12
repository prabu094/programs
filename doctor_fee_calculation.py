age=[]
for i in range(20):
    n=input()
    if(n == ""):
        break
    elif(int(n) in range(0,120)):
        age.append(int(n))
    else:
        print("invalid input")
        exit()
fee=0 
for i in age:
    if i in range(1,17):
        fee =fee+200
    elif(i in range(18,40)):
        fee=fee+400
    else:
        fee=fee+300
print(fee)
