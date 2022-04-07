"""
https://www.acmicpc.net/problem/2839

"""

num = int(input())
count = 0

while num >= 0:
    if num % 5 == 0:
        count += int(num // 5)
        print(count)
        break

    num -= 3
    count += 1

else:
    print(-1)

# def solution(num):


nums = [18, 4, 6, 9, 11, 15, 22, 33]
for i in nums:
    solution(i)
