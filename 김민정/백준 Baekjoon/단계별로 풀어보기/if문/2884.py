# 알람 시계 (https://www.acmicpc.net/problem/2884)

H, M = map(int, input().split())

M -= 45
if M < 0:
    M = M + 60
    H -= 1

if H < 0:
    H += 24

print(H, M)