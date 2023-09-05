from itertools import zip_longest,chain,tee
def replace(lst):
    lst1,lst2 = tee(iter(lst),2)
    return list(chain.from_iterable(zip_longest(lst1[1::2],lst2[::2])))

n = [0,1,2,3,4,5]
print(replace(n))