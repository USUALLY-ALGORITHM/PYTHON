# 소수 (https://www.acmicpc.net/problem/2581)

M = int(input())
N = int(input())

prime_number = []
for i in range(M, N + 1):
    flag = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            prime_number.append(i)

if len(prime_number) > 0:
    print(sum(prime_number))
    print(min(prime_number))
else:
    print(-1)
