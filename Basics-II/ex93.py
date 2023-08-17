def middle_char(txt):
  return txt[(len(txt)-1)//2:(len(txt)+2)//2]
text = "Python"
print("Original string: ",text)
print("Middle character(s) of the said string: ",middle_char(text))