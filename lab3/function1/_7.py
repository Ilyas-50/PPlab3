def has_33(arr):
    for i in range(len(arr) - 1):
        if arr[i] == 3 and arr[i+1] == 3:
            return True
    return False 
        
print(has_33([3, 1, 3]))
