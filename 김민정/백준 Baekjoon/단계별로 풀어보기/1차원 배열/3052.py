# 나머지 (https://www.acmicpc.net/problem/3052)

m = []
for i in range(10):
    n = int(input())
    n %= 42
    m.append(n)

m = set(m) # set : 리스트를 집합으로 변환시켜, 중복된 값을 제거
print(len(m))