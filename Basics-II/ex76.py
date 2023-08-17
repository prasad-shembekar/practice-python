# Write a Python program to find the starting and ending position of a given value in a given array of integers, sorted in ascending order.

def search(array_num,target):
    result_area = []
    start_pos = 0
    end_pos = 0

    for i in range(len(array_num)):
        if target == array_num[i] and start_pos == -1:
            start_pos = i
            end_pos = i
        elif target == array_num[i] and start_pos != -1:
            end_pos = i
    result_area.append(start_pos)
    result_area.append(end_pos)
    return result_area


