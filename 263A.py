matrix = []
for _ in range(5):
    matrix.append(list(map(int, input().split())))

c = 0

for i in range(5):
    if sum(matrix[i]) == 1:
        matrix[2] = matrix[i]
        c += abs(2-i)
        break

for i in range(5):
    if matrix[2][i] == 1:
        matrix[2][2] = 1
        c += abs(2-i)
        break

print(c)