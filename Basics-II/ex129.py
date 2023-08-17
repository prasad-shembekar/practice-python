def test(text):
    return [x for x in range(len(text)) if text[x].islower()]

print(test("pyThON"))