print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ").capitalize()

if month_name == "February":
    print("28/29 days in month")
elif month_name in ("April", "June", "September", "November"):
    print("30 days in month")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    print("31 days in month")
else:
    print("Wrong Month name")