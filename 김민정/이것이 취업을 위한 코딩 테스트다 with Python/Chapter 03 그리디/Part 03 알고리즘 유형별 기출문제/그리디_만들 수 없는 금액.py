N = int(input())
array = list(map(int, input().split()))
array_sum = sum(array)

answer = []
for i in range(N):
    for j in range(i + 1, N + 1):
        answer.append(sum(array[i:j]))

result = 1e9
for i in range(1, array_sum):
    if i not in answer:
        result = min(result, i)

print(result)
