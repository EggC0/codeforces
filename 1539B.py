n, q = (int(i) for i in input().split())

s = input()

for _ in range(q):
    l, r = (int(i) for i in input().split())
    print(sum(s[l-1:r].encode())-96*(r-l+1))
    