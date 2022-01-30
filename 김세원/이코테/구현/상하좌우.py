# N 입력받기
n = int(input())
x, y = 1, 1
plan = input().split()

dx = {'L':0, 'R':0, 'U':-1, 'D':1}
dy = {'L':-1, 'R':1, 'U':0, 'D':0}

for i in plan:
    nx = x + dx[i]
    ny = y + dy[i]
    
    #공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    x, y = nx, ny
    
print(x, y)
