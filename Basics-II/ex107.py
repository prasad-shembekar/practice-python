def oddish_evenish_num(n):
	return 'Oddish' if sum(map(int, str(n))) % 2 else 'Evenish'
n = 120
print("Original Number",n)
print("Check whether the sum of all digits of the said number is odd or even!")
print(oddish_evenish_num(120))