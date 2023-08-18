# Write a Python program to find out if a given array of integers contains any duplicate elements. Return true if any value appears at least twice in the array, and return false if every element is distinct.

def test_duplicate(array_num):
    num_set = set(array_num)
    return len(array_num) != len(num_set)

print(test_duplicate([1,2,3,4,5]))