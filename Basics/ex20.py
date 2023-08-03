# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

# def copies(str,n):
#     return str*3

# n = int(input("Enter copies you want"))
# str = input("Enter string")

# ans = copies(str,n)
# print(ans)

def copies(text,n):
    result = ""
    for i in range(n):
        result = result + text
    return result

print(copies("hello",5))