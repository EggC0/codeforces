for _ in range(int(input())):
    n = int(input())
    m = 3
    if 100 > n > 3:
        while m <= n//2:
            if n % m == 0:
                print("YES")
                break
            m += 2
        else:
            if n % 2 == 1:
                print("YES")
            else:
                print("NO")
    elif n <= 3:
        if n == 3:
            print("YES")
        else:
            print("NO")
    else:
        if n % 2 == 0:
            print("NO")
        else:
            print("YES")