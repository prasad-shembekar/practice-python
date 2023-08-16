# Write a Python program that generates a list of all possible permutations from a given collection of distinct numbers.

def permute(nums):
    result_perms = [[]]
    for n in nums:
        new_perms = []
        for perm in result_perms:
            for i in range(len(perm)+1):
                new_perms.append(perm[:i] + [n] + perm[i:])
                result_perms = new_perms
    return result_perms

my_nums = [1,2,3]
print("Original Collection:",my_nums)
print("Collection with distinct number:",permute(my_nums))

