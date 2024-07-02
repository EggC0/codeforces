for _ in range(int(input())):
    n, m, k = (int(i) for i in input().split())
    n0, m0, k0 = (1, 1, 0)
    while n0 != n:
        n0 += 1
        k0 += m0
    while m0 != m:
        m0 += 1
        k0 += n0
    if k == k0:
        print("YES")
    else:
        print("NO")