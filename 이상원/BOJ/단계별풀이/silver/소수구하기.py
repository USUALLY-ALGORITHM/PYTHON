"""
https://www.acmicpc.net/problem/1929

https://sso-feeling.tistory.com/387
"""
x, y = map(int, input().split())

for i in range(x, y + 1):
    if i == 1:  # 1은 소수가 아뉘지!
        continue
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i)
