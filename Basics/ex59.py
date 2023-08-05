# Write a Python program to convert height (in feet and inches) to centimeters.

feet = int(input("Enter feet"))
inches = int(input("Enter inches"))

inches += feet * 12
cm = round(inches * 2.54, 1)
print("Height is: %d cm" % cm)
