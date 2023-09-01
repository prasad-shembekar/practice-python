# Print pattern of right angle triangle
# *
# **
# ***
# ****
# *****

# Algorithm
# take input no of rows
# for loop rows and column
# range(1,11) here it will print 0 to 10 where 11 is excluded
# understand print("Hello");print("Hii")
# hello
# hi
# understand print("hello",end=" ");print("Hii")
# hello hi

num = int(input("ENter number of rows: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


