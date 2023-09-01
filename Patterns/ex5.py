#  print inverted pyaramid
# *_*_*_*
#  *_*_*
# __*_*__
# ___*__

num = int(input("Enter numberof rows:"))
for i in range(num,0,-1):
    for j in range(0,num-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
