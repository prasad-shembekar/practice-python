# Write a Python program to calculate sum of digits of a number.

# def sum(n):
#     sum1 = 0

#     for i in n:
#         sum1 = sum1 + int(i)

#     print(sum1)


# sum("5245")

def sum(n):
    temp = 0
    while n != 0:
        digit = int(n % 10)
        temp += digit
        n = n / 10
    print(temp)


sum(5245)
