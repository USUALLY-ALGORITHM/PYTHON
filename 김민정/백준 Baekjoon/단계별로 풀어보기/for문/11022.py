# A + B - 8 (https://www.acmicpc.net/problem/11022)

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print("Case #%d: %d + %d = %d" %(i + 1, A, B, A + B))