def maxSubArrayProduct(arr,size) :
    maxProduct = arr[0]
    imax = arr[0]
    imin = arr[0]
    for i in range(n): 
        if(arr[i]<0): 
            swap(imax,imin)
        imax = max(arr[i], imax * arr[i])
        imin = min(arr[i],imin * arr[i])
        maxProduct = max(maxProduct, imax)
    
    return maxProduct

arr=[4,4,4,4,4,4]
n=len(arr)
print(maxSubArrayProduct(arr,n))
