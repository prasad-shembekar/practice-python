def list_count(lst, n):
    count = 0
    for i in lst:
        if i == n:
            count += 1
    return count


lst = list(map(int, input().split()))
n = int(input("Enter number want to count"))
print(list_count(lst, n))
