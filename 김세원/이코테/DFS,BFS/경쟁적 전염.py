from collections import deque

n, k = map(int, input().split())
test = [] # 전체 맵 정보 담는 리스트
data =[] # 바이러스 정보를 담는 리스트
for i in range(n):
    test.append(list(map(int, input().split())))
    for j in range(n):
        if test[i][j] != 0:
            # 바이러스 숫자, x위치, y위치, 시간 을 입력받는다.
            data.append((test[i][j], i, j, 0))

rs, rx, ry = map(int, input().split())
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

data.sort()
q = deque(data)

while q:
    virus, x, y, time = q.popleft()
    if time == rs:
        break
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < n and 0 <= my < n:
            if test[mx][my] == 0:
                test[mx][my] = virus
                q.append((virus, mx, my, time+1))

print(test[rx-1][ry-1])
