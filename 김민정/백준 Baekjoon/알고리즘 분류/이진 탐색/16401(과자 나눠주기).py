# 과자 나눠주기 (https://www.acmicpc.net/problem/16401)

M, N = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    # 모든 조카에게 같은 길이의 막대과자를 나눠줄 수 없을 때
    if mid == 0:
        total = 0
        break

    for x in array:
        if x >= mid:
            total += (x // mid)

    if total >= M:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)