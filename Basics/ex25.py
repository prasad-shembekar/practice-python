# Write a Python program to test whether a passed letter is a vowel or not.


# lst = ["a","e","i","o","u"]
# char = input("Enter Character").lower()

# if char in lst:
#     print("True")
# else:
#     print("False")

def is_vowel(char):
    all_vowel = 'aeiou'
    return char in all_vowel


print(is_vowel("C"))
