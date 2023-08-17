# Write a Python program to create a string with no duplicate consecutive letters from a given string.

def no_consecutive(txt):
    return txt[0] + ''.join(txt[i] for i in range(1,len(txt)) if txt[i]!=txt[i-1])

print(no_consecutive("PPYYTTHHOONN"))