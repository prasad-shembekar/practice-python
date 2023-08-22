s = input("Input a string;")
d = l =0
for c in s:
    if c.isdigit():
        d = d+1
    elif c.isalpha():
        l+=1
    else:
        pass
print(f'letters{l} and digit{d}')