n = int(input())
cnt = 0

# if n % 5 != 0 and n % 3 != 0:
#     cnt = -1

# while n!=0:
#     n = n // 5
#     cnt += n
#     n = (n % 5) // 3
#     cnt += n
while n>=0:
    if n % 5 == 0:
        cnt += int(n//5)
        print(cnt)
        break

    n -= 3
    cnt += 1

else:
    print(-1)
