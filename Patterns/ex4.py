# Print pyramid
# ___*___
# __*_*__
# _*_*_*_
# *_*_*_*

num = int(input("Enter number of rows:"))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end="")
    print()

num = int(input("Enter number of rows:"))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,2*i+1):
        print("*",end="")
    print()

def pyramid(rows):
    for i in range(rows):
        print(''*(rows-i-1)+'*'(i+1))
