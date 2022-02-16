"""
NxM 크기의 직사각형 형태의 미로에 갇혀있다 
시작 위치는 1,1
한번에 한 칸씩 움직일 수 있다 
탈출하기 위해 움직여야 하는 최소의 움직임 
시작 칸과 마지막 칸 모두 센다 
괴물이 있는 부분은 0 없는 부분은 1 
BFS를 사용하면 좋다 가까운 노드부터 탐색하기 때문 

5 6
101010
111111
000001
111111
111111

"""

from collections import deque


n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상 하 좌 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs
def bfs(x, y):
    # 큐 구현을 위해 deque 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어날 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 겨우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]


print(bfs(0, 0))
