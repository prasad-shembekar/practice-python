import random
def random_select(list,n):
    return random.sample(list,n)

list = [1,1,2,3,4,4,5,1]
result = random_select(list,3)
print(result)