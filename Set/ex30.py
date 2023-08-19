def remove_duplicates(strings):
    return list(set(strings))


strs = ['foo', 'bar', 'abc', 'foo', 'qux', 'bar', 'baz']
print("Original list of strings:")
print(strs);
print("strs of strings after removing duplicates:")
print(remove_duplicates(strs))
strs = ["Python","Exercises","Practice","Solution","Exercises"] 
print("\nOriginal list of strings:")
print(strs);
print("List of strings after removing duplicates:")
print(remove_duplicates(strs))
