# 베르트랑 공준 (https://www.acmicpc.net/problem/4948)

while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    prime_list = [True] * (2 * n + 1)  # 모든 수가 소수 라고 가정
    for i in range(2, int((n * 2) ** 0.5) + 1):
        if prime_list[i]: # i가 소수인 경우
            for j in range(i + i, n * 2 + 1, i): # i 이후의 i의 배수들을 False로 판정
                prime_list[j] = False

    for x in range(n + 1, 2 * n + 1):
        if prime_list[x] == True:
            count += 1

    print(count)