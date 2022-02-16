"""
게임을 좋아하는 큐브러버는 체스에서 사용할 새로운 말 "데스 나이트"를 만들었다. 
데스 나이트가 있는 곳이 
(r, c)라면, (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), 
(r+2, c-1), (r+2, c+1)로 이동할 수 있다.

크기가 N×N인 체스판과 두 칸 (r1, c1), (r2, c2)가 주어진다. 
데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 구해보자. 체스판의 행과 열은 0번부터 시작한다.

데스 나이트는 체스판 밖으로 벗어날 수 없다.

## 입력
첫째 줄에 체스판의 크기 N(5 ≤ N ≤ 200)이 주어진다. 둘째 줄에 r1, c1, r2, c2가 주어진다.
## 출력
첫째 줄에 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 출력한다. 이동할 수 없는 경우에는 -1을 출력한다.

7
6 6 0 1

"""

from collections import deque


n = int(input())
chess = [[0] * n for _ in range(n)]
r1, c1, r2, c2 = list(map(int, input().split()))

nr = [-2, -2, 0, 0, 2, 2]
nc = [-1, 1, -2, 2, -1, 1]


def bfs(r, c):
    queue = deque()
    queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for i in range(len(nr)):
            rCheck = r + nr[i]
            cCheck = c + nc[i]

            # 체스판 밖이면 다음으로
            if rCheck < 0 or cCheck < 0 or rCheck >= n or cCheck >= n:
                continue
            if chess[rCheck][cCheck] == 0:
                chess[rCheck][cCheck] = chess[r][c] + 1
                queue.append((rCheck, cCheck))
    if chess[r2][c2] == 0:
        return -1
    else:
        return chess[r2][c2]


print(bfs(r1, c1))
