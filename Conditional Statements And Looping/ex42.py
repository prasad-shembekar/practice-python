print("Input integer to calculate their sum and average:")

count  = 0
sum = 0.0
number = 1

while number != 0:
    number = int(input(""))
    sum += number
    count += 1

if count == 0:
    print("Input some numbers")
else:
    print("Average and sum of the above numbers are:",sum/count(count-1),sum)