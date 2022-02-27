# 제로 (https://www.acmicpc.net/problem/10773)

K = int(input())
result = []

for i in range(K):
    num = int(input())
    if num == 0:
        result.pop()
    else:
        result.append(num)

print(sum(result))