n, m = map(int, input().split())

d = sorted(list(map(int, input().split())))

minn = float("inf")

for i in range(len(d)-n+1):
    numbers = d[i:i+n]
    minn = min(minn, max(numbers)-min(numbers))

print(minn)



