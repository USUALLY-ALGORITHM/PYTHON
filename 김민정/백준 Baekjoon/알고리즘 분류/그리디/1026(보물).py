# 보물 (https://www.acmicpc.net/problem/1026)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0
for i in range(N):
    result += min(A) * max(B)
    A.pop(A.index(min(A))) # index : 인덱스 받기
    B.pop(B.index(max(B))) # pop : 배열 빼기

print(result)