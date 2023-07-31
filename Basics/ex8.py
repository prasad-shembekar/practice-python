# Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]
# Sample Output:
# Red Black

list = input("Enter color list:").split()
len = len(list)
print(f"{list[0]} {list[len-1]}")
print("%s %s"%(list[0],list[-1]))
