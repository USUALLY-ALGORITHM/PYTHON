# 소트인사이드 (https://www.acmicpc.net/problem/1427)

N = int(input())
array = list(map(int, str(N)))

array.sort(reverse=True)

for i in array:
    print(i, end='')