# Write a Python program to find the highest and lowest number from a given string of space-separated integers.

def highest_num(str1):
    num_list = list(map(int,str1.split()))
    return max(num_list),min(num_list)

text= "1 4 5 77 9 0"
print("Num are",highest_num(text))