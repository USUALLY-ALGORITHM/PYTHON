# 영화감독 슘 (https://www.acmicpc.net/problem/1436)

N = int(input())
nth = 666
count = 0

while True:
    if '666' in str(nth):
        count += 1
    if count == N:
        print(nth)
        break
    nth += 1