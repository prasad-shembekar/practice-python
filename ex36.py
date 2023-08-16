def round(n):
    if n% 1000:
        return (1+n//1000)*1000
    else:
        return n
    
def compute(n):
    if n==0: return 100000
    return int(round(compute(n-1)*1.05))

print("Input number of months:")
result = compute(int(input()))
print("Amount of debt: ","$"+str(result).strip())