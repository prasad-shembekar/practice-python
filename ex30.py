# Write a Python program to reverse the digits of a given number and add them to the original. Repeat this procedure if the sum is not a palindrome.

def rev_number(n):
    s = 0
    while True:
        k = str(n)
        if k == k[::-1]:
            break
        else:
            m = int(k[::-1])
            n += m
            s += 1
        return n
    
print(rev_number(1234))