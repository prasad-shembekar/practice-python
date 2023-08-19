def tuple_int(tuple_str):
    result = tuple((int(x[0]), int(x[1])) for x in tuple_str)
    return result 

print(tuple_int((('333','33'),('1416','55'))))
