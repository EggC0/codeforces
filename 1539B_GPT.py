def calculate_lengths(n, q, s, queries):
    # Создаем массив repeat_count
    repeat_count = [i + 1 for i in range(26)]

    # Создаем массив prefix_sum
    prefix_sum = [0] * (n + 1)

    # Заполняем prefix_sum
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + repeat_count[ord(s[i - 1]) - ord('a')]

    # Обрабатываем запросы
    results = []
    for l, r in queries:
        length = prefix_sum[r] - prefix_sum[l - 1]
        results.append(length)

    return results


# Входные данные
n, q = map(int, input().split())
s = input().strip()
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Вычисление и вывод результатов
results = calculate_lengths(n, q, s, queries)
for result in results:
    print(result)