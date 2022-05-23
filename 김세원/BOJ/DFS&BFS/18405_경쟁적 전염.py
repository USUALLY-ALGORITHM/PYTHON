from collections import deque

n,k = map(int,input().split())
graph = []
data = []

for _ in range(n):
    graph.append(list(map(int,input().split())))
s,x,y = map(int,input().split())

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            #바이러스 종류, 위치, 초
            data.append([graph[i][j],i,j,s])
#바이러스 종류가 낮은 수부터 증식
data.sort()

q = deque(data)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
#큐가 존재할때까지 
while q:
    virus_type,startx,starty,sec = q.popleft()
    #초가 0이되면 멈춤
    if sec <= 0:
        break
    #현재를 기준으로 상하좌우 0이면 감염
    for i in range(4):
        nx = startx + dx[i]
        ny = starty + dy[i]
        #범위 안에 있는 경우만
        if nx >=0 and nx<n and ny >= 0 and ny<n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus_type
                #감염된 노드 큐에 추가 하고 현재 초에서 1뺀다
                #1초 사이클을 모든 바이러스가 돌 동안 sec는 바뀌지 않는다
                q.append([graph[nx][ny],nx,ny,sec-1])
        
print(graph[x-1][y-1])
