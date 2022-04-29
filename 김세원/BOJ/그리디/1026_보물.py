n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = 0

a.sort()

for i in range(n):
    s += a[i] * b.pop(b.index(max(b)))
    
print(s)
