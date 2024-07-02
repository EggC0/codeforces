c = 0
for _ in range(int(input())):
    s = input().split(" ")
    if sum(map(int, s)) >= 2:
        c += 1

print(c)