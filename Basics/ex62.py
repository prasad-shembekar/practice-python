# Write a Python program to convert all units of time into seconds.

days = int(input("Enter days: ")) * 3600 * 24
hours = int(input("Enter hours: ")) * 3600
minutes = int(input("Enter minutes: ")) * 60
seconds = int(input("ENter seconds: "))

time = days+hours+minutes+seconds

print("Amount of seconds", time)
