def to_string(n,base):
    convert="0123456789ABCDEF"
    if n < base:
        return convert[n]
    else:
        return to_string(n//base,base) + convert[n % base]
    
print(to_string(2835,16))