N = int(input())

X = list(map(int, input().split()))
X.sort()

group = list()
group_count = 0

for i in X:
    group.append(i)
    if len(group) == i:
        group_count += 1
        group.clear()
    else:
        continue

print(group_count)