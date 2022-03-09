# 체스판 다시 칠하기 (https://sejong.webex.com/sejong/j.php?MTID=m27efce6982529c1cd6048e084b5fada4)

N , M = map(int, input().split())
board = []
result = []

for _ in range(N):
    board.append(input())

for a in range(N - 7):
    for b in range(M - 7):
        index1, index2 = 0, 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if board[i][j] != 'W':
                        index1 += 1
                    if board[i][j] != 'B':
                        index2 += 1
                else:
                    if board[i][j] != 'B':
                        index1 += 1
                    if board[i][j] != 'W':
                        index2 += 1
        result.append(min(index1, index2))
print(min(result))