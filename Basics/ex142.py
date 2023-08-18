# Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of same length in a given string. Return True/False. 

def test(str):
    while '01' in str:
        str = str.replace('01','')
    return len(str) == 0

str = "0101010101"
print(test(str))

