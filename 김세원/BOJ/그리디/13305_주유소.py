n = int(input())
k = list(map(int, input().split()))
l = list(map(int, input().split()))

result = 0
min_l = l[0]

for i in range(n-1):
    if l[i] < min_l:
        min_l = l[i]

    result += min_l * k[i]

print(result)
