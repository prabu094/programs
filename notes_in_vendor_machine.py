nominals = (100, 50, 20, 10, 5, 2, 1)
amount = int(input())
if amount > 0:
    output = {}
    for n in nominals:
        output[n] = amount // n
        amount %= n
    for k, v in output.items():
        print(str(k)+ "\'s",'= ', str(v))
else:
    print("INVALID INPUT")
