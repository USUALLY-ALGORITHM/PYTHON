import sys
input=sys.stdin.readline

n , m = map(int, input().split())
arr = list(map(int, input().split()))
sum =0
pre = [0]

for i in range(n):
    sum += arr[i]
    pre.append(sum)

for i in range(m):
    a, b = map(int, input().split())
    print(pre[b]-pre[a-1])
