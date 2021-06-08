def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[56,78,23,98,12,56,12,4]
bubble(arr)
print("Sorted array:")
for i in range(len(arr)):
    print(arr[i])
