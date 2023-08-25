def recursive_facto(n):
    if n <=1:
        return 1
    else:
        return n * (recursive_facto(n-1))
    
print(recursive_facto(5))