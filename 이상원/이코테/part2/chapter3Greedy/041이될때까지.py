def mySolution(N, K):
    count = 0

    while True:
        if N == 1:
            break
        if N % K == 0:
            N /= K
        else:
            N -= 1
        count += 1
    return count


def solution():
    # 입력 받기
    n, k = map(int, input().split())

    result = 0

    while True:
        # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
        target = (n // k) * k
        result += (n - target)
        n = target
        # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
        if n < k:
            break
        result += 1
        n //= k

    # 마지막으로 남은 수에 대해 1씩 빼기
    result += (n - 1)
    return result


if __name__ == '__main__':
    N = 25
    K = 3
    print(mySolution(N, K))
    print(solution())
