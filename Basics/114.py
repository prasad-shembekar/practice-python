# Write a Python program to filter positive numbers from a list.

nums = [34,1,0,-23,12,-88]
print("Original list:",nums)
new = list(filter(lambda x:x>0,nums))
print(new)