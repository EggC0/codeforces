n, k = map(int, input().split())

b = list(map(int, input().split()))

ball = b[k-1]

print(sum([1 for i in b if i >= ball and i != 0]))
