n = int(input())
d = sorted(list(map(int, input().split())), reverse=True)

c = 1

summ = 0

for i in range(len(d)):
    summ += d[i]
    if i+1 >= len(d):
        d_summ = 0
    else:
        d_summ = sum(d[i+1:])
    if summ > d_summ:
        print(c)
        break
    else:
        c += 1

