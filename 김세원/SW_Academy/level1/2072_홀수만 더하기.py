n = int(input())

for i in range(n):
    data = list(map(int, input().split()))
    sum = 0
    for x in data:
        if x % 2 != 0:
            sum += x

    print(f'#{i + 1}', sum)
