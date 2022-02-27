# 직각삼각형 (https://www.acmicpc.net/problem/4153)

while True:
    data = list(map(int, input().split()))
    if sum(data) == 0:
        break
    data.sort(reverse=True)
    if data[0] ** 2 == data[1] ** 2 + data[2] ** 2:
        print('right')
    else:
        print('wrong')