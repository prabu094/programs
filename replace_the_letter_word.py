'''input:
INPUT          Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k''''


def mutate_string(string, position, character):
    k=""
    k=string[:position] + character + string[position+1:]
    return k

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
