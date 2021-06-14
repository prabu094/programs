n=input()
n=n[::-1]
finalresult=''
num=''
for i in range(len(n)):
    num = num +n[i]
    if (int(num) >=65 and int(num) <=90) or (int(num) >= 97 and int(num) <=122) or int(num) ==32:
        chara=chr(int(num))
        finalresult += chara
        num=''
print(finalresult)
