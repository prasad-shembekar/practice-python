# Write a Python program that accepts six numbers as input and sorts them in descending order.

print("Inpute 6 integer: ")
nums = list(map(int,input().split()))
nums.sort()
nums.reverse()
print(*nums)