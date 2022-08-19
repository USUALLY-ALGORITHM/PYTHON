n = int(input())
white_board = [[0] * 100 for _ in range(100)]

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            white_board[i][j] = 1

cnt = 0
for i in white_board:
    cnt += i.count(1)

print(cnt)

# https://corin-e.tistory.com/m/entry/%EB%B0%B1%EC%A4%80-2563-%EC%83%89%EC%A2%85%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC