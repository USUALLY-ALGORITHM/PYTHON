t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    floor = [i for i in range(1, n+1)]

    for j in range(k):
        for x in range(1, n):
            floor[x] += floor[x-1]
    print(floor[-1])
