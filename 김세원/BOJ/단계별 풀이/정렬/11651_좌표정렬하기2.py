n = int(input())
num = []
for i in range(n):
    [a,b] = map(int, input().split())
    rev = [b, a]
    num.append(rev)

num = sorted(num)

for i in range(n):
    print(num[i][1], num[i][0])