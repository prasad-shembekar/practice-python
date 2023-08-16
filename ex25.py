# Write a Python program to find the digits that are missing from a given mobile number.

def absent(n):
    all = [0,1,2,3,4,5,6,7,8,9]
    n = set([int(i) for i in n])
    n = n.symmetric_difference(all)
    n = sorted(n)
    return n 

print(absent([9,8,3,2,2,0,9,7,6,3]))