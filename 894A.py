s = input()

qi = []
ai = []
res = 0
for index in range(len(s)):
    if s[index] == "Q":
        qi.append(index)
    if s[index] == "A":
        ai.append(index)

for a in ai:
    res += s[:a].count("Q")*s[a:].count("Q")
print(res)
