A,B = map(int, input().split())

count = 0

while True:
    
    if A == B:
        break
    elif B == 0:
        print('-1')
        exit()
    if B % 2 == 1:
        B -= 1
        B = B / 10
    else:
        B //= 2
    count += 1

print(count+1)
