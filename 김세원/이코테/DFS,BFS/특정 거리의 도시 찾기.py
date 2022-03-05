from collections import deque

# 도시의 갯수, 도로의 갯수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 모든 도로 정보 입력받기
for _ in range(m) :
	a, b = map(int, input().split())
	graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0 #출발 도시까지의 거리는 0으로 설정

# 너비 우선탐색 BFS 수행
q = deque([x]) # queue 생성

while q :
	now = q.popleft()
	# 현재 도시에서 이동할 수 있는 모든 도시를 확인
	for next_node in graph[now] :
		if distance[next_node] == -1 : # 아직 방문하지 도시일때
			distance[next_node] = distance[now] + 1 # 최단 거리 갱신
			q.append(next_node) # queue에 집어넣기

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1) :
	if distance[i] == k  : # 최단거리 딱 K인 도시 발견
		print(i)
		check = True

# 하나도 없다면 -1 출력
if check == False :
	print(-1)
