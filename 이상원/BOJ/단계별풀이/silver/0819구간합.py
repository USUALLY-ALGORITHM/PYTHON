import sys


inputs = sys.stdin.readline
N, M = map(int, inputs().split())
arr = list(map(int, inputs().split()))

dp = [0 for i in range(N+1)]

for item in range(1, len(arr) + 1):
    dp[item] += dp[item-1] + arr[item - 1]

for item in range(M):
    a, b = map(int, inputs().split())
    print(dp[b] - dp[a-1])
