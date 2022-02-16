n = int(input())
data = list(map(int, input().split()))
result = 0

data.sort()

for i in range(n):
    for j in range(i+1):
        result += data[j]
    
print(result)
