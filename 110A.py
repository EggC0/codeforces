n = input()

if set(str(n.count("4") + n.count("7"))).issubset(set("47")):
    print("YES")
else:
    print("NO")
