# Print inverted right angle triangle 
# ****
# ***
# **
# *

num = int(input("Enter rows: "))
for i in range(num+1,0,-1):
    for j in range(0,i-1):
        print("*",end=" ")
    print()
