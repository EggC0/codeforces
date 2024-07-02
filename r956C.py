for i in range(int(input())):
    a, b, c, d = map(int, input().split())
    if (a in range(min(c, d), max(c, d)+1) and b in range(min(c, d), max(c, d)+1)) or (a not in range(min(c, d), max(c, d)+1) and b not in range(min(c, d), max(c, d)+1)):
        print("NO")
    else:
        print("YES")
