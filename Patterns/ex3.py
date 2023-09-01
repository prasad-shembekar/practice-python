# print inverted reversed right angle triangle
# ****
#  ***
#   **
#    *

row = int(input("Enter row number: "))
for i in range(1,row+1):
    for j in range(1,row+1):
        if(j<i):
            print(" ",end=" ")
        else:
            print("*",end=' ')
    print()