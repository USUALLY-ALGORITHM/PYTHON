# 인접 행렬
INF = 987654321

graph = [[0, 7, 5], [7, 0, INF], [5, INF, 0]]

# 인접 리스트
lst = [[] for _ in range(3)]
print(lst)

# 노드 0에 연결된 노드 정보 저장 (노드, 거리)
lst[0].append((1, 7))
lst[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장
lst[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장
lst[2].append((0, 5))

print(lst)
