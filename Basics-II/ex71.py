def reverse_vowel(str1):
    vowels = ""
    for char in str1:
        if char in "aeiouAEIOU":
            vowels += char
    result = ""

    for char in str1:
        if char in "aeiouAEIOU":
            result += vowels[-1]
            vowels = vowels[:-1]
        else:
            result += char
    return result

print(reverse_vowel("Hello Prasad"))