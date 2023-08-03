# Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

# def file(x,y):
#     sum = x + y
#     if sum >= 15 and sum <= 20:
#         return 20
#     else:
#         return sum

# print(file(10,6))
# print(file(10,12))

def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum


print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))
