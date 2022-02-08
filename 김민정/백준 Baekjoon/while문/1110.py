# 더하기 사이클 (https://www.acmicpc.net/problem/1110)

N = int(input())
temp = N

count = 0
while True:
    sum = (temp // 10) + (temp % 10)
    new = ((temp % 10) * 10) + (sum % 10)
    count += 1

    if new == N:
        break
    temp = new
print(count)