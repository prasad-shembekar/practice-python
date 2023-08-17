def prefix(str1):
    if not str1:
        return ""
    
    short_char = min(str1,key=len)

    for i,char in enumerate(short_char):
        for others in short_char:
            if others[i]!= char:
                return short_char[:i]

    return short_char

print(prefix(["abcdefg",'abcddfsfs']))

