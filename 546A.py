k, n, w = map(int, input().split())

summ = 0
for i in range(1, w+1):
    summ += k*i

if summ - n <= 0:
    print(0)
else:
    print(summ-n)