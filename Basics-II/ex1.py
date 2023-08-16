#  Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other. 

def test(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False
    
print(test([1,5,5,7,9]))