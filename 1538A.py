import math


for _ in range(int(input())):
    n = int(input())
    data = [int(i) for i in input().split()]
    numbers = []
    for ai in range(len(data)):
        if len(data) % 2:
            numbers.append(abs(abs(math.floor(len(data)/2) - ai)-math.floor(len(data)/2)) + 1)
        else:
            if ai < len(data)//2:
                numbers.append(ai + 1)
            elif ai >= len(data)//2:
                numbers.append(len(data)//2 - (ai - len(data)//2))


    i_max = data.index(max(data))
    i_min = data.index(min(data))

    if (i_max < len(data)/2 and i_min < len(data)/2) or (i_max >= math.floor(len(data)/2) and i_min >= math.floor(len(data)/2)):
        print(max(numbers[i_max], numbers[i_min]))
    elif numbers[i_max] == numbers[i_min] and numbers[i_min] == max(numbers):
        print(max(numbers) + 1)
    else:
        r1 = numbers[i_max] + numbers[i_min]
        r2 = abs(i_min - i_max) + min(numbers[i_max], numbers[i_min])
        print(min(r1, r2))


