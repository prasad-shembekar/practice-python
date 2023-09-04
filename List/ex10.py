def long_word(n,str):
    word_len = []
    txt = str.split(" ")

    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len

print(long_word(3,"The quick brown fox jumps"))