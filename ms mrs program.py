def person_lister(func):
    def inner(people):
        return [ func(p) for p in sorted(people, key = lambda x: (int(x[2])))]
    return inner
@person_lister
def name_format(person_lister):
    return ("Mr. " if person_lister[3] == "M" else "Ms. ") + person_lister[0] + " " + person_lister[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
