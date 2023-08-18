def max_pair(arr):
    arr_len = len(arr)
    if (arr_len < 2):
        print("No pairs exists")
        return None
    
    x = arr[0]; y = arr[1]

    for i in range(0,arr_len):
        for j in range(i +1,arr_len):
            if (arr[i] * arr[j] > x*y):
                x = arr[i]; y = arr[j]

    return x,y

nums = [1, 2, 3, 4, 7, 0, 8, 4] 
print("Original array:", nums)
print("Max product pair:",max_pair(nums))