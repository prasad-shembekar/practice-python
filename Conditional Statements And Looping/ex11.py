row = int(input("Enter rows"))
col = int(input("Enter col"))
mult_list = [[0 for col in range(col)] for row in range(row)] 

for r in range(row):
    for c in range(col):
        mult_list[r][c] = r*c

print(mult_list)