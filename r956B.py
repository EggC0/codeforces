for i in range(int(input())):
    s = input()
    if len(set(s)) != 1:
        print("YES")
        sl = [i for i in s]
        for j in range(len(s)):
            if s[0] != s[j]:

                sl[j] = s[0]
                sl[0] = s[j]

                break

        print("".join(sl))

    else:
        print("NO")
