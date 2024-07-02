for _ in range(int(input())):
    n, m = map(int, input().split())
    data = []
    for _ in range(n):
        data.append(input())
    new_data = []
    for i in range(m):
        new_data.append([data[j][i] for j in range(n)])
    v, i, k, a = (False, False, False, False)
    for el in new_data:
        if "v" in el and not v:
            v = True
        elif "i" in el and v and not i:
            i = True
        elif "k" in el and v and i and not k:
            k = True
        elif "a" in el and v and i and k:
            a = True
        if v and i and k and a:
            print("YES")
            break
        # print(el, v, i, k, a)
    else:
        print("NO")