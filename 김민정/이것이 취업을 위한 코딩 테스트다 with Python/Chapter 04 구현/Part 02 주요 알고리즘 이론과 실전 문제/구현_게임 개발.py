N , M = map(int, input().split())
x, y, direction = map(int, input().split())

array = []
for i in range(N):
    array.append(list(map(int, input().split())))

map_array = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

map_array[x][y] = 1
count = 1
turned_count = 0

while True:
    direction -= 1
    if direction == -1:
        direction = 3

    nx = x + dx[direction]
    ny = y + dy[direction]

    if array[nx][ny] == 0 and map_array[nx][ny] == 0:
        map_array[nx][ny] = 1
        count += 1
        x, y = nx, ny
        turned_count = 0
        continue
    else:
        turned_count += 1

    if turned_count == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

    if array[nx][ny] == 0:
        x, y = nx, ny
    else:
        break
    turned_count = 0

print(count)
