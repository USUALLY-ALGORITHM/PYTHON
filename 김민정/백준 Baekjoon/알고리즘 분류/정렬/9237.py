# 이장님 초대 (https://www.acmicpc.net/problem/9237)

n = int(input())
tree = list(map(int, input().split()))
tree.sort(reverse=True)

sum, max = 0, 0
index = 1

for i in tree:
    sum = i + index
    if max < sum:
        max = sum
    index += 1
print(max + 1)

"""
for i in range(len(tree))
    tree[i] = tree[i] + i + 1
print(max(tree) + 1)
"""
