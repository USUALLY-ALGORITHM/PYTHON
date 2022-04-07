"""https://www.acmicpc.net/problem/9237
"""

n = int(input())
lst = list(map(int, input().split()))

lst.sort(reverse=True)
day = 0
for i in range(1, n + 1):
    now = i + lst[i - 1]
    if day < now:
        day = now

print(day + 1)
