# 최댓값 (https://www.acmicpc.net/problem/2562)

m = []
max, max_i = 0, 0

for i in range (9):
    n = int(input())
    m.append(n)
    if m[i] > max:
        max = m[i]
        max_i = i

print(max)
print(max_i + 1)

"""
for i in range (9):
    m.append(int(input())
print(max(m))
print(m.index(max(a)) + 1)
"""