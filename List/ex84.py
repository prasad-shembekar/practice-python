nums = [22,4,16,9,11]
numbers = list(map(round,nums))
numbers=list(set(numbers))
numbers = (sorted(map(lambda n:n*5,numbers)))
print(numbers)