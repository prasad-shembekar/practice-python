# Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure. 


kpa = float(input("Input pressure value:"))
psi = kpa / 6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa / 101.325
print("Pressure in pounds per square inch: %.2f psi" %(psi))
print("Pressure in mmhg: %.2f" %(mmhg))
print("Pressure in %.2f atm" %(atm))
