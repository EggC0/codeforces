n = int(input())


m_100 = n // 100
n %= 100
m_20 = n // 20
n %= 20
m_10 = n // 10
n %= 10
m_5 = n // 5
n %= 5
m_1 = n // 1
n %= 1

print(m_100 + m_20 + m_10 + m_5 + m_1)
