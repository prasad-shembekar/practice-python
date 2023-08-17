def is_pandigital_num(n):
    return len(set(str(n))) == 10

n = 1023456897
print("Original number:",n)
print("Check the said number is Pandigital number or not?")
print(is_pandigital_num(n))