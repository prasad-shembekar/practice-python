# Write a Python program that removes and prints every third number from a list of numbers until the list is empty.

def remove_nums(int_list):
    position = 3-1
    index = 0
    len_list = (len(int_list))
    while len_list > 0:
        index = (position + index) % len_list
        print(int_list.pop(index))
        len_list -= 1

nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)