n = int(input())

for i in range(n):
    data = list(map(int, input().split()))

    data.sort()

    print(f'#{i+1}', max(data))
