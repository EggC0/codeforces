s = input()

c = 1
i_0 = ""

for i in s:
    if i == i_0:
        c += 1
        if c == 7:
            print("YES")
            break
    else:
        c = 1
    i_0 = i

else:
    print("NO")
