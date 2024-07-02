n = int(input())
c = 0
m = 0
while m != n:
    for i in range(5, 0, -1):
        if (n - m) >= i:
            m += i
            c += 1
            break

print(c)
