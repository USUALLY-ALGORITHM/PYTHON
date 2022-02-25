# 숫자 빈도수 (https://www.acmicpc.net/problem/14912)

n, d = map(int, input().split())

sum = 0
for i in range(1, n + 1):
    sum += str(i).count(str(d))
print(sum)
