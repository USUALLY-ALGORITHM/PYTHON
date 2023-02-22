n = int(input())
# coin_list = [2, 5]
count = 0

if n < 1:
    print(-1)
# for coin in coin_list:
while n % 5 != 0:
    n -= 2
    count += 1

count += n // 5

print(count)

