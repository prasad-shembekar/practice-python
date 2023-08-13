# Write a Python program that inputs a number and generates an error message if it is not a number.

while True:
    try:
        a = int(input("Enter number:"))
        break
    except ValueError:
        print("\n This in not a number")