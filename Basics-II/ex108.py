def check_last_digit(x, y, z):
  return str(x+z)[-1] == str(y)[-1]
print(check_last_digit(12, 26, 44))
print(check_last_digit(145, 122, 1010))
print(check_last_digit(0, 20, 40))
print(check_last_digit(1, 22, 40))
print(check_last_digit(145, 129, 104))
