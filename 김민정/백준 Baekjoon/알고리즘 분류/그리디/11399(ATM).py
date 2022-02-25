# ATM (https://www.acmicpc.net/problem/11399)

N = int(input())
sum, result = 0, 0

P = list(map(int, input().split()))
P. sort()  # 인출 시간이 적은 사람이 앞으로 오도록 오름차순 정렬

for time in range(N):
    sum += P[time]
    result += sum

print(result)