def solution(N, M, K, arr):
    lst.sort()

    first = lst[-1]
    second = lst[-2]

    result = 0

    while True:
        for i in range(K):
            if M == 0:  # M이 0이면 탈출
                break
            result += first
            M -= 1  # 더할 때마다 1씩 빼기
        if M == 0:  # M이 0이면 탈출
            break
        result += second  # 두 번재 큰 수를 한번 더하기
        M -= 1  # 더할때마다 1씩 빼기
    return result


def solution2():
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))

    data.sort()
    first = data[-1]
    second = data[-2]

    count = int(m / (k + 1)) * k
    count += m % (k + 1)

    result = 0
    result += (count) * first
    result += (m - count) * second

    return result


if __name__ == '__main__':
    N = 5
    M = 8
    K = 3
    lst = [2, 4, 5, 4, 6]
    print(solution(N, M, K, lst))
