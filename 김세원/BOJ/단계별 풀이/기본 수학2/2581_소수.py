m = int(input())
n = int(input())
arr = []

for i in range(m, n+1):
    cnt = 0
    if i == 1:
        continue

    for j in range(2, i+1):
        if i%j == 0:
            cnt += 1

    if cnt == 1:
        arr.append(i)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))
