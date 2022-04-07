"""
3 10
1 2 3 4 5 6 7 8 9 10
"""
import sys


inputs = sys.stdin.readline

m, n = map(int, inputs().split())
snacks = list(map(int, inputs().split()))

start = 0
end = max(snacks)
print(f"end: {end}")

result = 0
snacks.sort(reverse=True)  # sort를 하니까 더 오래걸렸음 ... n log n 이라서 그런듯

while start <= end:
    print('---single step---')
    total = 0
    mid = (start + end) // 2
    print(f'start: {start}  mid {mid}  end: {end}')
    if mid == 0:
        break

    for snack in snacks:  # sort 안했을 땐 k*n 만큼의 시간이 걸림 (n이 클 수록 k*n < n*logn)
        if snack >= mid:
            total += snack // mid
        else:
            break

    if total >= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
