
print("Input")
num = list(input())
print(int("".join(sorted(num,reverse=True))) - int("".join(sorted(num))))