input()
d = list(map(int, input().split()))

if len(d) == 1:
    print(1)
else:
    c = 0
    result = 0

    for i in range(len(d) - 1):
        if d[i] <= d[i + 1]:
            c += 1
        else:
            result = max(result, c + 1)
            c = 0
        if i == len(d) - 2:
            result = max(result, c + 1)

    print(result)
