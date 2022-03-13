n = int(input())
cnt = 1

while n>1:
    n -= 6*cnt
    cnt+=1

print(cnt)
