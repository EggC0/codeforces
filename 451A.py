n, m = map(int, input().split())

c = 0

while n > 0 and m > 0:
    c += 1
    n -= 1
    m -= 1

print(("Akshat", "Malvika")[c % 2 == 0])
