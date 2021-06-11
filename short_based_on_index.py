'''Input Format

The first line contains  and  separated by a space.
The next  lines each contain  elements.
The last line contains .

Constraints



Each element 

Output Format

Print the  lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

Sample Input 0

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
Sample Output 0

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
Explanation 0

The details are sorted based on the second attribute, since  is zero-indexed.'''
def sorted(arr):
    for i in range(n-1):
        if arr[i][k] > arr[i+1][k]:
            second_large = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = second_large
        
    for i in range(n-1):
        if arr[i][k] > arr[i+1][k]:
            sorted(arr)
    
    return True
            




if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
        

    k = int(input())
    
    if sorted(arr) == True:
        for i in range(n):
            for j in range(m):
                print(arr[i][j],end=" ")
            print(end="\n")
