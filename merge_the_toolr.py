'''Sample Input:

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
Sample Output:

AB
CA
AD'''
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        uniq = ''
        for c in string[i : i+k]:
            if (c not in uniq):
                uniq+=c
        print(uniq)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    
