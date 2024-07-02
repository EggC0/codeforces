s = input()

if all([(i not in s) for i in ["H", "Q", "9"]]):
    print("NO")
else:
    print("YES")
