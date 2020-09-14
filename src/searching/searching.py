def linear_search(arr, target):
    for i in arr:
        if i == target:
            return arr.index(i)


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    high = len(arr) -1
    low = 0
    mid = 0
    while low <= high:
        
        mid = (high+low)//2
    
        
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            high = mid-1
        else:
            low = mid+1
        


    return -1  # not found

  
   
  
    