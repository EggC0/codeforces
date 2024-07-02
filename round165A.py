from itertools import permutations

for _ in range(int(input())):
    n = int(input())
    ll = list(map(lambda x: [x, False, False], map(int, input().split())))
    mn = 100
    li = []
    for j in range(1, n+1):
        li.append(j)

        for i in range(n):
            if i in li:
                ll[i][1] = True

        for i in range(n):
            if ll[i][1]:
                if ll[ll[i][0]-1][1]:
                    ll[i][2] = True
        if
    print(ll)


