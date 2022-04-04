def sol(n):
    timer = [5 * 60, 60, 10]

    cnt = []
    for i in timer:
        cnt.append(n // i)
        n %= i
    if n != 0:
        print(-1)
    else:
        print(*cnt)


if __name__ == '__main__':
    n = [100, 189]
    for i in n:
        sol(i)
