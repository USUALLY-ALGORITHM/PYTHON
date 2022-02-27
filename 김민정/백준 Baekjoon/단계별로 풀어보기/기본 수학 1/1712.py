# 손익분기점 (https://www.acmicpc.net/problem/1712)

A, B, C = map(int, input().split())
num = 1

if B >= C:
    print(-1)

else:
    print(A // (C - B) + 1)