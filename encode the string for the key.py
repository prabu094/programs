'''
Example 1:
Enter your PlainText: All the best
Enter the Key: 1

The encrypted Text is: Bmm uif Cftu
'''

s = input()
key = int(input())


def encode(key, s):
    res = ''
    for i in s:
        if i.isalpha():
            res += chr(ord(i) + key)
        elif i.isdigit():
            res += str(int(i) + key)
        elif i == '-':
            res += '-'
        elif i.isspace():
            res += " "
    return res.replace("!", " ")


print(encode(key, s))
