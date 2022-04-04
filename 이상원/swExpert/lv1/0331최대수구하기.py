n = int(input())
answer = []
for item in range(n):
    nums = list(map(int, input().split()))
    nums.sort()
    answer.append(nums[-1])

for item in range(n):
    print(f'#{item+1} {answer[item]}')
