def test(N):
    result = []
    for i in range(N):
        result.append([N]*N)
    return result

N = int(input())
print(test(N))


