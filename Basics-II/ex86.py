# Write a Python program to count the number of equal numbers from three given integers.

def test(x,y,z):
    result = set([x,y,z])
    if len(result) == 3:
        return 0 
    else:
        return (4 - len(result))
    
print(test(1,1,1))