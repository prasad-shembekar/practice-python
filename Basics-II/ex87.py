def is_valid(emp_code):
    return len(emp_code) in [8,12] and emp_code.isdigit()

print(is_valid('123455544321'))