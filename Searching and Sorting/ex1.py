# Binary Search 

def binary_search(item_list,target):
    first = 0 
    last = len(item_list)-1
    found = False

    while(first<=last and not found):
        mid = (first + last) // 2
        if item_list[mid] == target:
            found = True
        else:
            if target < item_list[mid]:
                last = mid -1
            else:
                first = mid + 1
    return found 

print(binary_search([1,2,3,4,5,6],6))