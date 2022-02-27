# 분수찾기 (https://www.acmicpc.net/problem/1193)

X = int(input())

line, end = 0, 0 # line : 대각선 라인, end : 마지막 인덱스 번호
while X > end:
    line += 1
    end += line

gap = end - X
if line % 2 == 0:
    top = line - gap
    bottom = gap + 1

else:
    top = gap + 1
    bottom = line - gap

print("%d/%d"%(top, bottom))