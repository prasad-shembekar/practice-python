def string_lowe_upper_count(s):
    d = {"UPPER CASE":0,"LOWER_CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    print("Original String:",s)
    print("No. of upper case letters: ",d["UPPER CASE"])
    print("No. of lower case letters: ",d["LOWER_CASE"])

string_lowe_upper_count('The quick Brown Fox')