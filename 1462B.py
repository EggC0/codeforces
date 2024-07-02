for c in range(int(input())):
    n = int(input())
    s = input()
    if s == "2020":
        print(c, s, "YES")
    elif s[0] == "2" and s[-2] + s[-1] == "20":
        if "0" in s[1:-1] and "2" in s[1:-1]:
            print(c, s, "YES")
        '''elif s[:2] == "20" and s[-2:] == "20":
            print("YES")'''
    else:
        print(c, s, "NO")
