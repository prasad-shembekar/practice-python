def pascal_triangle(n):
    throw = [1]
    y = [0]
    for x in range(max(n,0)):
        print(throw)
        throw=[l+r for l,r in zip(throw+y,y+throw)]
    return n >= 1

pascal_triangle(6)
