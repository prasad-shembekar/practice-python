from copy import deepcopy

tuplex = ("Hello",5,[],True)
tuple_copy  = deepcopy(tuplex)
tuple_copy[2].append(50)
