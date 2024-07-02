n = int(input())
data = [int(i) for i in input().split()]
mx = 0
c = 1
if n > 1:
    for i in range(len(data)-1):
        if data[i] < data[i+1]:
            c += 1
            mx = max(mx, c)
        else:
            mx = max(mx, c)
            c = 1
    print(mx)

else:
    print(1)
