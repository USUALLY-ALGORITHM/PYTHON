n, l = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
start = 0
cnt = 0

for i in data:
    if start < i:
        cnt += 1
        start = i + l -1

print(cnt)
