t = int(input())


def check(l):
    return ((not (l.count(1) % 2)) and (not (l.count(2) % 2))) or ((l.count(2) % 2) and (not (l.count(1) % 2)) and l.count(1) > 0)


for _ in range(t):
    n = int(input())
    is_ok = check([int(i) for i in input().split()])
    if is_ok:
        print("YES")
    else:
        print("NO")
