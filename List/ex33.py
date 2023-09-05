from itertools import combinations

def sub_lists(my_list):
    subs = []
    for i in range(0,len(my_list)+1):
        temp = [list(x) for x in combinations(my_list,i)]
        if len(temp) > 0:
            subs.extend(temp)
    return subs

l1 = [10,20,30,40]
l2 = ['X','Y','Z']
print(sub_lists(l1))