def is_narcissistic_num(num):
	return num == sum([int(x) ** len(str(num)) for x in str(num)])

print(is_narcissistic_num(153))