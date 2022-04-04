n = int(input())
answer = []
for item in range(n):
    arr = list(map(int, input().split()))
    listAvg = sum(arr) / 10
    answer.append(round(listAvg))

for item in range(n):
    print(f'#{item+1} {answer[item]}')
