"""
NxM 크기의 얼음 틀이 있다.
구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1
구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는것
생성되는 총 아이스크림 개수 ??

4 5
00110
00011
11111
00000

"""


n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))


# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드 방문
def dfs(x, y):
    # 주어진 범위를 봇어나는 경우 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상하좌우 위치 모두 재귀적 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


# 모든 노드에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)
