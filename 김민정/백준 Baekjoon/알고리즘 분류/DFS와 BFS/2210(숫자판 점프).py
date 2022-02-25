# 숫자판 점프 (https://www.acmicpc.net/problem/2210)

board = [list(input().split()) for _ in range(5)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, num):
  if len(num) == 6:
    if num not in result: # 6자리의 수가 중복이 아닌 경우
      result.append(num)
    return

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
      continue
    else:
      dfs(nx, ny, num + board[nx][ny])

result = []
for i in range(5):
  for j in range(5):
    dfs(i, j, board[i][j])
print(len(result))