"""
https://www.acmicpc.net/problem/2839

"""

n = int(input())

bucket = [5, 3]
answer = 0
for i in bucket:
    cnt = n // i
    n -= cnt * i
    answer += cnt
if answer != 0:
    print(-1)
else:
    print(answer)
