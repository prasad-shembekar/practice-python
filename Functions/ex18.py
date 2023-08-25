mycode = 'print("Hello World")'
code = """
def multiply(x,y):
    return x*y

print('Multiple of 2 and 3 is:',multiply(2,3))
"""

exec(mycode)
exec(code)