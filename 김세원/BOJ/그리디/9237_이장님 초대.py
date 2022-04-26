n = int(input())
a = list(map(int, input().split()))
# arr = []
# arr.append(input().split())
max = 0
a.sort(reverse=True)

cnt = 1
total = 0
for i in a:
    total = i + cnt
    cnt += 1

    if total > max:
        max = total

print(max+1)
