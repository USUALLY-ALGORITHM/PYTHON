import sys


inputs = sys.stdin.readline

n = int(inputs())

arr = []
cnt = 0
table = [[0 for i in range(101)] for j in range(101)]
for item in range(n):
    startY, startX = map(int, inputs().split())

    for item in range(startY, startY + 10):
        for j in range(startX, startX+10):
            if table[item][j] == 1:
                continue
            table[item][j] = 1
            cnt += 1

print(cnt)
