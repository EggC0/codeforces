n = int(input())
for i in range(1, n):
    if i % 2 == 0 and (n - i) % 2 == 0 and (n - i) != 0:
        print("YES")
        break
else:
    print("NO")
