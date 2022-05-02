n = int(input())
num = []
for i in range(n):
    [a, b] = map(int, input().split())
    num.append([a,b])

num = sorted(num)

for i in range(n):
    print(num[i][0],num[i][1])
