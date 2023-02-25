n = int(input())
data = list(map(int, input().split()))
result = []
data.sort()

if n % 2 != 0:
    for i in range(n//2):
        result.append(data[i]+data[n-i-2])

    if max(result) >= max(data):
        print(max(result))
    else:
        print(max(data))
else:
    for i in range(n//2):
        result.append(data[i]+data[n-i-1])
    print(max(result))
