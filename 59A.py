s = input()

is_lower = [1 for i in s if i.islower()]
is_upper = [1 for i in s if i.isupper()]

if sum(is_lower) >= sum(is_upper):
    print(s.lower())
else:
    print(s.upper())
