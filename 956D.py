for i in range(int(input())):
    s = input()
    patt = list(map(str, sorted([int(i) for i in s])))
    c = 0
    for j in range(len(patt)):
        if s[j] != patt[j]:
            c += 1
    print(c // 2 + 1)
