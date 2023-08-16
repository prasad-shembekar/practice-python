def findTrailingZero(n):
    count = 0
    i = 5

    while(n / i >= 1):
        count+= int(n/i)
    return int(count)

n = 100
print("Count factorial is",findTrailingZero(n))