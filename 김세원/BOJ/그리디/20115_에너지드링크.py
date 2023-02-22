n = int(input())
drink = list(map(int, input().split()))
result = 0

drink.sort(reverse=True)

for i in range(1, n):
    result = drink[i-1] + (drink[i]/2)
    drink[i] = result

print(result)
