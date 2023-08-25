def recurgcd(a,b):
    low = min(a,b)
    high= max(a,b)

    if low == 0:
        return high
    elif low ==1:
        return 1
    else:
        return recurgcd(low,high%low)
    
print(recurgcd(12,14))