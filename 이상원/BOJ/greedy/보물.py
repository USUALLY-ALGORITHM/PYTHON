n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))  # 재배열 하면 안됨

a.sort()
result = 0
for i in a:
    result += i * b.pop(b.index(max(b)))

print(result)
