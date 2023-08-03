# Write a Python program to find the least common multiple (LCM) of two positive integers.

def lcm(a,b):
    if a > b:
        z = a
    else:
        z = b

    while(True):
        if((z%a == 0) and (z%b == 0)):
            lcm = z
            break
        z += 1
    return lcm 

a = int(input())
b = int(input())
print(lcm(a,b))
