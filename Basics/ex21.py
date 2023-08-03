# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.

n = int(input("Enter Number"))
mod = n % 2
if mod > 0:
    print("Odd Number")
else:
    print("Even Number")
