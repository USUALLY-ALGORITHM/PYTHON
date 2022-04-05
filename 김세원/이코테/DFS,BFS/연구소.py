import sys
from collections import deque
from itertools import combinations
import copy

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 0(빈공간), 1(벽), 2(바이러스)


def bfs(x, y, graph):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))


array = []
countArray = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            array.append((i, j))

combiArray = list(combinations(array, 3))
for case in combiArray:
    count = 0
    tempGraph = copy.deepcopy(graph)
    # 새로운 벽 1로 표시
    for node in case:
        tempGraph[node[0]][node[1]] = 1
    # 바이러스 bfs탐색하면서
    for i in range(n):
        for j in range(m):
            if tempGraph[i][j] == 2:
                bfs(i, j, tempGraph)

    for i in range(n):
        for j in range(m):
            if tempGraph[i][j] == 0:
                count += 1

    countArray.append(count)


print(max(countArray))
