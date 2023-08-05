# Write a Python program to sum the first n positive integers.

# def sum(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i
#     return sum


# print(sum(5))


n = int(input())
sum = (n*(n+1))/2
print(sum)
