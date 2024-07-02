def get_n(n):
    if n == 1:
        return 1
    else:
        r = (n-1)*4
        return r + get_n(n-1)


print(get_n(int(input())))
