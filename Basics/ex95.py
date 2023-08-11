# Write a Python program to check whether a string is numeric

str = 'a123'
try:
    i = float(str)
except (ValueError, TypeError):
    print('\n Not Numeric')
print()
