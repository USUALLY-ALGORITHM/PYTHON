n, m, k, x = map(int, input().split())
 
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [0] * (n + 1)
 
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
 
from collections import deque
 
def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = True
 
    while q:
        cur = q.popleft()
 
        for n in graph[cur]:
            if not visited[n]:
                visited[n] = True
                q.append(n)
                distance[n] = distance[cur] + 1
    
bfs(x)
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
 
if not check: 
    print(-1)
