time = int(input())

if time % 10 != 0:
    print(-1)
else:
    A = B = C = 0
    A = time // 300
    B = (time % 300) // 60
    C = (time % 300) % 60 // 10
    print(A, B, C)
