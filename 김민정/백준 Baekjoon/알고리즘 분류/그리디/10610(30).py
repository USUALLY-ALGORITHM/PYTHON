# 30 (https://www.acmicpc.net/problem/10610)

N = list(input())
N.sort(reverse=True)

sum = 0
for i in N:
    sum += int(i)
if sum % 3 != 0 or '0' not in N: # 30의 배수 : 수의 합이 3으로 나누어 떨어지고, 0이 포함되어 있어야 한다.
    print(-1)
else:
    print(''.join(N))