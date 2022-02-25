N = int(input())
array = []

for _ in range(N):
    array.append(input().split())
array = sorted(array, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(len(array)):
    print(array[i][0])