from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# 모든 도로 정보 입력받기
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    # 예제의 경우 [[], [2, 3], [3, 4], [], []]와 같이 인접노드를 포함한 graph 생성

# 모든 도시에 대한 거리 초기화
distance = [-1] * (N + 1) # 방문하지 않은 도시는 -1
distance[X] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([X])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 이는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            # 현재 도시와 출발 도시 사이의 거리 + 1
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 도든 도시의 번호를 오름차순으로 출력
# 출발 도시로부타 최단 거리가 K인 도시가 없다면 -1을 출력하기 위해 False 초기화
check = False
for i in range(1, N + 1):
    # 도시들 간의 최단 거리를 확인하여 K와 동일하면 그 도시를 출력
    if distance[i] == K:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)