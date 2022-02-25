# 숫자의 개수 (https://www.acmicpc.net/problem/2577)

A = int(input())
B = int(input())
C = int(input())

result = list(str(A * B * C)) # [1, 7, 0, 3, 7, 3, 0, 0]

for i in range(10):
    print(result.count(str(i)))