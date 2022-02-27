# 날짜 계산 (https://www.acmicpc.net/problem/1476)

M, S, E = map(int, input().split())
year = 1

while True:
    if (year - M) % 15 == 0 and (year - S) % 28 == 0 and (year - E) % 19 == 0:
        break
    year += 1

print(year)