T = int(input())

for i in range(T):
    sum = 0
    array = list(map(int, input().split()))
    for data in array:
        if data % 2 != 0:
            sum += data
    print(f'#{i + 1}', sum)