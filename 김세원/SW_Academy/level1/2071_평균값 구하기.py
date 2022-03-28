n = int(input())

for i in range(n):
    data = list(map(int, input().split()))
    sum = 0

    for x in data:
        sum += x

    print(f'#{i + 1}', round(sum/10))
