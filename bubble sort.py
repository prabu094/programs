def sort(arr):
    n = len(arr)
  
    for i in range(n-1):

        for j in range(0, n-i-1):
  
            
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def printlist(l1):
    for i in l1:
        print(i)
        
n=int(input())
arr=list()
for i in range(n):
    arr.append(int(input()))
sort(arr)
printlist(arr)
