if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort()
    l=max(arr)
    while max(arr) == l:
        arr.remove(l)
    print(max(arr))
