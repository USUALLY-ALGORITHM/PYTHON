N = int(input())
array = list(map(int, input().split()))

array.sort()
if N % 2 == 0:
    print(array[N // 2 - 1])
else:
    print(array[N // 2])